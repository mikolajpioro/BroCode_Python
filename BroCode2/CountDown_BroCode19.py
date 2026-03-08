cardValues = ["10H", "JH", "QH", "KH", "AH", "2S"]
finished = []

for card in cardValues:
    if card[0].isdigit():
        if card[0] == '1' and card[1] == '0':
            finished.append('10')
        else:
            finished.append(card[0])
    elif card[0].isalpha():
        if card[0] == 'A':
            finished.append('1')
        else:
            finished.append('10')

print(finished)
