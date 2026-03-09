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

## 優先ライブラリ

- Lowest Common Ancestor（LCA）
- Rolling Hash（累積和ベースの静的版）
- Rolling Hash（`atcoder.segtree` ベースの動的版）

> 注: DSU / セグ木本体は AtCoder Library にあるため、このリポジトリでは優先対象外です。

## Python 実装における依存

`atcoder.segtree` 版 Rolling Hash は、以下の `ac-library-python` を利用します。

- https://github.com/not522/ac-library-python

インストール例:

```bash
pip install git+https://github.com/not522/ac-library-python
```

## GitHub Pages

GitHub Pages の初期構成として `docs/` を追加しています。

- エントリページ: `docs/index.md`
- Python 説明ページ: `docs/python.md`
- Codon 説明ページ: `docs/codon.md`

公開は GitHub の **Settings > Pages** で Branch を `main`、Folder を `/docs` に設定してください。

## ライセンス

このリポジトリは MIT License の下で公開されています。
詳細は [LICENSE.txt](./LICENSE.txt) を参照してください。
