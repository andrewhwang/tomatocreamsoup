#!__*__coding:utf-8__*__

import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mat

font_location = r"c:\windows\fonts\malgun.ttf"
font_name = mat.font_manager.FontProperties(fname=font_location).get_name()
mat.rc('font', family=font_name, size=10)

######################################
csv = r"starbucks_지역별_상점수.xlsx"
yy = pd.read_excel(csv, encoding="utf-8")
yy["지역명"] = yy.광역시도 + " " + yy.행정구역
zz = yy[["지역명", "상호명"]]
zz.columns = ["지역명", "스타벅스수"]
zz.스타벅스수[zz.스타벅스수.isnull()] = 0
zz = zz.sort_values(["스타벅스수"], ascending=False)
zz.index = zz.지역명
zz = zz.head(30) #[0:50, :]
print(zz)

#__call__(self, x=None, y=None, kind='line', ax=None, subplots=False, sharex=None, sharey=False, layout=None, figsize=None, use_index=True, title=None, grid=None, legend=True,
# style=None, logx=False, logy=False, loglog=False, xticks=None, yticks=None, xlim=None, ylim=None, rot=None, fontsize=None, colormap=None, table=False, yerr=None,
#  xerr=None, secondary_y=False, sort_columns=False, **kwds)

#https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.plot.html

ax = zz.plot(figsize=(8,10), kind="bar", color="green", position=0)

pos1 = ax.get_position() # get the original position
pos2 = [pos1.x0 , pos1.y0 + 0.15,  pos1.width, pos1.height - 0.15]

ax.set_position(pos2) # set a new position

for p in ax.patches:
    ax.annotate(str(int(p.get_height())), xy=(p.get_x()  , p.get_height() + 0.5))

plt.show()
print(zz)
