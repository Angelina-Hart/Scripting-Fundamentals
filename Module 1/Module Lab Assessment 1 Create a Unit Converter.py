def convert_kg(value):
    kglb = value * 2.20462
    kgoz = value * 35.274
    print(f"{value} kg converted is {kglb} pounds and {kgoz} ounces.")

def convert_pounds(value):
    lbkg = value * 0.453592
    lboz = value * 16
    print(f"{value} pounds converted is {lbkg} kg and {lboz} ounces.")

def convert_ounces(value):
    ozkg = value * 0.0283
    ozlb = value * 0.0625
    print(f"{value} ounces converted is {ozkg} kg and {ozlb} pounds.")


# 1 fluid ounce is equal to:
# 0.029573 liters
# 0.0625 pints
# 0.03125 quarts
def convert_flounces(value):
    folt = value * 0.029573
    fopt = value * 0.0625
    foqt = value * 0.03125
    if value == 1:
        print(f"{value} fluid ounce converted is {folt} liters, {fopt} pints, and {foqt} quarts.")
    elif value < 0:
        print("Invalid input.")
    else:
        print(f"{value} fluid ounces converted is {folt} liters, {fopt} pints, and {foqt} quarts.")


# 1 liter is equal to:
# 33.814022 fluid ounces
# 2.113376 pints
# 1.056688 quarts
def convert_liters(value):
    ltfo = value * 33.814022
    ltpt = value * 2.113376
    ltqt = value * 1.056688
    if value == 1:
        print(f"{value} liter converted is {ltfo} fluid ounces, {ltpt} pints, and {ltqt} quarts.")
    elif value < 0:
        print("Invalid input.")
    else:
        print(f"{value} liters converted is {ltfo} fluid ounces, {ltpt} pints, and {ltqt} quarts.")


# 1 pint is equal to:
# 16 fluid ounces
# 0.473176 liters
# 0.5 quarts
def convert_pints(value):
    ptfo = value * 16
    ptlt = value * 0.473176
    ptqt = value * 0.5
    if value == 1:
        print(f"{value} pint converted is {ptfo} fluid ounces, {ptlt} liters, and {ptqt} quarts.")
    elif value < 0:
        print("Invalid input.")
    else:
        print(f"{value} pints converted is {ptfo} fluid ounces, {ptlt} liters, and {ptqt} quarts.")


# 1 quart is equal to:
# 32 fluid ounces
# 0.946352 liters
# 2 pints
def convert_quarts(value):
    qtfo = value * 32
    qtlt = value * 0.946352
    qtpt = value * 2
    if value == 1:
        print(f"{value} quart converted is {qtfo} fluid ounces, {qtlt} liters, and {qtpt} pints.")
    elif value < 0:
        print("Invalid input.")
    else:
        print(f"{value} quarts converted is {qtfo} fluid ounces, {qtlt} liters, and {qtpt} pints.")


if __name__ == "__main__":
    convert_kg(10)
    convert_pounds(10)
    convert_ounces(10)
    convert_flounces(60)
    convert_liters(20)
    convert_pints(10)
    convert_quarts(5)
