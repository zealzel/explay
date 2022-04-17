import pytest
from explay.source import ExPlay
from explay.merger import xlMerger


@pytest.fixture()
def exp_merge_all():
    home = "test/example_projects/merger/merge_all"
    exp = ExPlay(home=home, proj_name="project")
    return exp


@pytest.fixture()
def exp_merge_sheets():
    home = "test/example_projects/merger/merge_sheets"
    exp = ExPlay(home=home, proj_name="project")
    return exp


@pytest.fixture()
def exp_merge_files():
    home = "test/example_projects/merger/merge_files"
    exp = ExPlay(home=home, proj_name="project")
    return exp


def test_merge_all(exp_merge_all):
    exp_merge_all.run_proj(to_excel=False)
    assert True


def test_merge_sheets(exp_merge_sheets):
    exp_merge_sheets.run_proj(to_excel=False)
    assert True


#  def test_merge_files(exp_merge_files):
#  exp_merge_files.run_proj(to_excel=False)
#  assert True
