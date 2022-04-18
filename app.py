from explay.source import ExPlay
from explay.utils import pd_set_option

pd_set_option(max_colwidth=80, max_columns=15)

home_merge_all = "test/example_projects/merger/merge_all"
home_merge_sheets = "test/example_projects/merger/merge_sheets"
home_merge_files = "test/example_projects/merger/merge_files"
home_filter_1 = "test/example_projects/filter/case1"


if __name__ == "__main__":
    home = home_filter_1
    proj = "project"
    ee = ExPlay(home=home, proj_name=proj)
    ee.run_proj(to_excel=False)
    ee.export_inputs()
    ee.export_parsers()

    #  df.to_excel("out.xlsx", index=None)

"""
ref: https://stackoverflow.com/questions/47571618/how-to-split-expand-a-string-value-into-several-pandas-dataframe-rows
    df.assign(genres=df.genres.str.split(', ')).explode('genres')


for my case
    df.assign(orders=df.orders.str.strip().str.split('[\s、]+')).explode('orders')
"""
