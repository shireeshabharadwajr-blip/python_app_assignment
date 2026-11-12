def cumulative_average_generator():
    nums = []
    def add_number(num):
        nums.append(num)
        return sum(nums) / len(nums)
    return add_number

if __name__ == "__main__":
    avg_tracker = cumulative_average_generator()
    for val in [10, 20, 30, 40]:
        print(f"After entering {val} -> Cumulative Average: {avg_tracker(val)}")
