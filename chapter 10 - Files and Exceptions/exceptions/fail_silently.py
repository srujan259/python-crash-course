from pathlib import Path
def word_count(file_path):
    """ Count the number of words in the file """
    path = Path(file_path)
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

files_names = ['alice.txt', 'slimshady.txt', 'dummy.txt']
for file in files_names:
    word_count(file)