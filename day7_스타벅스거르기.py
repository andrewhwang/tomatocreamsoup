#!__*__coding:utf-8__*__
import pandas as pd

filename = r"Z:\상가업소정보_2017년_6월\상가업소_201706_01.csv"
df = pd.read_csv(filename, engine="python")

df[df.상호명.isnull()] = "상호없음"
df_star = df[df.상호명.str.contains("스타벅스")]

df_star.to_excel("스타벅스거르기2.xlsx")

df_star = pd.read_excel("스타벅스거르기2.xlsx")
df2 = df_star[["상호명", "시도명", "시군구명"]]
gf = df2.groupby(["시도명", "시군구명"]).count()
gf = gf.reset_index()
gf.to_excel("스타벅스_상점수.xlsx")

kf = pd.read_csv(r"Z:\20170923_7일차\data_draw_korea.csv", \
                 engine="python", encoding="utf-8")
result = pd.merge(gf, kf, left_on=["시도명","시군구명"], \
                  right_on=["광역시도", "행정구역"], how="right")

import korea_showMap
korea_showMap.drawKorea('상호명', result, '광역시도', '행정구역', 'Reds')
