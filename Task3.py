def treemap(func, lst):
    print(len(lst))
    for i in range(len(lst)):
        print('i=', i)
        print('lst[i]=', lst[i])
        if type(lst[i]) == int:
            print('int', lst[i])
            return func(lst[i])
        else:
            print('ret',lst[i])
            return treemap(func, lst[i])


print(treemap(lambda x: x*x, [[[1], [2, 3], 4], [5, 6], 7]))