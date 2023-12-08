with open("input.txt", "r") as f:
    file = f.read().strip().splitlines()

hands = {
    "Five of a kind":[],
    "Four of a kind":[],
    "Full house":[],
    "Three of a kind":[],
    "Two pair":[],
    "One pair":[],
    "High card":[]
}
values = {
    "A":"E",
    "K":"D",
    "Q":"C",
    "J":"",
    "T":"A"
}

for i in file:
    hand = i.split()

    jokers = hand[0].count("J")
    hand[0] = [values.get(card, card) for card in hand[0]]
    unique_cards = len(set("".join(hand[0]))) or 1
    
    if unique_cards == 1:
        hands["Five of a kind"].append(hand)
        continue

    if unique_cards == 4:
        hands["One pair"].append(hand)
        continue 

    if unique_cards == 5:
        hands["High card"].append(hand)
        continue 

    num_of_duplicates = (hand[0].count(i) for i in hand[0])
    if unique_cards == 3:
        if 3 - jokers in num_of_duplicates:
            hands["Three of a kind"].append(hand)
            continue 
        else:
            hands["Two pair"].append(hand)
            continue             

    # this if statement isnt needed but is added for clarity 
    if unique_cards == 2:
        if 4 - jokers in num_of_duplicates:
            hands["Four of a kind"].append(hand)
            continue 
        else:
            hands["Full house"].append(hand)
            continue

num = 0
ordered = []
for key in hands:
    ordered.extend(sorted(hands[key], reverse=True))

for i, v in enumerate(reversed(ordered)):
    num += int(v[1]) * (i + 1)

print(num)
