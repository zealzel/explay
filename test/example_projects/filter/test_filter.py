import pytest
from explay.source import ExPlay


@pytest.fixture()
def exp1():
    home = "test/example_projects/filter/case1"
    exp = ExPlay(home=home, proj_name="project")
    return exp


def test_filter_case1(exp1):
    exp1.run_proj(to_excel=False)
    assert True
