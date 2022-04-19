import pytest
from explay.source import ExPlay


@pytest.fixture()
def exp1():
    home = "test/v2_example_projects/yaml/"
    exp = ExPlay(home=home, proj_name="project")
    return exp


def test_filter_case1(exp1):
    exp1.run_proj(to_excel=False)
    assert True
