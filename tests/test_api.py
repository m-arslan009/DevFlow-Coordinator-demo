from devflow_demo.api import task_payload


def test_task_payload():
    assert task_payload(4, 'Review')['id'] == 4
