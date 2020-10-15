import pandas as pd

pdf = pd.read_csv("./data/processed_data/power.csv")

print('DESCRIPTION:\n\n\n{}'.format(pdf.describe()))
print('HEAD:\n\n\n{}'.format(pdf.head()))
# print('DESCRIPTION:\n\n\n{}'.format(df.describe()))
tdf = pd.read_csv("./data/processed_data/temperature.csv")

print('DESCRIPTION:\n\n\n{}'.format(tdf.describe()))
print('HEAD:\n\n\n{}'.format(tdf.head()))
# print('DESCRIPTION:\n\n\n{}'.format(df.describe()))
