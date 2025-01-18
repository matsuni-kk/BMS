# 概要

**Browser-use**の概要からインストール手順、主要機能、および**MCP（Model Context Protocol）**との統合方法までを包括的に整理しています。ClaudeなどのLLMと連携して高度なブラウザ操作を行うシナリオに対応するための参考にしてください。

---

# 1. Browser-useとは

**Browser-use**は、Pythonを用いてAIエージェントがウェブブラウザを操作できるようにするライブラリです。Playwrightを活用してページ遷移や要素取得、マルチタブ管理、ファイルアップロードなどの高度なブラウザ操作を実現します。

LLM（大規模言語モデル）と組み合わせることで、自然言語での指示によるブラウザ自動化が可能となり、単なるスクレイピングから複雑なE2Eテストまで幅広く活用できます。

---

# 2. インストールと構築手順

## 2.1 必要な環境の準備

1. **Pythonバージョン**
    - Python 3.11以上での利用が推奨（3.12でも可）。
2. **仮想環境（venv, uv等）の利用**または
    - 他のライブラリと競合しないように、仮想環境を作成することが推奨されます。
    
    ```bash
    bash
    コピーする
    python -m venv .venv
    source .venv/bin/activate
    
    ```
    
    ```bash
    bash
    コピーする
    uv venv --python 3.11
    source .venv/bin/activate
    
    ```
    

## 2.2 必要なライブラリのインストール

1. **Browser-useライブラリ**
    
    ```bash
    bash
    コピーする
    pip install browser-use
    
    ```
    
2. **Playwrightのインストール**
    
    ```bash
    bash
    コピーする
    playwright install
    
    ```
    
3. **依存パッケージ（必要に応じて）**
    
    ```bash
    bash
    コピーする
    pip install -r requirements.txt
    
    ```
    

## 2.3 環境変数の設定

1. `.env.example` ファイルをコピーして `.env` ファイルを作成し、下記のようにAPIキーやブラウザパスなどを設定します。
    
    ```jsx
    javascript
    コピーする
    OPENAI_API_KEY=your_openai_api_key
    CHROME_PATH=/path/to/chrome
    CHROME_USER_DATA_DIR=/path/to/user/data
    
    ```
    

---

# 3. サンプルコードの実行

以下は、**Browser-use**を使って「Googleで東京の天気を検索する」というタスクを実行する基本的なサンプルコードです。

```python
python
コピーする
import asyncio
from browser_use import Agent, Browser, BrowserConfig
from langchain_openai import ChatOpenAI

async def main():
    # ブラウザ設定（ヘッドレスモードで実行）
    browser = Browser(config=BrowserConfig(headless=True))

    # タスク定義とエージェント初期化
    task = "Googleで東京の天気を検索してください"
    model = ChatOpenAI(model="gpt-4o")  # GPT-4相当のモデル
    agent = Agent(task=task, llm=model, browser=browser)

    # タスク実行
    result = await agent.run()
    print(result)

if __name__ == "__main__":
    asyncio.run(main())

```

---

# 4. カスタムアクションの追加

`controller.action`デコレータを使用すると、独自のアクション（クリックやファイルアップロードなど）を定義してエージェントの操作を拡張できます。

```python
python
コピーする
from browser_use.controller.service import Controller
from browser_use.agent.views import ActionResult

controller = Controller()

@controller.action("Go to the webpage")
def go_to_webpage():
    return ActionResult(extracted_content="https://example.com", include_in_memory=True)

```

---

# 5. WebUIの利用（オプション）

- *WebUI（Gradioベース）**を使用すると、ブラウザを開いて直感的にBrowser-useを操作できます。
1. 起動方法例
    
    ```bash
    bash
    コピーする
    python webui.py --ip 127.0.0.1 --port 7788
    
    ```
    
2. ブラウザで `http://127.0.0.1:7788` にアクセスすると、WebUIが利用可能になります。

---

# 6. Dockerでのセットアップ（オプション）

Docker環境下でBrowser-useを利用したい場合の手順例です。

```bash
bash
コピーする
git clone https://github.com/browser-use/web-ui.git
cd web-ui
docker compose up --build

```

---

# 7. Browser-useの主な機能

1. **ブラウザ操作**
    - Playwrightを活用し、ページ遷移や要素の取得、クリック、スクロール、ファイルアップロードなどの自動化を実現。
