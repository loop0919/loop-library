from pyhton.src.rolling_hash_static import RollingHashStatic


def test_static_equal() -> None:
    s = "abracadabra"
    rh = RollingHashStatic(s)

    assert rh.equal(0, 4, 7, 11)  # "abra" == "abra"
    assert not rh.equal(0, 3, 3, 6)  # "abr" != "aca"
