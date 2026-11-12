def analyze_cards(cards):
    total = len(cards)
    aces = sum(1 for c in cards if c.startswith('A'))
    faces = sum(1 for c in cards if any(c.startswith(f) for f in ('J', 'Q', 'K')))
    reds = sum(1 for c in cards if c.endswith('H') or c.endswith('D'))
    blacks = sum(1 for c in cards if c.endswith('C') or c.endswith('S'))
    
    freq = {'Ace': aces, 'Face': faces, 'Red': reds}
    most_freq = max(freq, key=freq.get)
    
    return {
        'P(Ace)': round(aces / total, 3),
        'P(Face)': round(faces / total, 2),
        'P(Red)': round(reds / total, 2),
        'P(Black)': round(blacks / total, 2),
        'Most Frequent Category': most_freq
    }

if __name__ == "__main__":
    cards = ["AH", "10D", "KC", "QS", "2H", "JD", "7C", "KH"]
    print(analyze_cards(cards))
