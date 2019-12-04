import pandas as pd
import numpy as np
# Exercise 1
dd = [2 , 4 , 6 , 8 , 10]
ddf = pd.Series(dd)
print(ddf)

# Exercise 2
d1 ={'a':100 , 'b':200 , 'c':300 , 'd':400 , 'e':800}
s = pd.Series(d1)
print(s)


# Exercise 3
data = [20 , 10 , 150 , 110 , 100 , 50]
d2 = pd.Series(data)
#d2.plot(kind="bar")

# Exercise 4
Data = {'d1':[100,200,5,400,700,100,200,50,400,700],
        'd2':[140,0,300,400,200,140,0,700,400,200]}
d3 = pd.DataFrame(Data)
print(d3.describe())
#d3.plot()


# Exercise 5
data2 = {'X':[78,85,96,80,86], 
              'Y':[84,94,89,83,86],
              'Z':[86,97,96,72,83]}
print(pd.DataFrame(data2))

# Exercise 6
df5 = {
    'name': ["Bob", "Jessica", 'Mary', "John", "Mel"],
    'births': [986, 155, 77, 578, 973]
}

df5 = pd.DataFrame(df5)
plot = df5.plot.pie(y='births', figsize=(5, 5))


# Exercise 7

df6 = pd.read_csv('myDataFrame.csv', sep='\t', index_col=0)
print(df6)
df6.describe()

df6.to_csv('df2.csv', sep=',', encoding='utf-8')


# Exercise 8
dates = pd.date_range('20000101' , periods=4)
df = pd.DataFrame(np.random.randn(4, 2), index = dates, columns = ['A', 'B'] )
print(df)
print(df.head(2))
print(df[['A']])
print(df[0:1])
print(df['20000102':'20000104'])
print(df.loc['20000102':'20000104' ,['A']])
print(df.iloc[:,1:2])
print(df[df>0])
df['A'] = [100 , 200, 300 ,100]
print(df)
print(df[df['A'].isin([200,300])])



