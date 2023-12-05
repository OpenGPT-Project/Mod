import json

def main():
    existing_data = load_from_json('words.json')

    while True:
        word = input("Enter a word (or type 'exit' to stop): ").strip().lower()

        if word == 'exit':
            break

        rating = get_rating()

        entry = {"word": word, "rating": rating}
        existing_data.append(entry)

    save_to_json(existing_data, 'words.json')
    print("Data saved to 'words.json'.")

def get_rating():
    while True:
        try:
            rating = int(input("Enter a rating from 0 to 10 on how offensive the word is: "))
            if 0 <= rating <= 10:
                return rating
            else:
                print("Please enter a valid rating between 0 and 10.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def load_from_json(filename):
    try:
        with open(filename, 'r') as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return []

def save_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=2)

if __name__ == "__main__":
    main()
