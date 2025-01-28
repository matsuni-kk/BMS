# 目的

このルールは、URLからMarkdownファイルを作成するツールの開発と運用をガイドするために作成されました。
LangChainのUnstructuredHTMLLoaderを使用して、より正確なコンテンツ抽出を実現します。

# 前提条件

- Python 3.8以上
- requests
- langchain-community
- unstructured（HTMLパーサー用）

# ディレクトリ構造

```
url_md/
├── url_md.py          # メインスクリプト
├── ai_agent_rule.md   # このルールファイル
├── output/            # 変換結果の出力先
└── packages/          # 依存パッケージ
    └── url_md/       
        └── requirements.txt
```

# 実行手順

1. 必要なライブラリをインストールします。
   ```bash
   pip install requests langchain-community unstructured
   ```

2. スクリプトを実行し、変換したいURLを引数として渡します。
   ```bash
   python url_md.py <URL>
   ```
   （例）`python url_md.py https://example.com`

3. 変換されたMarkdownファイルは`output`ディレクトリに保存されます。
   ファイル名の形式: `[ドメイン名]_[タイムスタンプ].md`

# ファイルの保護

- 出力されたMarkdownファイルは読み取り専用として扱います
- 変更が必要な場合は、新しいファイルとして保存してください
- 元のファイルの上書きは禁止されています

# テスト

テストを実行するには、以下のコマンドを使用します。

```bash
pytest
```

# 注意事項

- このツールは、LangChainのUnstructuredHTMLLoaderを使用してコンテンツを抽出します
- JavaScriptで動的に生成されるコンテンツは取得できない場合があります
- 大量のURLを処理する場合は、サーバーの負荷を考慮してリクエスト間隔を適切に設定してください
- 取得したコンテンツは自動的に`output`ディレクトリに保存され、上書き防止のため一意のタイムスタンプが付与されます

# エラー処理

- URLが無効な場合は適切なエラーメッセージを表示
- ネットワークエラーの場合は再試行を推奨
- パース失敗時は部分的な結果でも保存

# 責任

- このツールの開発者は、ツールの使用によって生じたいかなる損害に対しても責任を負いません
- ユーザーは、自己の責任においてツールを使用してください

# 変更履歴

- 2025-01-28: LangChain実装への移行、ファイル保護機能の追加
- 2025-01-20: 初版作成