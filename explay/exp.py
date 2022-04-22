import os
import argparse
import warnings
from pathlib import Path

from explay.source import ExPlay
from explay.utils import pd_set_option, register_func

warnings.simplefilter("ignore")
pd_set_option(max_colwidth=80, max_columns=15)


class ExplicitDefaultsHelpFormatter(argparse.ArgumentDefaultsHelpFormatter):
    def _get_help_string(self, action):
        if action.default in (None, False):
            if action.dest == "home":
                return f"{action.help} (default: current workdir)"
            return action.help
        return super()._get_help_string(action)


def main():
    #  parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(formatter_class=ExplicitDefaultsHelpFormatter)
    parser.add_argument("--home", "-H", type=str, help="project home directory")
    parser.add_argument("--proj", type=str, help="project name", default="project")
    parser.add_argument(
        "--export-html",
        action="store_true",
        help="toggle if exporting the parsers output in html form",
        default=False,
    )
    parser.add_argument(
        "--export-merged",
        action="store_true",
        help="toggle if exporting the merged output in xlsx form",
        default=False,
    )
    args = parser.parse_args()
    home = args.home
    proj = args.proj
    export_html = args.export_html
    export_merged = args.export_merged

    if not home:
        print("There is no home assigned! Use current working directory instead.")
        home = os.getcwd()

    filepath = os.path.join(home, f"{proj}.yml")
    if not os.path.isfile(filepath):
        print(f"project yaml file {filepath} does not exist!\n")
        parser.print_help()
        return

    workdir = str(Path(home).resolve())
    register_func(workdir)
    ee = ExPlay(home=workdir, proj_name=proj)
    ee.run_proj(to_excel=False)

    if export_merged:
        ee.export_merged()

    if export_html:
        for name, (inp, parser) in ee._proj.items():
            print("proj name", name)
            ee.export_html(name, f"{name}_output")
    return ee
