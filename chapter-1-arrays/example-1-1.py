#!/usr/bin/python

def products(numbers):

    prefix_products = []

    for number in numbers:

        if prefix_products:
            prefix_products.append(prefix_products[-1] * number)
        else:
            prefix_products.append(number)

    suffix_products = []

    for number in reversed(numbers):
        if suffix_products:
            suffix_products.append(suffix_products[-1] * number)
        else:
            suffix_products.append(number)

    suffix_products = list(reversed(suffix_products))

    result = []
    for i in range(len(numbers)):
        if i == 0:
            result.append(suffix_products[i + 1])
        
        elif i == len(numbers) - 1:
            result.append(prefix_products[i - 1])
        
        else:
            result.append(prefix_products[i - 1] * suffix_products[i + 1])

    return result

if __name__ == "__main__":

    print products([3, 2, 1])
