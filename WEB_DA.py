import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_csv("data-export (1).csv")
# print(df.head())

df.columns = df.iloc[0]
# print(df.head())
df = df.drop(index = 0).reset_index(drop = True)
df.columns = ["channel group", "Datehour", "User", "Session","Engaged Session", "Average engagement time per session", "Engaged sessions per user","Events per session"	, "Engagement rate", "Event count"]
# print(df.head())
df["Datehour"] = pd.to_datetime(df["Datehour"], format="%Y%m%d%H", errors='coerce')
# print(df.head())

numeric_cols = df.columns.drop(["channel group", "Datehour"])
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')
df["Hour"] = df["Datehour"].dt.hour
# print(df.describe())

# Q1 session and user overtime
sns.set(style="whitegrid")
df.groupby("Datehour")[["Session", "User"]].sum().plot(ax=plt.gca())
plt.title("session and user overtime")
plt.xlabel("hour")
plt.ylabel("count")
# print(plt.show())

#Q2 total users by channel
plt.figure(figsize=(8,5))
sns.barplot(data=df, x="channel group", y="User", estimator=np.sum, palette="viridis")
plt.title("total users by channel")
plt.xticks(rotation=45)
# print(plt.show())


# Q3 average engagement time
plt.figure(figsize=(8,5))
sns.barplot(data=df, x="channel group", y="Average engagement time per session", estimator=np.mean, palette="magma")
plt.title("Average engagement time by channel")
plt.xticks(rotation=45)
print(plt.show())

# Q4 engageent rate distribution by channel
plt.figure(figsize=(8,5))
sns.boxplot(data=df, x="channel group", y="Engagement rate", palette="coolwarm")
plt.title("engagement rate distribution")
plt.xticks(rotation=45)
print(plt.show())