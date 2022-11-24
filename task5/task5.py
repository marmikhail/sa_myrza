import numpy as np
import json


def get_dif(matrix: np.matrix):
    diff = np.array(np.where(matrix == 0)).T
    upper_diff = np.array([d for d in diff if d[0] < d[1]]) + 1
    return upper_diff


def constr_mtx(levels: list, args: list[str]):
    size = len(args)
    mtx = np.zeros((size, size))
    passed = []

    for level in levels:
        if passed:
            left = np.delete(args, passed)
        else:
            left = args

        if type(level) is list:
            for elem in level:
                arg = int(elem) - 1
                for idx in left:
                    mtx[arg, int(idx) - 1] = 1
                passed.append(int(elem) - 1)
        else:
            elem = level
            arg = int(elem) - 1
            for idx in left:
                mtx[arg, int(idx) - 1] = 1
            passed.append(int(elem) - 1)

    return np.matrix(mtx)



def str_prs(s_data: str):
    levels = json.loads(s_data)
    args = sorted(
        np.hstack(levels),
        key=lambda e: int(e)
    )
    return levels, args


def dumps_result(array: np.array):
    return json.dumps([[str(elem) for elem in pair.tolist()] for pair in array])

def merge_mtx(matrix_1: np.matrix, matrix_2: np.matrix):
    return np.multiply(matrix_1, matrix_2) + np.multiply(matrix_1.T, matrix_2.T)


def task(string_1: str, string_2: str):
    lvls_1, arguments_1 = str_prs(string_1)
    lvls_2, arguments_2 = str_prs(string_2)

    matrix_1 = constr_mtx(lvls_1, arguments_1)
    matrix_2 = constr_mtx(lvls_2, arguments_2)

    merged_matrix = merge_mtx(matrix_1, matrix_2)

    dif = get_dif(merged_matrix)

    result = dumps_result(dif)

    return result


if __name__ == "__main__":
    range_1 = '["1", ["2","3"],"4", ["5", "6", "7"], "8", "9", "10"]'
    range_2 = '[["3","4"], ["1","2","5"], "7", "6", "9", ["8","10"]]'

    res = task(range_1, range_2)

    print(res)