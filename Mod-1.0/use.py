import json
import re

def load_offensive_words(filename):
    try:
        with open(filename, 'r') as json_file:
            data = json.load(json_file)
            return [entry["word"] for entry in data]
    except FileNotFoundError:
        print(f"File '{filename}' not found. Please run the previous script to collect offensive words.")
        return []

def is_sentence_offensive(sentence, offensive_words):
    sentence_lower = sentence.lower()

    for word in offensive_words:
        if re.search(re.escape(word), sentence_lower):
            return True

    return False

def main():
    offensive_words = load_offensive_words('words.json')

    if not offensive_words:
        return

    while True:
        sentence = input("Enter a sentence (or type 'exit' to stop): ").strip().lower()

        if sentence == 'exit':
            break

        if is_sentence_offensive(sentence, offensive_words):
            print("Warning: This sentence contains offensive words.")
        else:
            print("This sentence is clean.")

if __name__ == "__main__":
    main()
