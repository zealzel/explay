from explay.source import ExPlay
from explay.utils import pd_set_option

pd_set_option(max_colwidth=80, max_columns=15)

home_2p = "examples/hr-bonus-2p"

home_typ_merge_all = "examples/typical/merge_all"

home_typ_merge_sheets = "examples/typical/merge_sheets"

home_typ_merge_files_1 = "examples/typical/merge_files_1"
home_typ_merge_files_2 = "examples/typical/merge_files_2"


if __name__ == "__main__":
    home = home_typ_merge_all
    proj = "project"
    ee = ExPlay(home=home, proj_name=proj)
    ee.run_proj(to_excel=False)
    ee.export_inputs()
    ee.export_parsers()

    #  out = df.assign(orders=df.orders.str.strip().str.split("[\s、，/&]+")).explode(
    #  "orders"
    #  )

    #  df.to_excel("out.xlsx")

"""
ref: https://stackoverflow.com/questions/47571618/how-to-split-expand-a-string-value-into-several-pandas-dataframe-rows
    df.assign(genres=df.genres.str.split(', ')).explode('genres')


for my case
    df.assign(orders=df.orders.str.strip().str.split('[\s、]+')).explode('orders')
"""
