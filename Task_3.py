def treemap(func, lst):
    for i in range(len(lst)):
        if type(lst[i]) == int:
            return func(lst[i])
        else:
            return treemap(func, lst[i])


print(treemap(lambda x: x*x, [[[1], [2, 3], 4], [5, 6], 7]))