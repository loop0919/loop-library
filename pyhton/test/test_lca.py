from pyhton.src.lca import LCA


def test_lca_query_and_dist() -> None:
    # 0-1, 0-2, 1-3, 1-4, 2-5
    edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5)]
    lca = LCA(6, edges)

    assert lca.query(3, 4) == 1
    assert lca.query(3, 5) == 0
    assert lca.query(2, 5) == 2
    assert lca.dist(3, 4) == 2
    assert lca.dist(3, 5) == 4
