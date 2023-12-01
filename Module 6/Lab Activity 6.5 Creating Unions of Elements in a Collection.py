def unite_lists(l1, l2):
    united_list = []
    for i1 in l1:
        if i1 not in united_list:
            united_list.append(i1)
    for i2 in l2:
        if i2 not in united_list:
            united_list.append(i2)
    return united_list
    

# Test your code here
if __name__ == '__main__':
    print(unite_lists([2,4,6,8],[3,6,9,12]))
