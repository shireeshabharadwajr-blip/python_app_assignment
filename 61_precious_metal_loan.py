def calculate_interest(metal, purity, amount, tenure):
    rates = {
        "gold": {18: 0.10, 22: 0.08, 24: 0.07},
        "silver": {925: 0.12, 950: 0.11, 999: 0.10},
        "platinum": {900: 0.09, 950: 0.08, 999: 0.07}
    }
    metal_lower = metal.lower()
    if metal_lower not in rates:
        raise ValueError(f"Invalid metal type: {metal}")
    if purity not in rates[metal_lower]:
        raise ValueError(f"Unsupported purity {purity} for {metal}")
        
    rate = rates[metal_lower][purity]
    return amount * rate * tenure

if __name__ == "__main__":
    test_calls = [
        lambda: calculate_interest(),
        lambda: calculate_interest("gold"),
        lambda: calculate_interest("gold", 22, 500000, 2),
        lambda: calculate_interest("diamond", 999, 100000, 2),
        lambda: calculate_interest("gold", 15, 100000, 2)
    ]
    for call in test_calls:
        try:
            res = call()
        except TypeError as te:
            print("Missing argument error:", te)
        except ValueError as ve:
            print("Validation error:", ve)
        else:
            print("Calculated Interest:", res)
        finally:
            print("---")
