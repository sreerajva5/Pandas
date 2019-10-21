import pandas as pd

df = pd.read_csv('data.csv')


df['mount'] = df['mount'].str.split(r'\\n')

df2 = df.explode('mount')


df2['mount'] = df2['mount'].map(lambda x: x.split(' on')[0])


df2.to_csv('sliced_data.csv')
