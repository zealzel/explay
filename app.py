import json
from explay.source import ExPlay
from explay.utils import pd_set_option
from pretty_html_table import build_table
from explay.utils import register_func
import warnings


#  warnings.filterwarnings("ignore")
warnings.simplefilter("ignore")


pd_set_option(max_colwidth=80, max_columns=15)

home_merge_all = "test/example_projects/merger/merge_all"
home_merge_sheets = "test/example_projects/merger/merge_sheets"
home_merge_files = "test/example_projects_v1/merger/merge_files"
home_filter_1 = "test/v2_example_projects/filter/case1"
home_filter_2 = "test/v2_example_projects/filter/case2"

home_yaml = "test/v2_example_projects/yaml/"
home_2p = "test/v2_example_private/hr-bonus-2p/"
home_4p = "test/v2_example_private/hr-bonus-4p/"

home = "/Users/zealzel/Downloads/My/code/執勤注意力各月清冊"


if __name__ == "__main__":
    home = home_filter_2
    proj = "project"
    register_func(home)
    ee = ExPlay(home=home, proj_name=proj)
    ee.run_proj(to_excel=False)
    ee.export_inputs()

    #  ee.inputs["df"].to_excel("out.xlsx")
    #  ee.export_parsers()
    #  ee.export_html(projname="excel")
