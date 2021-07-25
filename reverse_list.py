#Title:Project-7b
def reverse_list(lon):
    """a function named reverse_list
    that takes as a parameter a list and and reverses
    the order of the elements in that list """
    for m in range(len(lon)//2):
        lon[m], lon[len(lon)-m-1] = lon[len(lon)-m-1], lon[m]


#vals = [7, -3, 12, 9]
#reverse_list(vals)
#print(vals)  # This should print [9, 12, -3, 7]