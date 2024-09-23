import numpy as np
import matplotlib.pyplot as plt

# Data for the table
hand_types = np.array([
    "Pocket Aces (AA)",
    "Pocket Aces (AA)",
    "Pocket Aces (AA)",
    "Pocket Kings (KK)",
    "Pocket Kings (KK)",
    "Pocket Kings (KK)",
    "Pocket Queens (QQ)",
    "Pocket Queens (QQ)",
    "Pocket Queens (QQ)",
    "Ace-King Suited (AKs)",
    "Ace-King Suited (AKs)",
    "Ace-King Suited (AKs)",
    "Pocket Tens (TT)",
    "Pocket Tens (TT)",
    "Pocket Tens (TT)",
    "Suited Connectors (e.g., 7♠-8♠)",
    "Suited Connectors (e.g., 7♠-8♠)",
    "Suited Connectors (e.g., 7♠-8♠)",
    "Small Pocket Pairs (e.g., 2-2)",
    "Small Pocket Pairs (e.g., 2-2)",
    "Small Pocket Pairs (e.g., 2-2)",
    "Flush Draw (after Flop)",
    "Flush Draw (after Flop)",
    "Open-Ended Straight Draw",
    "Open-Ended Straight Draw",
    "Inside Straight Draw",
    "Inside Straight Draw"
])

scenarios = np.array([
    "Heads-Up (2 players)",
    "Against 3 random hands",
    "Against 5 random hands",
    "Heads-Up (2 players)",
    "Against 3 random hands",
    "Against 5 random hands",
    "Heads-Up (2 players)",
    "Against 3 random hands",
    "Against 5 random hands",
    "Heads-Up (2 players)",
    "Against 3 random hands",
    "Against 5 random hands",
    "Heads-Up (2 players)",
    "Against 3 random hands",
    "Against 5 random hands",
    "Heads-Up (2 players)",
    "Against 3 random hands",
    "Against 5 random hands",
    "Heads-Up (2 players)",
    "Against 3 random hands",
    "Against 5 random hands",
    "Flop to Turn",
    "Flop to River",
    "Flop to Turn",
    "Flop to River",
    "Flop to Turn",
    "Flop to River"
])

probabilities = np.array([
    "~85%", "~63%", "~49%",
    "~82%", "~59%", "~47%",
    "~80%", "~57%", "~45%",
    "~66%", "~47%", "~33%",
    "~77%", "~54%", "~39%",
    "~38%-45%", "~27%-34%", "~20%-25%",
    "~49%-51%", "~36%-38%", "~27%-29%",
    "~19.6%", "~35%",
    "~17.4%", "~31.5%",
    "~8.5%", "~16.5%"
])

# Plot the table
plt.figure(figsize=(10, 8))
plt.axis('off')
table_data = np.column_stack((hand_types, scenarios, probabilities))
table = plt.table(cellText=table_data, colLabels=[
                  "Hand Type", "Scenario", "Winning Probability (%)"], cellLoc='center', loc='center')
table.auto_set_font_size(False)
table.set_fontsize(12)
table.scale(1.2, 1.2)

# Display the table
plt.show()
