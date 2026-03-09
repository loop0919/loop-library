"""Dynamic rolling hash with `atcoder.segtree.SegTree` from ac-library-python.

Dependency:
    pip install git+https://github.com/not522/ac-library-python
"""

from atcoder.segtree import SegTree


class RollingHashSegTree:
    def __init__(self, s: str, base: int = 911382323, mod: int = 1_000_000_007) -> None:
        self.n = len(s)
        self.base = base
        self.mod = mod
        self.pow = [1] * (self.n + 1)
        for i in range(self.n):
            self.pow[i + 1] = (self.pow[i] * base) % mod

        def op(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
            h1, l1 = a
            h2, l2 = b
            return ((h1 * self.pow[l2] + h2) % self.mod, l1 + l2)

        self.seg = SegTree(op, (0, 0), [(ord(ch), 1) for ch in s])

    def set_char(self, i: int, ch: str) -> None:
        self.seg.set(i, (ord(ch), 1))

    def hash(self, l: int, r: int) -> int:
        return self.seg.prod(l, r)[0]

    def equal(self, l1: int, r1: int, l2: int, r2: int) -> bool:
        return (r1 - l1 == r2 - l2) and (self.hash(l1, r1) == self.hash(l2, r2))
