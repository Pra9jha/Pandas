import pandas as py
data=py.read_csv('/Users/praveen/PycharmProjects/csv/weather_by_cities.csv')
# print(data)
# print("_____________________________________________________________________")
# g=data.groupby("event")
g=data.groupby("city")
# for i , j in g:
#     print(i)
#     print("_*****************************************************************\n\n")
#     print(j)
# g=g.get_group("mumbai",)
# print(g)
print(g.max())
print(g.mean())
print(g.describe())