def calc_sum_difference(n):
    square_of_sums = sum(range(1, n + 1)) ** 2
    sum_of_squares = sum(map(lambda i: i * i, range(1, n + 1)))
    return square_of_sums - sum_of_squares
