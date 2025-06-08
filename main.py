import random

def card_value(card):
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 11
    else:
        return int(card)

def deal_card():
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return random.choice(cards)

def calculate_score(hand):
    total = sum(card_value(c) for c in hand)
    aces = hand.count('A')

    # Adjust Aces if total exceeds 21
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

def show_hand(hand, who="Player"):
    print(f"{who} has: {', '.join(hand)} (Total: {calculate_score(hand)})")

def play():
    print("Welcome to 21 card game!")
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

    show_hand(player_hand)

    while True:
        if calculate_score(player_hand) == 21:
            print("You have 21! Dealer's turn.")
            break
        elif calculate_score(player_hand) > 21:
            print("You busted! You lose.")
            return

        decision = input("Do you want another card? (y/n): ").strip().lower()
        if decision == 'y':
            player_hand.append(deal_card())
            show_hand(player_hand)
        elif decision == 'n':
            break
        else:
            print("Please enter 'y' or 'n'.")

    print("\nDealer's turn...")
    show_hand(dealer_hand, "Dealer")

    while calculate_score(dealer_hand) < 17:
        dealer_hand.append(deal_card())
        show_hand(dealer_hand, "Dealer")

    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    print("\nFinal result:")
    show_hand(player_hand, "Player")
    show_hand(dealer_hand, "Dealer")

    if dealer_score > 21 or player_score > dealer_score:
        print("You win!")
    elif player_score < dealer_score:
        print("You lose.")
    else:
        print("Tie.")

def main():
    play()  

if __name__ == '__main__':
    main()