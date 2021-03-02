import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import sys


file = sys.argv[1]

df = pd.read_csv(file)
df1 = pd.DataFrame()

# Date	Time	Field	Home	H Score	Away	A Score	game_duration_minutes

df1['game#'] = df['Game Number']
df1['Date'] = df['Game Date']
df1['Time'] = df['Game Start Time']
df1['Field'] = df['Field Name (full)']
df1['Home'] = df['Home Team Name']
df1['Away'] = df['Away Team Name']

df1['Date'] = pd.to_datetime(df1.Date)
df1['Date'] = df1['Date'].dt.strftime('%m/%d/%Y')

df1.to_csv("~/Downloads/plametrics_export.csv")