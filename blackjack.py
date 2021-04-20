from typing import List
from itertools import product
from random import shuffle
from time import sleep

deck = []
player_hand : List[str] = []
dealer_hand = []
players = [player_hand, dealer_hand]

def generate_deck(deck: List[str]) -> None:
    deck.clear()
    ranks = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')
    suits = range(0, 3)
    for p in product(ranks, suits):
        deck.append(p)
    shuffle(deck)
    # print(deck)


def deal_card(hand: List[str]) -> None:
    hand.append(deck.pop())


def display_hand(hand: List[int]) -> None:
    print(f"{evaluate_hand(hand):2}", end="   ")
    for card in hand:
        # chr(9824) to chr(9831) are card suits symbols
        print(f"{card[0]}{chr(card[1]+9828)}", end=" ")
    print()


def print_scores(players: List[List[str]], play: bool) -> None:
    print("Player:", end =" ")
    display_hand(players[0])
    
    print("Dealer:", end=" ")
    if play:
        display_hand([players[1][0]])
    else:
        display_hand(players[1])


def evaluate_hand(player_hand: List[str]) -> int:
    aces = 0
    total = 0
    for card in player_hand:
        if card[0] == 'A':
            aces += 1
            total += 11
        elif card[0] > '9':
            total += 10
        else:
            total += int(card[0])

    while aces and total > 21:
        total -= 10
        aces -= 1

    return total


def game():
    # create a shuffled deck
    generate_deck(deck)

    # TODO remove below after testing
    print("Cards in the deck: ")
    for card in deck:
        print(f"{card[0]}{chr(card[1]+9828)}", end=" ")
    print()
    # TODO remove above after testing

    play = True

    # deal 2 cards for both the player and the dealer
    # but keep the dealer's second card face down
    for hand in players:
        for _ in range(2):
            deal_card(hand)
    print_scores(players, True)

    if evaluate_hand(player_hand) == 21:
        if dealer_hand == 21:
            print("IT'S A TIE!")
        else:
            print("BLACKJACK!!!")
            # TODO: reveal dealer's other card
    
    while play:
        print("*" * 25)
        choice = input("H for hit, S for stand: ").lower()
        if choice not in ("h", "s"):
            print("I didn't get you...")
            continue
        if choice == "h":
            sleep(1)
            deal_card(player_hand)
            player_score = evaluate_hand(player_hand)
            print_scores(players, True)
            if player_score > 21:
                print("You bust! Dealer wins.")
                play = False
            elif player_score == 21:
                choice = "s"
                play = False
            else:
                continue
        if choice == "s":
            print("*" * 25)
            print_scores(players, False)
            sleep(1)

            dealer_score = evaluate_hand(dealer_hand)
            player_score = evaluate_hand(player_hand)

            # TODO check if dealer needs to hit if above player_score but below 17
            while dealer_score < 17 and dealer_score <= player_score:
                sleep(1)
                deal_card(dealer_hand)
                dealer_score = evaluate_hand(dealer_hand)
                print("*" * 25)
                print_scores(players, False)
            if player_score > dealer_score:
                print("Well done! You won!!!")
            elif player_score < dealer_score:
                if dealer_score <= 21:
                    print("Dealer wins!")
                else:
                    print("Dealer bust. You won!")
            else:
                print("It's a tie!")
            # TODO consider deleting this printout
            # print()
            # print_scores(players, False)
            play = False


if __name__ == '__main__':
    game()

    # TODO remove after testing
    print("\nCards left in the deck:")
    for card in deck:
        print(f"{card[0]}{chr(card[1]+9828)}", end=" ")
    print()
