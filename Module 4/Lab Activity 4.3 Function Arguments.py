def skip_integers(*args):
    for a in args:
        if type(a) == int:
            continue
        else:
            pass
            print(a)

# Test you code here
skip_integers(3, 5.2, "value", 6.0)
