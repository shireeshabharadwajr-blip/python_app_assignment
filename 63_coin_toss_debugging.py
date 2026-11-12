import random

def coin_toss_game():
    # Uncomment the line below to trigger VS Code / pdb debugger breakpoint:
    # breakpoint()
    guess = input("Predict toss (heads/tails): ").strip().lower()
    toss = random.choice(["heads", "tails"])
    result = (guess == toss)
    print(f"Toss was {toss}. You win: {result}")

if __name__ == "__main__":
    coin_toss_game()
