li = [1, 2, 3, 4]


def change_list(li):
    li.append(5)  # this will change the original list itself
    return li


def change_list_2(li):
    li = [1, 2, 3]  # this will not change the original list
    return li


new_li = change_list_2(li)
print(li)
print(new_li)
