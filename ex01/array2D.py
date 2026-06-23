import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """A function that takes as parameters a 2D array,
        prints its shape, and returns a truncated
        version of the array based on the provided
        start and end arguments"""
    if (not isinstance(family, list) or not isinstance(start, int)
            or not isinstance(end, int)):
        raise TypeError("Arguments should be of type list or int")

    if len(family) == 0:
        print("My shape is : (0, 0)")
        print("My new shape is : (0, 0)")
        return []

    first_row_len = None
    for row in family:
        if not isinstance(row, list):
            raise TypeError("All elements inside the main list must be lists")
        if first_row_len is None:
            first_row_len = len(row)
        elif len(row) != first_row_len:
            raise ValueError("All rows in the 2D array must be the same size")

    np_arr = np.array(family)
    print(f"My shape is : {np_arr.shape}")

    truncated_arr = np_arr[start:end]
    print(f"My new shape is : {truncated_arr.shape}")

    return truncated_arr.tolist()
