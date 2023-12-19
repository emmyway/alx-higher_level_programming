def safe_print_list_integers(my_list=[], x=0):
    """prints elements of list that are integers
        Args:
            mylist(list): the list to print from
            x(int,strings): the elements in list
        Return:
            number of elements printed
    """

    count = 0

    try:

        for i in range(x):
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                count += 1
    except IndexError: 
        pass
    finally:
        print()
        return (count)
