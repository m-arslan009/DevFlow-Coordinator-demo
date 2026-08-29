from devflow_demo.reporting import completion_ratio


def test_completion_ratio():
    assert completion_ratio(2, 4) == 0.5
