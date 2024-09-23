import numpy as np

# Define the total number of cards in a deck
total_cards = 52
# Define the number of hearts in a deck
hearts = 13
# Define the number of face cards (Jack, Queen, King) in each suit
face_cards_per_suit = 3
# Calculate the number of face cards that are hearts (since there are 3 face cards in the hearts suit)
face_hearts = face_cards_per_suit
# Calculate the total number of face cards in the deck
total_face_cards = face_cards_per_suit * \
    4  # 3 face cards in each of the 4 suits
# Calculate P(A | B) = P(A and B) / P(B)
# P(A and B): Probability that a card is a heart and a face card
p_A_and_B = face_hearts / total_cards
# P(B): Probability that a card is a face card
p_B = total_face_cards / total_cards
# Calculate the conditional probability P(A | B)
p_A_given_B = p_A_and_B / p_B
print(
    f"Prob of drawing a heart given that the card is a face card: {p_A_given_B:.8f}")
