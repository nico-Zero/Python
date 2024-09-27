import numpy as np
from random import randint


def generate_array(*shape: int, dim: int = 0, ran: int | tuple = ()) -> np.array:  # type: ignore
    def array(axes):
        if not shape or shape[axes] <= 0:
            raise ValueError("length must be grater then Zero!!!")
        elif len(shape) == axes + 1:
            if ran:
                if type(ran) == tuple:
                    return list(i for i in range(*ran))
                else:
                    return list(i for i in range(ran))  # type: ignore
            else:
                return list(randint(1, 100) for _ in range(shape[axes]))
        elif len(shape) > axes:
            return list(array(axes + 1) for _ in range(shape[axes]))

    if dim:
        shape = [dim for _ in range(dim)]  # type: ignore
        return np.array(array(0))
    elif ran:
        if type(ran) == int:
            shape = [ran for _ in range(ran)]  # type: ignore
        else:
            shape = [ran for _ in range(len(range(ran)))]  # type: ignore
        return np.array(array(0))
    else:
        return np.array(array(0))
