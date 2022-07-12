def get_dpa(number):

    def get_classification(num):
        proper_divisors = [num / (i + 2) for i in range(num - 1) if (num / (i + 2)).is_integer()]
        if sum(proper_divisors) < num:
            return 'deficient'
        elif sum(proper_divisors) == num:
            return 'perfect'
        else:
            return 'abundant'

    results = {'deficient': 0, 'perfect': 0, 'abundant': 0}
    for x in range(number):
        result = get_classification(x + 1)
        results[result] += 1
    return [x for x in results.values()]


print(get_dpa(20000))
