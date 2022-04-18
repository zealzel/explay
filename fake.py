from random import choice, randint
from faker import Faker
import numpy as np
import pandas as pd


size = 20
#  fake = Faker("zh_TW")
fake = Faker()
people = choice([fake.name_male, fake.name_female])
score = lambda: np.clip(int(np.random.normal() * 20 + 60), a_min=1, a_max=99)
group = lambda: choice(range(1, 11))

data = lambda: [[people(), score(), group()] for _ in range(size)]


#  df2 = pd.DataFrame(data(), columns=["name", "address", "email"])
#  df3 = pd.DataFrame(data(), columns=["name", "address", "email"])
#  df2.to_excel(writer, index=None, sheet_name="Sheet3")
#  df3.to_excel(writer, index=None, sheet_name="Sheet4")

out_xlsx = "out.xlsx"
writer = pd.ExcelWriter(out_xlsx, engine="xlsxwriter")

df1 = pd.DataFrame(data(), columns=["name", "score", "group"])
df1.to_excel(writer, index=None, sheet_name="Sheet1")

writer.save()
