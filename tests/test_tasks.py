from devflow_demo.tasks import score_task


def test_score_task():
    assert score_task('M') == 3
