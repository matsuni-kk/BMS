#!/usr/bin/env node
import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import {
  CallToolRequestSchema,
  ErrorCode,
  ListToolsRequestSchema,
  McpError,
} from '@modelcontextprotocol/sdk/types.js';
import { BedrockRuntimeClient, InvokeModelCommand } from "@aws-sdk/client-bedrock-runtime";

// AWS Bedrockクライアントの設定
const bedrock = new BedrockRuntimeClient({
  region: process.env.AWS_REGION || 'us-east-1'
});

// デフォルトモデルID
const DEFAULT_MODEL_ID = "anthropic.claude-v2";

interface BedrockResponse {
  content: Array<{
    text: string;
  }>;
}

class BedrockServer {
  private server: Server;

  constructor() {
    this.server = new Server(
      {
        name: 'bedrock',
        version: '0.1.0',
      },
      {
        capabilities: {
          tools: {},
        },
      }
    );

    this.setupToolHandlers();
    
    // エラーハンドリング
    this.server.onerror = (error: Error): void => {
      console.error('[MCP Error]', error);
    };

    process.on('SIGINT', async () => {
      await this.server.close();
      process.exit(0);
    });
  }

  private setupToolHandlers(): void {
    // ツール一覧の定義
    this.server.setRequestHandler(ListToolsRequestSchema, async () => ({
      tools: [
        {
          name: 'invoke_bedrock',
          description: 'Amazon Bedrockのモデルを呼び出す',
          inputSchema: {
            type: 'object',
            properties: {
              model: {
                type: 'string',
                description: 'モデルID (anthropic.claude-v2など)',
              },
              prompt: {
                type: 'string',
                description: 'プロンプト',
              },
            },
            required: ['prompt'],
          },
        },
      ],
    }));

    // ツール呼び出しの実装
    this.server.setRequestHandler(CallToolRequestSchema, async (request) => {
      if (request.params.name !== 'invoke_bedrock') {
        throw new McpError(
          ErrorCode.MethodNotFound,
          `Unknown tool: ${request.params.name}`
        );
      }

      const args = request.params.arguments as {
        model?: string;
        prompt: string;
      };

      try {
        // Bedrockモデルの呼び出し
        const command = new InvokeModelCommand({
          modelId: args.model || DEFAULT_MODEL_ID,
          body: JSON.stringify({
            anthropic_version: "bedrock-2023-05-31",
            messages: [
              {
                role: "user",
                content: args.prompt
              }
            ],
            max_tokens: 2048,
            temperature: 0.7
          }),
          contentType: "application/json",
          accept: "application/json",
        });

        const response = await bedrock.send(command);
        const responseBody = JSON.parse(
          new TextDecoder().decode(response.body)
        ) as BedrockResponse;
        
        return {
          content: [
            {
              type: 'text',
              text: responseBody.content[0].text,
            },
          ],
        };
      } catch (error: unknown) {
        console.error('Bedrock API Error:', error);
        return {
          content: [
            {
              type: 'text',
              text: `Bedrock API error: ${error instanceof Error ? error.message : String(error)}`,
            },
          ],
          isError: true,
        };
      }
    });
  }

  async run(): Promise<void> {
    const transport = new StdioServerTransport();
    await this.server.connect(transport);
    console.error('Bedrock MCP server running on stdio');
  }
}

const server = new BedrockServer();
server.run().catch((error: Error) => console.error(error));
