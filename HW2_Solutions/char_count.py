alma_mater = "Proud and immortal Bright shines your name Oklahoma State We herald your fame Ever you'll find us Loyal and true To our Alma Mater (O-S-U)."

char_count = {}
for char in alma_mater:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1


char_count_sorted = sorted(char_count.items(),
                           key=lambda key_value: key_value[1],
                           reverse=True)
# Print out 5 top letters
print(char_count_sorted[0:5])
