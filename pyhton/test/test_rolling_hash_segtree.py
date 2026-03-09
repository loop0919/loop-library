import pytest


atcoder = pytest.importorskip("atcoder.segtree")

from pyhton.src.rolling_hash_segtree import RollingHashSegTree


def test_segtree_hash_update_and_equal() -> None:
    rh = RollingHashSegTree("abcdef")
    assert rh.equal(0, 3, 3, 6) is False

    rh.set_char(3, "a")
    rh.set_char(4, "b")
    rh.set_char(5, "c")

    assert rh.equal(0, 3, 3, 6) is True
