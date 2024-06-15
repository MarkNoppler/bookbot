def main():
	book_path = "books/frankenstein.txt"
	text = get_book_text(book_path)
	total_words = word_count(text)
	print(total_words)
	
def get_book_text(path):
	with open(path) as f:
		return f.read()
	
def word_count(words):
    total_words = words.split()
    return len(total_words)

main()