def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        counted_word = contents.split()
        counted_words = len(counted_word)
        print(f"{filename} contains {counted_words} words")
        for i in counted_word:
            print(i)
        print(f"Which are {i}: ")

answer = input("Enter filename to count words for: ")
count_words(answer)