def flower_box(nutrient_values):
    a, b = 0, 0
    for val in nutrient_values:
        a, b = b, max(a + val, b)
    return b


if __name__ == '__main__':
    print(f'flower_box([3, 10, 3, 1, 2]) = {flower_box([3, 10, 3, 1, 2])}')
    print(f'flower_box([9, 10, 9]) = {flower_box([9, 10, 9])}')
