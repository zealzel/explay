from random import choice
from faker import Faker
import pandas as pd


size = 3
#  fake = Faker("zh_TW")
fake = Faker()
generate_people = choice([fake.name_male, fake.name_female])

data = lambda: [
    [generate_people(), fake.address(), fake.address()] for _ in range(size)
]

df1 = pd.DataFrame(data(), columns=["name", "address", "email"])
df2 = pd.DataFrame(data(), columns=["name", "address", "email"])
df3 = pd.DataFrame(data(), columns=["name", "address", "email"])

out_xlsx = "out.xlsx"
writer = pd.ExcelWriter(out_xlsx, engine="xlsxwriter")
df1.to_excel(writer, index=None, sheet_name="Sheet1")
#  pd.DataFrame().to_excel(writer, sheet_name="Sheet2")
#  df2.to_excel(writer, index=None, sheet_name="Sheet3")
#  df3.to_excel(writer, index=None, sheet_name="Sheet4")
writer.save()
