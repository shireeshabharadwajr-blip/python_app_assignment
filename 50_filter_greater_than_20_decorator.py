def filter_decorator(func):
    def wrapper(nums):
        return list(filter(lambda x: x <= 20, func(nums)))
    return wrapper

@filter_decorator
def get_numbers(nums):
    return nums

if __name__ == "__main__":
    print("Filtered List:", get_numbers([5, 10, 23, 40, 8]))
