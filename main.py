def main():
  book_path = "books/frankenstein.txt"
  book_name = book_path.split("/")[-1].split(".")[0]
  text = get_text(book_path)
  word_count = get_num_words(text)
  char_count = get_char_count(text)
  sorted_char_count = sort_char_count(char_count)
  print("-------------------------")
  print(f"Book statistics for '{book_name}':")
  print("\n")
  print(f"Word count: {word_count}")
  print("\n")
  print("Character count:")
  for char, count in sorted_char_count.items():
    print(f"'{char}' character was found: {count} times")
  print("\n")
  print("End of statistics. Thank you!")
  print("-------------------------")

def get_text(book_path):
  return open(book_path).read()

def get_num_words(text):
  return len(text.split())

def get_char_count(text):
  char_count = {}
  lowered = text.lower()
  for char in lowered:
    if char.isalpha():
      if char in char_count:
        char_count[char] += 1
      else:
        char_count[char] = 1
  return char_count

def sort_char_count(char_count):
  def sort_key(item):
    return item[1]
  sorted_items = sorted(char_count.items(), key=sort_key, reverse=True)
  sorted_dict = dict(sorted_items)
  return sorted_dict

if __name__ == "__main__":
  main()