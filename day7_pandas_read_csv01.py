#!__*__coding:utf-8__*__
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mat

font_location = r"c:\windows\fonts\malgun.ttf"
font_name = mat.font_manager.FontProperties(fname=font_location).get_name()
mat.rc('font', family=font_name)

csv = r"Z:\대구인구현황\download\대구광역시 북구_월별인구현황_20170430.csv"

y = pd.read_csv(csv, engine="python")

print(y[5:10])
print(len(y))

print(y.columns)
print(y.구분)
print(y.info())


for i in y.columns:
    print(">>" + i + "<<")

y.columns = [x.strip() for x in y.columns]

print(y.info())

y1 = y[["구분", "세대수", "남", "여"]]
y1.index = y.구분

z1 = y1.plot()
plt.xticks(range(len(y1.index)), y1.index)

for tick in z1.get_xticklabels():
    tick.set_rotation(90)

print(dir(z1))

plt.show()

y1.plot(kind="bar")
plt.show()

y2 = y[["구분", "남", "여"]]
y2.index = y2.구분
y2.plot(kind="hist")
plt.show()

