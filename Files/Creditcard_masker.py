# by:neverfriendme
def Credit_card_masker(card):
    try:
        print("*" * 12 + card[12:16])
        Credit_card_masker("1234567890123457")
    except IndexError:
        print("Invalid")
