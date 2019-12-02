

def merge(l1, l2):
    new = []
    while len(l1) and len(l2):
        if l1[0] < l2[0]:
            new.append(l1.pop(0))

        else:
            new.append(l2.pop(0))

    if len(l1):
        for item in l1:
            new.append(item)

    else:
        for item in l2:
            new.append(item)

    return new


def merge_sort(l):
    if len(l) == 1:
        return l

    middle = len(l) // 2

    l1 = merge_sort(l[:middle])
    l2 = merge_sort(l[middle:])

    return merge(l1, l2)


if __name__ == '__main__':
    unsorted = [3, 3123, 314, 4, 56, 675, 23]

    print(unsorted)
    print(merge_sort(unsorted))
