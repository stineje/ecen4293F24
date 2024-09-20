
def read_words_from_file(file_path):
    """
    read words from a file using a try block
    """
    words = []
    try:
        with open(file_path, 'r') as file:
            # Read each line in the file
            for line in file:
                # Split the line into words and extend the list
                words.extend(line.split())
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except IOError:
        print(
            f"Error: An I/O error occurred while reading the file '{file_path}'.")
    return words


def count_words(words, n=None):
    """
      Lets count words of dictionary by iterating over entire file
    """
    word_count = {}
    # Iterate over each word in the list
    for word in words[:n]:
        # Remove punctuation from the word
        word = ''.join(char for char in word if char.isalnum())
        # Count the word occurrences
        if word:  # Check if word is not empty
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    return word_count


# https://www.govinfo.gov/content/pkg/CDOC-110hdoc50/html/CDOC-110hdoc50.htm
file_path = 't8.shakespeare.txt'
words = read_words_from_file(file_path)
result = count_words(words)
# sort dictionary
sorted_dict = sorted(result.items(), key=lambda item: item[1], reverse=True)

# Print the top 25 results with formatted numbers
formatted_output = ', '.join(
    f"({key}, {value:,})" for key, value in sorted_dict[0:25])
print(formatted_output)
