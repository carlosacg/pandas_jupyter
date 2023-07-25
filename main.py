import pandas as pd
from utils import get_max_country, get_most_sold_products, get_trend, get_correlation

file_path = "online_retail_II.xlsx"
df = pd.read_excel(file_path)

get_max_country(df)
get_most_sold_products(df)
get_trend(df)
get_correlation(df)
