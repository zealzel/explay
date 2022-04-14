from explay.source import ExPlay
from explay.utils import pd_set_option

pd_set_option(max_colwidth=80, max_columns=15)

PROJECT1 = "project1"
PROJECT2 = "project2"

home_typ_merge_files = "examples/typical/merge_files_2"
proj_typ_merge_files = "project"
home = home_typ_merge_files
proj = proj_typ_merge_files


if __name__ == "__main__":
    ee = ExPlay(home=home, proj_name=proj)
    ee.run_proj(to_excel=False)

    #  out = df.assign(orders=df.orders.str.strip().str.split("[\s、，/&]+")).explode(
    #  "orders"
    #  )

    df.to_excel("out.xlsx")

"""
ref: https://stackoverflow.com/questions/47571618/how-to-split-expand-a-string-value-into-several-pandas-dataframe-rows
    df.assign(genres=df.genres.str.split(', ')).explode('genres')


for my case
    df.assign(orders=df.orders.str.strip().str.split('[\s、]+')).explode('orders')
"""
