from pathlib import Path
import pandas as pd
import numpy as np

app_dir = Path(__file__).parent
raw_df = pd.read_json(app_dir / "covid-19d-vaccination-eu.json")

df = pd.DataFrame(raw_df['records'].tolist())

df = df[df['TargetGroup'] == 'ALL']

df['NumberOfIndivOneDose'] = df['NumberOfIndivOneDose'].replace(['UNK', 'NA'], np.nan)
df['NumberOfIndivOneDose'] = pd.to_numeric(df['NumberOfIndivOneDose'], errors='coerce')

df = df.dropna(subset=['NumberOfIndivOneDose'])

print("Available columns:", df.columns.tolist())
