from explay.source import xlManager, ExPlay
from explay.utils import pd_set_option

pd_set_option(max_colwidth=80, max_columns=15)

HOME1 = "examples/test1/"
PROJECT1 = "project1"
PROJECT2 = "project2"


if __name__ == "__main__":

    home = HOME1
    project = PROJECT2

    ee = ExPlay(home, project)
    ee.run_proj(to_excel=False)

    out = df.assign(orders=df.orders.str.strip().str.split("[\s、，/&]+")).explode(
        "orders"
    )
    out.to_excel("out.xlsx")

"""
ref: https://stackoverflow.com/questions/47571618/how-to-split-expand-a-string-value-into-several-pandas-dataframe-rows
    df.assign(genres=df.genres.str.split(', ')).explode('genres')


for my case
    df.assign(orders=df.orders.str.strip().str.split('[\s、]+')).explode('orders')
"""
