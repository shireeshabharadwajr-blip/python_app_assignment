class NumberIterator:
    def __init__(self, start=0.0, stop=1.0, step=0.25):
        self.current = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.stop + 1e-9:
            raise StopIteration
        val = round(self.current, 4)
        self.current += self.step
        return val

if __name__ == "__main__":
    for num in NumberIterator(0.0, 1.0, 0.25):
        print(num)
