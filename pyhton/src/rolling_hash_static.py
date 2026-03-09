"""Static rolling hash with prefix sums (single modulus)."""


class RollingHashStatic:
    def __init__(self, s: str, base: int = 911382323, mod: int = 1_000_000_007) -> None:
        self.s = s
        self.n = len(s)
        self.base = base
        self.mod = mod

        self.pow = [1] * (self.n + 1)
        self.pref = [0] * (self.n + 1)

        for i, ch in enumerate(s):
            self.pow[i + 1] = (self.pow[i] * base) % mod
            self.pref[i + 1] = (self.pref[i] * base + ord(ch)) % mod

    def hash(self, l: int, r: int) -> int:
        """Return hash of s[l:r]."""
        return (self.pref[r] - self.pref[l] * self.pow[r - l]) % self.mod

    def equal(self, l1: int, r1: int, l2: int, r2: int) -> bool:
        return (r1 - l1 == r2 - l2) and (self.hash(l1, r1) == self.hash(l2, r2))
