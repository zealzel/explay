import argparse
import warnings
from pathlib import Path

from explay.source import ExPlay
from explay.utils import pd_set_option, register_func

warnings.simplefilter("ignore")
pd_set_option(max_colwidth=80, max_columns=15)


if __name__ == "__main__":
    """
    Usage:
        python app.py --home=/path/to/proj/dir --proj=project
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("--home", type=str, help="project home directory", default="")
    parser.add_argument("--proj", type=str, help="project name", default="project")
    args = parser.parse_args()
    home, proj = args.home, args.proj

    workdir = str(Path(home).resolve())
    register_func(workdir)
    ee = ExPlay(home=workdir, proj_name=proj)
    ee.run_proj(to_excel=False)

    #  ee.inputs["df"].to_excel("out.xlsx")
    #  ee.export_inputs()
    #  ee.export_parsers()
    #  ee.export_html(projname="excel")
