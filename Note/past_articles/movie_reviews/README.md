# 映画レビュー (Movie Reviews)

このディレクトリには、映画に関するレビューや感想を保管します。

## ディレクトリの目的
- 視聴した映画のレビュー保管
- 映画分析の記録
- 映画に関する考察の保存
- 推薦文や批評の管理

## 保管するコンテンツ
- 映画レビュー
- 映画分析記事
- 映画批評
- 映画の感想文
- 作品比較分析

## ディレクトリ構造
```
movie_reviews/
├── by_year/           # 年代別レビュー
├── by_genre/          # ジャンル別レビュー
├── by_director/       # 監督別レビュー
└── special_features/  # 特集記事
```

## ファイル命名規則
- YYYY-MM-DD-movie-title-review.md
  例：2024-01-15-inception-review.md

## メタデータ
各ファイルの冒頭には以下のメタデータを含めること：
```
---
title: 映画タイトル（日本語）
original_title: 原題
release_year: 公開年
director: 監督名
review_date: YYYY-MM-DD
rating: 1-5
tags: [tag1, tag2]
genre: [genre1, genre2]
watched_date: YYYY-MM-DD
status: published/draft
---
```

## レビュー構成
1. 作品基本情報
2. ストーリー概要（ネタバレなし）
3. 評価ポイント
4. 詳細レビュー（必要に応じてネタバレ警告）
5. 総評
6. 推奨対象者

## 注意事項
- ネタバレを含む場合は明確な警告を付けること
- 著作権に配慮した引用・画像使用を心がける
- 主観的な感想と客観的な分析を適切に区別する