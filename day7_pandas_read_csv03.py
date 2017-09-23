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
print(z)
print(z.columns)
z.columns = z.iloc[1]
z1 = z.drop(["범죄대분류", "범죄중분류", "계"])

print(z1)
#z["지역"] = [x.split(" ")[-1] for x ]

z1["지역"] = [x.split(" ")[-1] for x in z1.index]

print(z1)



csv = r"data_draw_korea.csv"

m = pd.read_csv(csv, encoding="utf-8", engine="python")
print(m)

y = z1.merge(m,  how = 'left', left_on = '지역', right_on = 'shortName')
print(y)

y = y[y.x.notnull()]

def convert_float(i):
    i = i.replace(",", "")
    if i.isdigit():
        return float(i)
    else:
        return 0

y["절도2"] = y["절도"].apply(lambda x : convert_float(x))

y.to_excel("output.xlsx")
import korea_showMap
y.index = y.shortName
y.reindex()
#y..pivot(index='y', columns='x', values=targetData)
for i in y.index:
    print(i)
#drawKorea('소멸위기지역', pop, '광역시도', '시도', 'Reds')
korea_showMap.drawKorea("절도2", y, "광역시도", "행정구역", "Reds")