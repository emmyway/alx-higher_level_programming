def safe_print_division(a, b):
    """fxn divides two integers and print result
    Args:
        a(int): first int value
        b(int): second int value
    Return:
        the result or none if failed
    """
    try:
        c = a / b
    except ZeroDivisionError:
        c = 0
    finally:
        if c == 0:
            print("Inside result:None")
            return None
        else:
            print("Inside result:{}".format(c))
            return c
