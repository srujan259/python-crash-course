from pathlib import Path
def count_words(filepath, word):
    path = Path(filepath)
    try:
        contents = path.read_text(encoding='utf-8')
    except:
        pass
    else:
        no = contents.lower().count(word)
        print(f" The word '{word}' apprears {no} of times in the story")

count_words('alice.txt', 'the ')