#!__*__coding:utf-8__*__

import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mat

font_location = r"c:\windows\fonts\malgun.ttf"
font_name = mat.font_manager.FontProperties(fname=font_location).get_name()
mat.rc('font', family=font_name, size=10)

file = "..\\상가업소정보_2017년_6월\\상가업소_201706_%s.csv"


pds = []
for i in range(1, 2):
    one_file = file % str(i).zfill(2)
    x = pd.read_csv(one_file, engine="python")
    pds.append(x)
z1 = pd.concat(pds)

"""
#file = "..\\상가업소정보_2017년_6월\\상가업소_201706_01.csv_xx.csv"
#file = "..\\상가업소정보_2017년_6월\\상가업소_201706_01.csv"

#f = open(file, "rb")
#fout = open(file + "_xx.csv", "wb")
#for i in range(100):
#    fout.write(f.readline())
#z1 = pd.read_csv(file, engine="python")
#print(z1.head(5))
"""

for i in z1.columns:
    print(">>" + i + "<<")

starbucks = z1[z1.상호명.notnull() & z1.상호명.str.contains("스타벅스")]

starbucks = starbucks[["상호명", "시도명", "시군구명"]]
starbucks = starbucks.groupby(["시도명", "시군구명"]).count()
starbucks = starbucks.reset_index()
starbucks.columns = ["시도명", "시군구명", "스타벅스수"]
starbucks.to_excel(".\\star_cafe1.xlsx")

cafebene = z1[z1.상호명.notnull() & z1.상호명.str.contains("이디야")]

cafebene = cafebene[["상호명", "시도명", "시군구명"]]
cafebene = cafebene.groupby(["시도명", "시군구명"]).count()
cafebene = cafebene.reset_index()
cafebene.columns = ["시도명", "시군구명", "이디야수"]
cafebene.to_excel(".\\star_cafe2.xlsx")

star_cafe = starbucks.merge(cafebene, how="outer", on=["시도명", "시군구명"])
star_cafe.to_excel(".\\star_cafe3.xlsx")

#star_cafe.스타벅스수 = star_cafe[star_cafe.스타벅스수.isnull()] = 0
#star_cafe.이디야 = star_cafe[star_cafe.이디야.isnull()] = 0

star_cafe["스타퍼센트"] = \
    star_cafe.스타벅스수 /  (star_cafe.스타벅스수 + star_cafe.이디야수)
star_cafe["이디야퍼센트"] = \
    star_cafe.이디야수 /  (star_cafe.스타벅스수 + star_cafe.이디야수)
star_cafe.to_excel(".\\star_cafe4.xlsx")

g1 = star_cafe[["스타퍼센트", "이디야퍼센트"]]
g1.index = star_cafe.시도명 + "_" + star_cafe.시군구명
ax = g1.plot(kind="bar", stacked=True)

pos1 = ax.get_position() # get the original position
pos2 = [pos1.x0 , pos1.y0 + 0.15,  pos1.width, pos1.height - 0.15]
ax.set_position(pos2) # set a new position

plt.show()