2. **マルチタブ管理**
    - 複数タブを同時に開き、各タブに対して操作を並行実行可能。
3. **カスタムアクション**
    - `controller.action`による任意のアクション追加が可能。
4. **LLMとの統合**
    - GPT-4やClaudeなど、さまざまな大規模言語モデルと連携。
5. **自己修正機能**
    - タスク実行時の操作失敗を自動で検知し、再試行する仕組みを提供。

---

# 8. Browser-useが利用可能なLLMモデル

- **OpenAIモデル**: GPT-4、GPT-3.5など
- **Anthropicモデル**: Claude 3.5 など
- **Llamaシリーズ**: MetaのLlama 2や将来的なLlama 3など
- **Geminiシリーズ**: Googleが開発中のGeminiと派生モデル
- **その他のモデル**:
    - Mistralシリーズ
    - Phiシリーズ
    - RedPajama
    - Qwen（通义千问） など
- **LangChain互換LLM**: LangChain対応のモデルはすべて利用可能

---

# 9. Amazon Bedrockモデルとの連携

Amazon BedrockはAnthropic ClaudeやAI21 LabsのJurassic、MetaのLLaMAなどをAPI経由で扱うサービスです。

Browser-useでも、**AWS SDK（Boto3）**を通じてBedrockのモデルを利用できます。

## 9.1 統合サンプルコード例

```python
python
コピーする
import asyncio
import json
import boto3
from browser_use import Agent, Browser, BrowserConfig

# AWS Bedrockクライアント設定
bedrock_client = boto3.client(
    service_name='bedrock-runtime',
    region_name='us-west-2',  # 必要に応じて変更
    aws_access_key_id='YOUR_AWS_ACCESS_KEY',
    aws_secret_access_key='YOUR_AWS_SECRET_KEY'
)

async def main():
    # ブラウザ設定
    browser = Browser(config=BrowserConfig(headless=True))

    # タスク定義
    task = "Amazon Bedrockモデルを使って質問に回答してください"

    # Bedrockモデル呼び出し
    prompt = {"prompt": "What is the capital of Japan?", "max_gen_len": 50}
    response = bedrock_client.invoke_model(
        modelId="anthropic.claude-3",  # 使用するモデルID
        contentType="application/json",
        accept="application/json",
        body=json.dumps(prompt)
    )

    # レスポンス取得
    result = json.loads(response['body'].read())
    generated_text = result.get('generated_text', '')

    # Browser-useエージェントに結果を渡す
    agent = Agent(task=task, llm_response=generated_text, browser=browser)
    await agent.run()

if __name__ == "__main__":
    asyncio.run(main())

```

**注意点**

- ベースとなるモデルの機能がツール使用や特殊APIに対応しているか確認。
- Bedrock利用時は従量課金制のため、使用トークン量に注意が必要。

---

# 10. MCP（Model Context Protocol）との統合

- *MCP（Model Context Protocol）**は、LLMが外部ツールやリソースと連携するためのオープンプロトコルです。ClaudeをはじめとしたMCP対応LLMと、Browser-useでのブラウザ操作を組み合わせることで、より高度なタスクを自然言語でコントロール可能になります。

## 10.1 MCPの概要とBrowser-useとの連携イメージ

1. ClaudeなどのLLMは、MCPサーバーを通じて外部のリソース（ブラウザ・ファイルシステム・データベースなど）へ指示を出せる。
2. MCPサーバーで受け取った指示をPythonスクリプト（Browser-use）に転送。
3. Browser-useはPlaywrightを通じてブラウザを操作し、その結果を再びMCPサーバーに返す。
4. LLMは返された結果をもとに、さらに高度な指示を続ける――というフローが可能。

## 10.2 必要な環境・ツール

1. **Python 3.12以上**
    - Browser-use および MCPサーバーとの連携処理用
2. **Node.js**
    - MCPサーバーをセットアップするために必要
3. **Claude Desktop（または他のMCP対応LLM）**
    - MCPプロトコル対応のLLMが必要

### MCPサーバーのインストール例

```bash
bash
コピーする
npm install -g @modelcontextprotocol/server

```

### Claude Desktopアプリ

- `claude_desktop_config.json`などの設定ファイルで、MCPサーバーとの接続先やポートを指定します。

## 10.3 MCPサーバーとBrowser-useの統合コード例

### (A) MCPサーバーコード例（`mcp_server.js`）

