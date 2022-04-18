from explay.source import ExPlay
from explay.utils import pd_set_option
from pretty_html_table import build_table


pd_set_option(max_colwidth=80, max_columns=15)

home_merge_all = "test/example_projects/merger/merge_all"
home_merge_sheets = "test/example_projects/merger/merge_sheets"
home_merge_files = "test/example_projects_v1/merger/merge_files"
home_filter_1 = "test/example_projects/filter/case1"

home_filter_2 = "test/example_projects_v1/filter/case2"
home_yaml = "test/example_projects_v2/yaml/"


if __name__ == "__main__":
    home = home_yaml
    proj = "project"
    ee = ExPlay(home=home, proj_name=proj)
    ee.run_proj(to_excel=False)
    ee.export_inputs()
    ee.export_parsers()

    parser = ee.parsers["parser1"]
    df = ee.inputs["df"]

    show_rows_max = 10
    with open("out.html", "w") as f:
        title = f"<h4>Merged input</h4>"
        html = title + build_table(df, "blue_light", font_size="10px")
        f.write(html)
        for parser, df in zip(parser, parser.output):
            each_to_show = df[:show_rows_max]
            title = f"<h4>{parser}</h4>"
            html = title + build_table(each_to_show, "blue_light", font_size="10px")
            f.write(html)
