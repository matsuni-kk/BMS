# toolsのai_agent_rule.md

# システムプロンプト

## 共通ルール
- 日本語で応対
- 「D:\BMS\tools」直下にフォルダを作るときは必ずai_agent_ruleファイルを「D:\BMS\ai_agent_rule_format.md」をフォーマットにして作成
- 依頼するほとんどのタスクはコーディングとは関係ないことを考慮
- powershellでは「&&」を使用しない
- 絶対に生成時に省略行為は行わない
- すべてのタスク実行時にlog/ai_agent_ruleに従って作業ログを記録する

## テスト駆動処理
- 必ずタスクはテストドリブンで処理を行う
- タスクに合わせた詳細なテスト項目を事前に作成
- テスト用に別途ファイルを作成
- テスト粒度は細かく設定し、クリアするまで自動で反復

## ワークフロー

重要：必ず各ディレクトリのai_agent_ruleを参照し、ワークフローを把握すること:

workflow:
  tools: |
    toolsディレクトリは、AIを活用した各種ツールを管理するための場所です。
    ここでは、以下のツールを体系的に管理します：
    - ファイル分割ツール（file_splitter）
    - グラフ生成ツール（graph_maker）
    - Markdownファイル生成ツール（markitdown）
    - URL解析・MD変換ツール（url_md）
    - ワードクラウド生成ツール（wordcloud）
    - Windows PC軽量化ツール（pc_lightener）
    - YouTube MP3抽出ツール（youtube4mp3）
    - 音声文字起こしツール（vosk）
    - フォルダ内全ファイルMD変換ツール（markitdown_anyfolder）
    - ディレクトリ構造MD出力ツール（dir_structure_md）
  timing: |
    toolsでの作業を開始する際には、以下の手順で進めてください：

    1. 作業の種類を特定し、適切なサブディレクトリを選択します：
       - ファイル分割ツール → file_splitter
       - グラフ生成 → graph_maker
       - Markdown生成 → markitdown
       - URL解析・MD変換 → url_md
       - ワードクラウド生成 → wordcloud
       - Windows PC軽量化ツール → pc_lightener
       - YouTube MP3抽出ツール → youtube4mp3
       - 音声文字起こしツール → vosk
       - フォルダ内全ファイルMD変換ツール → markitdown_anyfolder
       - ディレクトリ構造MD出力ツール → dir_structure_md

    2. 選択したサブディレクトリのai_agent_ruleを確認します：
       - ディレクトリ固有のルールとガイドラインを理解
       - 必要なテンプレートの場所を確認
       - 作業フローの把握
       - 注意事項の確認

    3. 定められたディレクトリ構造に従って作業を開始します：
       - 必要なフォルダの作成（output/等）
       - 依存パッケージの確認（packages/）
       - ファイルの命名規則の遵守
       - フォルダ階層の維持

    4. 作業ログを適切に記録します：
       - タスク開始時の記録
       - 進捗状況の更新
       - 問題点や課題の記録
       - 完了時の記録

    5. 必要に応じてテストを実施します：
       - テストケースの作成
       - テストの実行
       - 結果の記録
       - 改善点の特定と修正

  file_splitter:
    information: |
      ファイル分割ツールを管理するためのディレクトリです。
      ここでは、ファイル分割ツールの開発、テスト、メンテナンスに関する情報を体系的に管理します。
    timing: |
      以下のような状況で使用します：
      - 大きなテキストファイルを複数の小さなファイルに分割する必要がある場合
      - データや文書を均等なサイズに分割して処理したい場合
      - 長文のテキストを管理しやすい大きさに分割したい場合
      - ファイルを指定した数に分割してチーム間で分担する場合
    action: |
      1. `cd tools/file_splitter`でディレクトリ移動
      2. `python file_splitter.py`を実行（ファイルパスと分割数を引数として指定）
      3. 分割されたファイルは output/ ディレクトリに保存
      4. ファイル名は `{元のファイル名}_split_{番号}{元の拡張子}` 形式
    directory: tools/file_splitter/

  graph_maker:
    information: |
      グラフ生成ツールを管理するためのディレクトリです。
      データの可視化とグラフ作成機能を提供します。
    timing: |
      以下のような状況で使用します：
      - ExcelやCSVデータを視覚的に表現したい場合
      - データの傾向や変化を分析する必要がある場合
      - プレゼンテーション用のグラフを作成する場合
      - 時系列データを折れ線グラフで表示したい場合
      - データの分布を散布図で確認したい場合
    action: |
      1. `cd tools/graph_maker`でディレクトリ移動
      2. `python graph_maker.py`を実行
      3. GUIウィンドウが開くので、ファイルを選択し設定を行う
      4. 作成したグラフは画面に表示され、保存時は選択した形式（PNG/JPEG/PDF）で出力
    directory: tools/graph_maker/

  markitdown:
    information: |
      Markdownファイル生成ツールを管理するためのディレクトリです。
      テキストデータのMarkdown形式への変換を行います。
    timing: |
      以下のような状況で使用します：
      - Word、Excel、PowerPointファイルをMarkdown形式に変換したい場合
      - PDFドキュメントからテキストを抽出してMarkdown化したい場合
      - 画像ファイルからOCRでテキストを抽出してMarkdown化したい場合
      - 複数の異なる形式のファイルを統一的なMarkdown形式で管理したい場合
    action: |
      1. `cd tools/markitdown`でディレクトリ移動
      2. `python markitdown.py`を実行（ファイルパスを引数として指定）
      3. 変換結果は output/ ディレクトリに保存
      4. ファイル名は `{元のファイル名}_{タイムスタンプ}.md` 形式
    directory: tools/markitdown/

  url_md:
    information: |
      URL解析・MD変換ツールを管理するためのディレクトリです。
      Webページの内容をMarkdown形式に変換します。
    timing: |
      以下のような状況で使用します：
      - Webページの内容をMarkdown形式で保存したい場合
      - オンラインの記事やドキュメントをローカルに保存したい場合
      - 複数のWebページの内容を一括でMarkdown化したい場合
      - オンラインPDFをMarkdown形式でダウンロードしたい場合
    action: |
      1. `cd tools/url_md`でディレクトリ移動
      2. `python url_md.py`を実行（URLとモードを引数として指定）
      3. 変換結果は output/ ディレクトリに保存
      4. ファイル名はURLから自動生成
    directory: tools/url_md/

  wordcloud:
    information: |
      ワードクラウド生成ツールを管理するためのディレクトリです。
      テキストデータの視覚化を行います。
    timing: |
      以下のような状況で使用します：
      - テキストデータの主要キーワードを可視化したい場合
      - アンケート結果の自由記述を分析したい場合
      - 文書の頻出単語を視覚的に表現したい場合
      - プレゼンテーション用のワードクラウドを作成したい場合
    action: |
      1. `cd tools/wordcloud`でディレクトリ移動
      2. `python generate_wordcloud.py`を実行（CSVファイルパスと列名を引数として指定）
      3. 生成されたワードクラウドは output/ ディレクトリに保存
      4. ファイル名は `{元ファイル名}_{列名}_wordcloud.png` 形式
    directory: tools/wordcloud/

  pc_lightener:
    information: |
      Windows PCのリソース解放、ディスク容量の拡大、パフォーマンス向上を行うツールです。
      不要なプロセスの終了、一時ファイルの削除、キャッシュのクリア、ディスククリーンアップなどを実行します。
    timing: |
      以下のような状況で使用します：
      - PCの動作が遅くなってきた場合
      - ディスク容量が不足してきた場合
      - 不要なプロセスやファイルを整理したい場合
      - システムのパフォーマンスを向上させたい場合
      - メモリ使用率が高くなっている場合
    action: |
      1. `cd tools/pc_lightener`でディレクトリ移動
      2. `python pc_lightener.py`を管理者権限で実行
      3. 自動的に各最適化処理を実行
      4. 処理結果は標準出力に表示
    directory: tools/pc_lightener/

  youtube4mp3:
    information: |
      YouTubeの動画からMP3形式で音声を抽出するツールです。
      高品質な音声抽出（192kbps）に対応しています。
    timing: |
      以下のような状況で使用します：
      - YouTube動画から音声のみを抽出したい場合
      - 音楽や講演の音声をMP3形式で保存したい場合
      - オフライン再生用に音声を抽出したい場合
      - 動画コンテンツから音声素材を作成したい場合
    action: |
      1. `cd tools/youtube4mp3`でディレクトリ移動
      2. `python youtube_audio_extractor.py`を実行（@は使わずにURLを引数として指定）
      3. 抽出されたMP3は output/ ディレクトリに保存
      4. ファイル名は動画タイトルに基づいて自動生成
    directory: tools/youtube4mp3/

  vosk:
    information: |
      マイクからのリアルタイム音声入力とシステム音声を文字起こしするツールです。
      日本語と英語の音声認識に対応し、タイムスタンプ付きで保存します。
    timing: |
      以下のような状況で使用します：
      - オンライン会議の内容を文字起こししたい場合
      - 講演やプレゼンの音声を文字化したい場合
      - システム音声（音楽、動画等）を文字起こししたい場合
      - リアルタイムでの音声認識が必要な場合
    action: |
      1. `cd tools/vosk`でディレクトリ移動
      2. `python vosk_transcripter.py`を実行
      3. 文字起こし結果は output/YYYYMMDD/ に保存
      4. 1時間ごとに新しいファイルを作成
    directory: tools/vosk/

  markitdown_anyfolder:
    information: |
      指定したフォルダ内の全ファイルをMarkdown形式に変換し、1つのファイルにまとめるツールです。
      様々な形式のファイルに対応し、フォルダ階層を保持したMarkdown生成が可能です。
    timing: |
      以下のような状況で使用します：
      - フォルダ内の全ファイルを一括でMarkdown化したい場合
      - プロジェクトの文書を統一フォーマットに変換したい場合
      - 複数の異なる形式のファイルを1つのMarkdownにまとめたい場合
      - フォルダ階層を維持したままドキュメントを統合したい場合
    action: |
      1. `cd tools/markitdown_anyfolder`でディレクトリ移動
      2. `python markitdown_anyfolder.py`を実行（フォルダパスを引数として指定）
      3. 変換結果は output/ ディレクトリに保存
      4. ファイル名は `combined_YYYYMMDD_HHMMSS.md` 形式
    directory: tools/markitdown_anyfolder/

  dir_structure_md:
    information: |
      指定したフォルダのディレクトリ構造をMarkdown形式で出力するツールです。
      フォルダとファイル名のみを抽出し、リスト形式で表示します。
    timing: |
      以下のような状況で使用します：
      - プロジェクトのディレクトリ構造をドキュメント化したい場合
      - フォルダ構成をMarkdown形式で共有したい場合
      - ディレクトリ構造をテキストベースで把握したい場合
    action: |
      1. `cd tools\dir_structure_md`でディレクトリ移動
      2. 以下のいずれかのコマンドを実行:
         - 【期間指定なしの場合】
           `python dir_structure_md.py <directory_path>`
         - 【期間指定ありの場合】（更新日時によるフィルター機能あり）
           `python dir_structure_md.py <directory_path> "<start_date>" "<end_date>"`
           ※ 日付のフォーマットは `YYYY-MM-DD` （例: "2023-01-01"）
      3. 生成されたMarkdownファイルは output/ ディレクトリに保存されます。
      4. ファイル名は `dir_structure_YYYYMMDD_HHMMSS.md` 形式となります。
    directory: tools/dir_structure_md/
