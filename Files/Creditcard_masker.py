# by:neverfriendme
def Credit_card_masker(card):
    try:
        print("*" * 12 + card[12:16])
    except IndexError:
        print("Invalid")
