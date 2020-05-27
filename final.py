import pandas as pd
df4=pd.read_csv("file4.csv")
df5=pd.read_csv("file5.csv")

df=pd.merge(df4,df5,on="etag")
#print(df)

df.to_csv("merged4_5.csv")

df6=pd.read_csv("file6.csv")
df=pd.merge(df5,df6,on="etag")
df.to_csv("merged5_6.csv")

df7=pd.read_csv("file7.csv")
df=pd.merge(df6,df7,on="etag")
df.to_csv("merged6_7.csv")

df8=pd.read_csv("file8.csv")
df=pd.merge(df7,df8,on="etag")

df.to_csv("merged7_8.csv")


df9=pd.read_csv("file9.csv")
df=pd.merge(df8,df9,on="etag")
df.to_csv("merged8_9.csv")

df10=pd.read_csv("file10.csv")
df=pd.merge(df9,df10,on="etag")
df.to_csv("merged9_10.csv")