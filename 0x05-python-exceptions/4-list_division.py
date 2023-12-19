def list_division(my_list_1, my_list_2, list_length):
    '''function that divides element by element 2 lists.
    Args:
        my_list_1(list): list 1
        my_list_2(list): list 2
        list_length(int): length of new list
    Return: new list
    '''
    try:
        list_3 = []
        list_length = min(len(my_list_1), len(my_list_2))
        for i in range(list_length):
            list_3.append(my_list_1[i] / my_list_2[i])
    except ZeroDivisionError:
        list_3.append(0)
        print("division by 0")
    except (TypeError, ValueError):
        print("wrong type")
    finally:
        if len(my_list_1) != len(my_list_2):
            print("out of range")
        return list_3
