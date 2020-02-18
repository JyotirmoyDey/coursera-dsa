# python3


def max_pairwise_product(numbers):
    max_first = -1
    max_second = -1
    max_first_index = 0
    for i in range(len(numbers)):
        if numbers[i] > max_first:
            max_first = numbers[i]
            max_first_index = i
    numbers[max_first_index] = 0
    for i in range(len(numbers)):
        if numbers[i] > max_second:
            max_second = numbers[i]
    return max_first * max_second

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
