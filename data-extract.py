import pandas as pd
pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/blood-transfusion/transfusion.data').to_csv('transfusion_data.csv', index = False)