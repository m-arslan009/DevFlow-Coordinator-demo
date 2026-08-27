from devflow_demo.reviews import latest_review


def test_latest_review():
    assert latest_review(['COMMENTED', 'APPROVED']) == 'APPROVED'
