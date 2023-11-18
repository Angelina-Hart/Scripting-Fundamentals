for i in range(10, 100):
    if i == 0:
        pass
    elif i % 5 != 0:
        continue
    elif type(i) != int:
        continue
    elif i == 95:
        break
    else:
        pass
        print(i)
