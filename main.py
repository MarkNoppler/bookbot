def main():
	book_path = "books/frankenstein.txt"
	text = get_book_text(book_path)
	total_words = word_count(text)
	print(f"Total words: {total_words}")
	character_counts = count_characters(text)
	print(f"Character Counts: {character_counts}")
	letters = [{char: count} for char, count in character_counts.items() if char.isalpha()]
	letters.sort(reverse=True, key=sort)
	print("--- Begin report of books/frankenstein.txt ---")
	print(f"{total_words} words found in the document\n")

	for letter_dict in letters:
		char, count = list(letter_dict.items())[0]
		print(f"The '{char}' character was found {count} times")
	print("--- End report ---")
	
def get_book_text(path):
	with open(path) as f:
		return f.read()
	
def word_count(words):
    total_words = words.split()
    return len(total_words)

def count_characters(text):
	lowered_string = text.lower()
	char_count = {}
	for char in lowered_string:
		if char in char_count:
			char_count[char] += 1
		else:
			char_count[char] = 1
	return char_count

def sort(dict):
	return list(dict.values())[0]

if __name__ == "__main__":
	main()