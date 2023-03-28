lists = {
    ".append(val)": {
        'description': 'Adds the val to the end of the list.',
        'example': """lst = [1, 2]\nlst.append(3)\nprint(lst) = [1, 2, 3]"""
        },
    ".extend(iterable)": {
        'description': 'Adds all elements from the iterable to the end of the list.',
        'example': """lst = [1, 2]\nlst.extend([3, 4]\nprint(lst) = [1, 2, 3, 4])"""
        },
    ".insert(index, val)": {
        'description': 'Inserts the val into the list at the specified index.',
        'example': """lst = [1, 3]\nlst.insert(1, 2)\nprint(lst) = [1, 2, 3]"""
        },
    ".remove(val)": {
        'description': 'Removes the first occurance of val in the list. Raises ValueError if non-existent.',
        'example': """lst = [1, 2, 1]\nlst.remove(1)\nprint(lst) = [2, 1]"""
        },
    ".pop(index)": {
        'description': 'Index is optional. Removes the element at the index or from end of list if index is not given.',
        'example': """lst = [1, 2, 3]\nlst.pop()\nprint(lst) = [1, 2]\nlst.pop(0)\nprint(lst) = [2]"""
    },
    ".clear()": {
        'description': 'Removes all elements from the list.',
        'example': """lst = [1, 2, 3]\nlst.clear()\nprint(lst) = []"""
    },
    ".index(val, start, end)": {
        'description': 'Start(inclusive) and End(exclusive) are optional arguments to limit the search to a slice of the list. Returns the index of the first element equal to val. Raises a ValueError if element is non-existent.',
        'example': """lst = [1, 2, 4, 2, 3]\ni = lst.index(2)\nprint(i) = 1\nj = lst.index(2, 2, len(lst))\nprint(j) = 3"""
    },
    ".count(val)": {
        'description': 'Returns the number of times that val appears in the list.',
        'example': """lst = [1, 2, 1, 3]\nones = lst.count(1)\nprint(ones) = 2"""
    },
    ".sort(key=None, reverse=False)": {
        'description': 'Key and Reverse are optional keyword arguments. Sorts the elements in the list in place. All elements of the list must be of the same data type or sorting will not work properly.',
        'example': """lst = [AcA, aba, ABC]\nlst.sort()\nprint(lst) = [ABC, AcA, aba]\nlst.sort(key=str.lower)\nprint(lst) = [aba, ABC, AcA]\nlst = [1, 4, 2, 3]\nlst.sort(reverse=True)\nprint(lst) = [4, 3, 2, 1]"""
    },
    ".reverse()": {
        'description': 'Reverses the order of the elements in the list in place.',
        'example': """lst = [a, b, c, d]\nlst.reverse()\nprint(lst) = [d, c, b, a]"""
    },
    ".copy()": {
        'description': 'Returns a shallow copy of the list.',
        'example': """lst = [a, [b, [c]]]\ncopy = lst.copy()\nprint(copy) = [a, [b, [c]]]"""
    },
}

