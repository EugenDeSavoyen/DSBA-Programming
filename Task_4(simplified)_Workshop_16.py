def nest_dict(dic):
    nested_dict = {}
    for i in range(len(dic)):
        lst = dic.popitem()
        if str(lst[0]).find('.') == -1:
            nested_dict[lst[0]] = lst[1]
            print('one layer', lst[0], lst[1])
        else:
            if lst[0][0] not in nested_dict:
                nested_dict[lst[0][0]] = {}
                print('layer added', nested_dict)
            nested_dict[lst[0][0]][lst[0][2]] = lst[1]
            print('second layer', lst[0][0], lst[1])
    return nested_dict


dc = {'a': 1, 'b.x': 2, 'b.y': 3}
print(nest_dict(dc))
