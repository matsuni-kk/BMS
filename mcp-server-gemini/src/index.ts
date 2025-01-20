#!/usr/bin/env node
import { GoogleGenerativeAI, GenerativeModel } from '@google/generative-ai';

interface GeminiConfig {
  model: string;
  temperature?: number;
  maxOutputTokens?: number;
}

class GeminiClient {
  private genAI: GoogleGenerativeAI;
  private models: Map<string, GenerativeModel>;

  constructor(apiKey: string) {
    if (!apiKey) {
      throw new Error('API key is required');
    }
    this.genAI = new GoogleGenerativeAI(apiKey);
    this.models = new Map();
  }

  private getModel(config: GeminiConfig): GenerativeModel {
    const modelKey = JSON.stringify(config);
    if (!this.models.has(modelKey)) {
      this.models.set(
        modelKey,
        this.genAI.getGenerativeModel({
          model: config.model,
          generationConfig: {
            temperature: config.temperature,
            maxOutputTokens: config.maxOutputTokens,
          },
        })
      );
    }
    return this.models.get(modelKey)!;
  }

  async generateContent(prompt: string, config: GeminiConfig): Promise<string> {
    try {
      const model = this.getModel(config);
      const result = await model.generateContent(prompt);
      const response = await result.response;
      return response.text();
    } catch (error) {
      console.error('Error generating content:', error);
      throw error;
    }
  }
}

// メインの処理
async function main() {
  const apiKey = process.env.GEMINI_API_KEY;
  if (!apiKey) {
    console.error('GEMINI_API_KEY environment variable is required');
    process.exit(1);
  }

  const client = new GeminiClient(apiKey);

  // 標準入力からプロンプトを受け取る
  process.stdin.setEncoding('utf-8');
  console.error('Gemini client is ready. Enter your prompt:');

  let inputBuffer = '';
  
  process.stdin.on('data', async (chunk) => {
    inputBuffer += chunk;
    
    // 入力が完了したかチェック
    if (inputBuffer.includes('\n')) {
      const prompt = inputBuffer.trim();
      inputBuffer = '';
      
      try {
        const response = await client.generateContent(prompt, {
          model: 'gemini-1.5-pro',
          temperature: 0.7,
          maxOutputTokens: 2048,
        });
        
        // 応答を標準出力に書き込む
        process.stdout.write(JSON.stringify({
          text: response,
        }) + '\n');
      } catch (error) {
        console.error('Error:', error);
        process.stdout.write(JSON.stringify({
          error: error instanceof Error ? error.message : String(error),
        }) + '\n');
      }
    }
  });

  // エラーハンドリング
  process.on('SIGINT', () => {
    console.error('\nShutting down...');
    process.exit(0);
  });

  process.stdin.on('error', (error) => {
    console.error('Error reading from stdin:', error);
    process.exit(1);
  });
}

main().catch((error) => {
  console.error('Fatal error:', error);
  process.exit(1);
});