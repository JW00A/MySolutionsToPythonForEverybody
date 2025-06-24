new_list = [1, 2, 3, 4, 5, 6, 7]

print('List before: ', new_list)

def chop(list):
    del list[0]
    del list[len(list) - 1]
    return None

chop(new_list)
print('List after: ', new_list)

def middle(list):
    return list[1:len(list) - 1]

print('List from a function: ', middle(new_list))
print('List after: ', new_list)