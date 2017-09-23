#!__*__coding:utf-8__*__
#"난 수정이야!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

x =  [ [100,100], [200,200] ]
y =  [ [100,200], [100,200] ]
z =  [ [120,110], [2000,2150] ]

x = np.array(x)
y = np.array(y)
z = np.array(z)


plt.pcolor( x, y, z )


plt.pcolor( x, y, z, cmap='jet', shading='faceted' )

"""
title = "test"
plt.pcolor( x, y, z, cmap='jet', vmin=0, vmax=3000, shading='faceted' )
plt.axis([x.min(), x.max(), y.min(), y.max()])
plt.title( title )
plt.xlabel( 'X value' )
plt.ylabel( 'Y value' )
plt.colorbar()
plt.show()
plt.savefig( 'filename.svg', format='svg' )
"""


#fig, ax = plt.subplots()

image = np.random.uniform(size=(4, 4))
print(image)

title = "test"
plt.imshow(image, cmap='jet', vmin=0, vmax=1, interpolation='nearest', alpha=0.5)
#plt.axis([0, 3, 0, 3])
plt.title( title )
plt.xlabel( 'X value' )
plt.ylabel( 'Y value' )
plt.xticks([0,1,2,3], ["A", "B", "C", "D"])
plt.colorbar()
plt.show()


"""
plt.savefig( 'filename.svg', format='svg' )


#ax.imshow(image, cmap="jet" plt.cm.gray, interpolation='nearest')
ax.imshow(image, cmap="jet", interpolation='nearest')
ax.set_title('dropped spines')
ax.colorbar()
# Move left and bottom spines outward by 10 points
ax.spines['left'].set_position(('outward', 10))
ax.spines['bottom'].set_position(('outward', 10))
# Hide the right and top spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
# Only show ticks on the left and bottom spines
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')

plt.show()
"""