# by:neverfriendme
def Credit_card_masker(card):
    if card[15] not in card:
        quit()
    elif card[15] in card:
        pass

    print("*" * 12 + card[12:16])





Credit_card_masker("1234567890123456")
