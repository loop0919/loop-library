# Python ライブラリ説明

Python 実装は `pyhton/src`、verify テストは `pyhton/test` に配置します。

## 収録モジュール

- `lca.py`: Binary Lifting による Lowest Common Ancestor
- `rolling_hash_static.py`: 累積和（prefix hash）による静的 Rolling Hash
- `rolling_hash_segtree.py`: `atcoder.segtree` による更新可能 Rolling Hash

## 依存関係

`rolling_hash_segtree.py` は `ac-library-python` の `atcoder.segtree` を使用します。

- https://github.com/not522/ac-library-python

インストール例:

```bash
pip install git+https://github.com/not522/ac-library-python
```

## テスト方針

- `test_lca.py`: LCA クエリと距離クエリの検証
- `test_rolling_hash_static.py`: 部分文字列比較の検証
- `test_rolling_hash_segtree.py`: 1文字更新後の部分文字列比較の検証
