import pandas as pd
import dataframe_image as dfi
import os


os.makedirs("screenshots", exist_ok=True)


df = pd.read_csv("data/products.csv")


dfi.export(
    df.head(10),
    "screenshots/csv-output.png"
)


print("CSV screenshot saved!")