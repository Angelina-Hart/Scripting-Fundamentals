def content_combiner(dict1, dict2):
    dict1.update(dict2)
    return dict1

# Test your function using the code below
if __name__ == '__main__':
    print(content_combiner({"gold": "Yellow"}, {"karats": 24}))
