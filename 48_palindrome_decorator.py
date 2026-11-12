def palindrome_decorator(func):
    def wrapper(num):
        is_pal = str(num) == str(num)[::-1]
        return f"{num} is a Palindrome" if is_pal else f"{num} is Not a Palindrome"
    return wrapper

@palindrome_decorator
def check_palindrome(num):
    return num

if __name__ == "__main__":
    print(check_palindrome(121))
    print(check_palindrome(1234))
