#!__*__coding:utf-8__*__
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mat

font_location = r"c:\windows\fonts\malgun.ttf"
font_name = mat.font_manager.FontProperties(fname=font_location).get_name()
mat.rc('font', family=font_name)

csv = r"D:\ZZ.lecture\20170917_6일차\2015년 범죄발생지%28지역별%29.csv"

y = pd.read_csv(csv, engine="python")
z = y.T


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

