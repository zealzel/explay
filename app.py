import json
from explay.source import ExPlay
from explay.utils import pd_set_option
from pretty_html_table import build_table


pd_set_option(max_colwidth=80, max_columns=15)

home_merge_all = "test/example_projects/merger/merge_all"
home_merge_sheets = "test/example_projects/merger/merge_sheets"
home_merge_files = "test/example_projects_v1/merger/merge_files"
home_filter_1 = "test/example_projects/filter/case1"

home_yaml = "test/v2_example_projects/yaml/"
home_2p = "test/v2_example_private/hr-bonus-2p/"
home_4p = "test/v2_example_private/hr-bonus-4p/"


if __name__ == "__main__":
    home = home_4p
    proj = "project"
    ee = ExPlay(home=home, proj_name=proj)
    ee.run_proj(to_excel=True)
    ee.export_inputs()
    ee.export_parsers()
    ee.export_html(projname="excel")
