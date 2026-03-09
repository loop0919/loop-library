"""Lowest Common Ancestor (Binary Lifting)."""

from collections import deque


class LCA:
    def __init__(self, n: int, edges: list[tuple[int, int]], root: int = 0) -> None:
        self.n = n
        self.g = [[] for _ in range(n)]
        for u, v in edges:
            self.g[u].append(v)
            self.g[v].append(u)

        self.log = (n - 1).bit_length()
        self.parent = [[-1] * n for _ in range(self.log)]
        self.depth = [-1] * n

        self._build(root)

    def _build(self, root: int) -> None:
        q = deque([root])
        self.depth[root] = 0
        self.parent[0][root] = -1

        while q:
            v = q.popleft()
            for to in self.g[v]:
                if self.depth[to] != -1:
                    continue
                self.depth[to] = self.depth[v] + 1
                self.parent[0][to] = v
                q.append(to)

        for k in range(1, self.log):
            prev = self.parent[k - 1]
            curr = self.parent[k]
            for v in range(self.n):
                p = prev[v]
                curr[v] = -1 if p == -1 else prev[p]

    def query(self, u: int, v: int) -> int:
        if self.depth[u] < self.depth[v]:
            u, v = v, u

        diff = self.depth[u] - self.depth[v]
        bit = 0
        while diff:
            if diff & 1:
                u = self.parent[bit][u]
            diff >>= 1
            bit += 1

        if u == v:
            return u

        for k in range(self.log - 1, -1, -1):
            pu = self.parent[k][u]
            pv = self.parent[k][v]
            if pu != pv:
                u, v = pu, pv

        return self.parent[0][u]

    def dist(self, u: int, v: int) -> int:
        w = self.query(u, v)
        return self.depth[u] + self.depth[v] - 2 * self.depth[w]
