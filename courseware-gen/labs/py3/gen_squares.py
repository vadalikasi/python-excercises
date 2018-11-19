def res_generators(max_value):
    value = 0
    while value < max_value:
        yield value * value
        value += 1


def squares(max_value):
    res = []
    for i in range(max_value):
        res.append(i ** 2)
    return res


if __name__ == '__main__':
    gen = res_generators(10)
    for res in gen:
        print("Square is : {}".format(res))