```jsx
javascript
コピーする
const { exec } = require('child_process');

module.exports = {
  "actions": {
    "run_browser_task": async (params) => {
      return new Promise((resolve, reject) => {
        exec(`python run_browser_task.py "${params.task}"`, (error, stdout, stderr) => {
          if (error) {
            reject(stderr);
          } else {
            resolve(stdout);
          }
        });
      });
    }
  }
};

```

- `run_browser_task` はブラウザ操作のタスクをPythonスクリプト側に受け渡すアクション例です。

### (B) Browser-useタスク実行スクリプト（`run_browser_task.py`）

```python
python
コピーする
import sys
import asyncio
from browser_use import Agent, Browser, BrowserConfig

async def main(task):
    browser = Browser(config=BrowserConfig(headless=True))
    # MCP連携例ではLLMを直接呼ばず、代わりにタスク文字列を受け取ってBrowser-useが実行
    agent = Agent(task=task, llm=None, browser=browser)
    result = await agent.run()
    print(result)

if __name__ == "__main__":
    task = sys.argv[1]
    asyncio.run(main(task))

```

## 10.4 MCPサーバーの起動と接続

1. **MCPサーバーの起動**
    
    ```bash
    bash
    コピーする
    node mcp_server.js
    
    ```
    
2. **Claude DesktopなどMCP対応LLMで接続**
    - LLMの設定画面で、MCPサーバーのURLやポートを指定。
3. **操作の流れ**
    1. LLMへプロンプト例：「Googleで最新ニュースを検索して」と指示。
    2. LLMがMCPアクション（`run_browser_task`）を呼び出し、タスクをMCPサーバーへ送信。
    3. MCPサーバーが`run_browser_task.py`を実行して、Browser-useで実際のブラウザ操作を行う。
    4. 結果をMCPサーバー経由でLLMに返す。
    5. LLMはブラウザ操作結果を踏まえて、ユーザーへ回答や次のアクション提案をする。

## 10.5 応用例

- **Webスクレイピング**: Claudeに「特定サイトから商品情報を取得して一覧化」と命じ、結果を返答。
- **E2Eテスト**: LLMに「指定シナリオでテスト実行し、画面遷移結果を報告」と指示。
- **リアルタイム情報取得**: ユーザーの質問に合わせてブラウザ操作し、動的な結果を返す。

## 10.6 注意点

- **セキュリティ**
    - MCPサーバーをインターネット公開する場合は、SSL/TLSやアクセス制限の設定を必須化するなど注意が必要。
- **パフォーマンス**
    - LLM ⇔ MCPサーバー ⇔ Python（Browser-use）という構成のため、通信遅延が発生する場合があります。
- **依存関係管理**
    - Node.jsやPythonライブラリのバージョン互換性に留意。特にPlaywrightはOSやブラウザバージョンとの整合性が必要です。

---

# 11. まとめ

Browser-useは、Playwrightを通じたブラウザ自動化とLLMとの連携を実現する強力なフレームワークです。DockerやWebUIの利用による柔軟な開発・運用環境の構築が可能で、OpenAI・Anthropic・Amazon Bedrockなどの多様なモデルを統合できます。

さらに、**MCP（Model Context Protocol）**を組み合わせることで、ClaudeをはじめとするMCP対応LLMと外部ツールのシームレスな連携を実現でき、継続的かつ高度なブラウザ操作を自然言語で指示することが可能です。E2EテストやWebスクレイピングなど、幅広いユースケースに応用できます。

---

## 参考リンク/ソース例

- [github.com](https://github.com/)
- [chatgpt-lab.com](https://chatgpt-lab.com/)
- [weel.co.jp](https://weel.co.jp/)
- [pc.watch.impress.co.jp](https://pc.watch.impress.co.jp/)
- [note.com](https://note.com/)
- [youtube.com](https://youtube.com/)
- [research.google](https://research.google/)
- [press.opera.com](https://press.opera.com/)
- [kdnuggets.com](https://kdnuggets.com/)
- [simonwillison.net](https://simonwillison.net/)
- [signitysolutions.com](https://signitysolutions.com/)
- [capellasolutions.com](https://capellasolutions.com/)

以上の手順と機能を組み合わせることで、自然言語での高度なブラウザ自動化や情報取得が可能になります。複雑なワークフローや長期的なタスク管理にも対応できるため、実務の効率化から研究・開発案件まで幅広く活用いただけます。