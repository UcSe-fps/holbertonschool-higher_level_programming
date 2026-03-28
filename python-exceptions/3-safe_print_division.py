#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        idk = a / b
    except (ZeroDivisionError):
        idk = None
    finally:
        print("Inside result: {}".format(idk))
        return idk
