def main():
	book_path = "books/frankenstein.txt"
	text = get_book_text(book_path)
	total_words = word_count(text)
	print(f"Total words: {total_words}")
	character_counts = count_characters(text)
	print(f"Character Counts: {character_counts}")
	
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



main()