#!__*__coding:utf-8__*__
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as matp

font_location = "c:/windows/fonts/malgun.ttf"
font_name = matp.font_manager.FontProperties(fname=font_location).get_name()
matp.rc("font", family=font_name)

df = pd.read_excel("스타벅스거르기2.xlsx")

df["지역명"] = df["시도명"] + "_" + df["시군구명"]
df2 = df[["지역명","상호명"]]
gf = df2.groupby("지역명").count()
gf = gf.reset_index()
gf.index = gf.지역명
gf.plot(kind="bar", title="스타벅스 수")
print(help(gf.plot))

plt.show()

