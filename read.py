

def read_file():    # Function is defined with name : 'read_file'
    file = open("products.txt", "r")    # open stock file (products.txt) in read mode.
    lines = file.readlines()
    L = []  # assign empty list with name 'L'
    for line in lines:
        L.append(line.replace("\n", "").split(","))
    file.close()
    print("Following products are avilable in our Store")
    print("--------------------------------------------")
    print("PRODUCT\t\tPRICE\t\tQUANTITY")
    print("--------------------------------------------")
    for i in range(len(L)):
        print(L[i][0], "\t\t", L[i][1], "\t\t", L[i][2])    # prints the available product, price and quantity
    print("--------------------------------------------")
    return L
