from pathlib import Path
path = Path('write-to-file.txt')
content = "I love programming and I will excel in it \n"
content += "I also love devops \n"
content += "I also love cloud \n"
path.write_text(content)