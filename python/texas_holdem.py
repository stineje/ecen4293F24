import numpy as np

# Card ranks and suits
ranks = np.array(list('23456789TJQKA'))
suits = np.array(list('CDHS'))

# Create the deck of cards
deck = np.array([r + s for r in ranks for s in suits])

# Shuffle the deck
np.random.shuffle(deck)

# Deal two cards to each player
player1_hand = deck[:2]
player2_hand = deck[2:4]

# Deal the community cards (Flop, Turn, River)
community_cards = deck[4:9]


def get_card_value(card):
    """ Return the numerical value of the card rank. """
    return np.where(ranks == card[0])[0][0] + 2  # Rank is 2-14


def evaluate_hand(hand):
    """ Evaluate the best 5-card hand out of 7 cards. """
    # Generate all 5-card combinations
    from itertools import combinations
    all_combinations = np.array(list(combinations(hand, 5)))

    best_rank = 0
    for combination in all_combinations:
        values = np.array([get_card_value(card) for card in combination])
        suits = np.array([card[1] for card in combination])

        # Check for flush
        flush = len(np.unique(suits)) == 1
        # Check for straight
        straight = np.all(np.diff(np.sort(values)) == 1)
        # Check for same ranks
        counts = np.bincount(values)
        if flush and straight:
            rank = 9  # Straight flush
        elif 4 in counts:
            rank = 8  # Four of a kind
        elif 3 in counts and 2 in counts:
            rank = 7  # Full house
        elif flush:
            rank = 6  # Flush
        elif straight:
            rank = 5  # Straight
        elif 3 in counts:
            rank = 4  # Three of a kind
        elif list(counts).count(2) == 2:
            rank = 3  # Two pair
        elif 2 in counts:
            rank = 2  # One pair
        else:
            rank = 1  # High card

        if rank > best_rank:
            best_rank = rank

    return best_rank


# Combine each player's hand with the community cards
player1_full_hand = np.concatenate((player1_hand, community_cards))
player2_full_hand = np.concatenate((player2_hand, community_cards))

# Evaluate both hands
player1_rank = evaluate_hand(player1_full_hand)
player2_rank = evaluate_hand(player2_full_hand)

# Determine the winner
if player1_rank > player2_rank:
    winner = "Player 1"
elif player2_rank > player1_rank:
    winner = "Player 2"
else:
    winner = "It's a Tie!"

# Display results
print(f"Player 1 Hand: {player1_hand}")
print(f"Player 2 Hand: {player2_hand}")
print(f"Community Cards: {community_cards}")
print(f"Player 1 Hand Rank: {player1_rank}")
print(f"Player 2 Hand Rank: {player2_rank}")
print(f"Winner: {winner}")
