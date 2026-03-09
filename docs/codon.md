# Codon ライブラリ説明

Codon 実装は `codon/src`、verify テストは `codon/test` に配置します。

## 優先実装対象

- Lowest Common Ancestor（LCA）
- Rolling Hash（静的版: 累積和）
- Rolling Hash（動的版: セグ木）

## 実装方針

- Python 実装と API をなるべくそろえる
- Codon 特有の高速化を必要箇所に適用する
- 各モジュールに対応する verify テストを `codon/test` に追加する
