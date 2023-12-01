class Package:
    def __init__(self, items):
        if items > 6:
            excess_items = items - 6
            print(f"The maximum item limit has been exceeded. {excess_items} items must be removed from the package.")
        else:
            print(f"There are {items} items in the package being shipped out.")
            


# This is to test your code
if __name__ == '__main__':
    morepackages = True
    while morepackages:
        items = int(input("How many items are in the package?: "))
        package = Package(items)
        yn = input('Ship more packages? Y/N ')
        morepackages = yn == 'y' or yn == 'Y'

