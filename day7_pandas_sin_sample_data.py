#!__*__coding:utf-8__*__


import math
import numpy as np
f = open("sin_cos_test.csv", "w")
f.write("number,sin,cos\n")
for i in np.arange(0, 91, 1):
    j = i / 10.0
    f.write("%f,%f,%f\n" % (j, np.sin(j), np.cos(j)))
f.close()

import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mat

font_location = r"c:\windows\fonts\malgun.ttf"
font_name = mat.font_manager.FontProperties(fname=font_location).get_name()
mat.rc('font', family=font_name, size=10)

file = "sin_cos_test.csv"
data = pd.read_csv(file)
#방법 1
plt.plot(data.number, data.sin, label="sin")
plt.plot(data.number, data.cos, label="cos")
plt.grid()
plt.legend()
plt.title("SIN COS")
plt.show()

#방법 2
data.index = data.number
data = data.drop("number", 1)
data.plot(kind="line")
plt.grid()
plt.legend()
plt.show()
