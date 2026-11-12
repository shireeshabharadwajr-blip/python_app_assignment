def getvowels(name):
    vowels = "aeiouAEIOU"
    for char in name:
        if char in vowels:
            yield char

if __name__ == "__main__":
    for v in getvowels("Shireesha"):
        print(v)
