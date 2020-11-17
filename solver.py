import numpy as np


data = np.array(
[
[0,0,0,0,6,0,7,0,0],
[0,5,9,0,0,0,0,0,0],
[0,1,0,2,0,0,0,0,0],
[0,0,0,1,0,0,0,0,0],
[6,0,0,5,0,0,0,0,0],
[3,0,0,0,0,0,4,6,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,9,1],
[8,0,0,7,4,0,0,0,0]
]
)

#print(data)

maybe = np.zeros((9,9))
var = {}

vert_cond = set(data[0, :])
print("vert_cond: ", vert_cond)
gor_cond = set(data[:, 0])
print("gor cond: ",gor_cond)
cond = set(data[0:2,0:2].flat)
print ("cond: ", cond)

var = {1,2,3,4,5,6,7,8,9}.difference(vert_cond, gor_cond, cond)
print("Возможные варианты: ", var)

