import os
from collections import Counter
import re
import socket

def count_words(file_path):
    """Counts total words in a text file."""
    with open(file_path, 'r') as file:
        text = file.read()
        words = text.split()
        return len(words), words

def most_frequent_words(words, n=3):
    """Finds the most frequent words in a list."""
    return Counter(words).most_common(n)

def handle_contractions(words):
    """Handles contractions by splitting them into individual words."""
    new_words = []
    for word in words:
        # Split contractions
        split_words = re.findall(r"\b\w+(?:'\w+)?|\w+\b", word)
        new_words.extend(split_words)
    return new_words

def main():
    # Paths to the text files
    if_file_path = 'IF.txt'
    always_file_path = 'AlwaysRememberUsThisWay.txt'

    # Count words in IF.txt
    total_words_if, words_if = count_words(if_file_path)
    
    # Count words in AlwaysRememberUsThisWay.txt
    total_words_always, words_always = count_words(always_file_path)

    # Calculate grand total
    grand_total = total_words_if + total_words_always

    # Find top 3 most frequent words in IF.txt
    top_words_if = most_frequent_words(words_if)

    # Handle contractions in AlwaysRememberUsThisWay.txt
    split_words_always = handle_contractions(words_always)
    top_words_always = most_frequent_words(split_words_always)

    # Get IP address of the container
    ip_address = socket.gethostbyname(socket.gethostname())

    # Prepare results for output
    results = (
        f"Total words in IF.txt: {total_words_if}\n"
        f"Total words in AlwaysRememberUsThisWay.txt: {total_words_always}\n"
        f"Grand total words: {grand_total}\n"
        f"Top 3 words in IF.txt: {top_words_if}\n"
        f"Top 3 words in AlwaysRememberUsThisWay.txt: {top_words_always}\n"
        f"IP Address of container: {ip_address}\n"
    )

    # Write results to output file
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)
    output_file_path = os.path.join(output_dir, 'result.txt')
    
    with open(output_file_path, 'w') as output_file:
        output_file.write(results)

    # Print results to console
    print(results)

if __name__ == "__main__":
    main()
