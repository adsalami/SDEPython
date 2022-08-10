#!/usr/bin/env python3

def main():
    # create a list of favorite foods called listA
    listA = ["cheese_burger", "big_mac", "fish_peppersoup"]

     # display listA
    print(listA)
 # display listA[1] which should only display big_mac
    print(listA[1])

     # create a new list containing a single item
    listB= ["fried_rice"]

    # extend listA by listB (combine both lists together into a single list)
    listA.append(listB)

    # display listA, which now contains fried_rice
    print(listA)

# create listC
    listC = ["dodo", "jollof", "ogunfe"]

    # use the append operation to append list1 by listC
    listA.append(listC)

    # display the new complex listA
    print(listA)

    # my favorite food is
    print(listA[3])


main()
