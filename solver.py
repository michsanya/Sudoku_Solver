import numpy as np

data = np.array(
    [
        [0, 0, 0, 0, 6, 0, 7, 0, 0],
        [0, 5, 9, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [6, 0, 0, 5, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 4, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 1],
        [8, 0, 0, 7, 4, 0, 0, 0, 0]
    ]
)

maybe = np.empty((9, 9), dtype=np.object)
rang = np.empty((9, 9))
vert_cond = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
gor_cond = [{}, {}, {}, {}, {}, {}, {}, {}, {}]

for i in range(9):
    # Определение доступных вариантов по вертикальным столбцам
    vert_cond[i] = set(data[:, i].flat)
    # Определение доступных вариантов по горизонтальным строкам
    gor_cond[i] = set(data[i, :].flat)

for i in range(9):
    for j in range(9):
        ii = 3 * (i // 3)
        jj = 3 * (j // 3)
        subdata = data[ii:(ii + 3), jj:(jj + 3)]
        cond = set(subdata.flat)
        if data[i, j] == 0:
            maybe[i, j] = {1, 2, 3, 4, 5, 6, 7, 8, 9}.difference(vert_cond[i], gor_cond[j], cond)
        else:
            maybe[i, j] = {}

        rang[i, j] = int(len(maybe[i, j]))

print(maybe)
print(rang)
