# loop-library

競技プログラミング向けの **Python / Codon** ライブラリです。

## 目的

- 実戦で使いやすいアルゴリズム・データ構造を整理して提供する
- Python で書いた実装を Codon でも活用しやすくする
- 再利用可能なテンプレートと検証手順をまとめる

## ディレクトリ構成

- `pyhton/src`: Python 実装のソース
- `pyhton/test`: Python 実装の verify テスト
- `codon/src`: Codon 実装のソース
- `codon/test`: Codon 実装の verify テスト
- `docs/`: GitHub Pages 用ドキュメント

## 想定内容

- データ構造（Union-Find, Segment Tree など）
- グラフアルゴリズム（最短路, 木DP, LCA など）
- 数学（mod 演算, 組み合わせ, 素数関連）
- 文字列（Z-algorithm, Rolling Hash など）
- 入出力・テンプレート

## 方針

- まずは正しさと可読性を優先
- 必要に応じて高速化版（Python向け / Codon向け）を併記
- 典型問題での動作確認を行う

## GitHub Pages

GitHub Pages の初期構成として `docs/` を追加しています。

- エントリページ: `docs/index.md`
- Python 説明ページ: `docs/python.md`
- Codon 説明ページ: `docs/codon.md`

公開は GitHub の **Settings > Pages** で Branch を `main`、Folder を `/docs` に設定してください。

## ライセンス

このリポジトリは MIT License の下で公開されています。
詳細は [LICENSE.txt](./LICENSE.txt) を参照してください。
