from time import time


def main():
    gen_list_of_dict(int(input("Enter an integer number: ")))


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        func(*args, **kwargs)
        finish_time = time()
        print(f"The function has been completed {finish_time - start_time} seconds")
    return wrapper


@time_decorator
def gen_list_of_dict(n):
    my_list = []
    for v in range(n):
        my_dict = {v: v ** 2 for v in range(v + 1)}
        my_list.append(my_dict)
    print(my_list)


if __name__ == "__main__":
    main()

print('='*100)
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list_3 = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

# leave even numbers from the  list_1 and list_3
even1 = list(filter(lambda x: x % 2 == 0, list_1))
print('1:', even1)
even2 = list(filter(lambda x: x % 2 == 0, list_3))
print('1:', even2)

# leave odd numbers from the list_2
odd = list(filter(lambda x: not x % 2 == 0, list_2))
print('2:', odd)

# combining lists to the tuple of tuples
result = tuple(zip(list_1, list_2, list_3))
print('3:', result)

# total sum for each tuple
sum_ = tuple(map(sum, result))
print('4:', sum_)

# leave only odd numbers
a = tuple(filter(lambda x: not x % 2 == 0, sum_))
print('5:', a)
