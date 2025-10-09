word = "Donkey"

with open("newfile.txt", "r") as f:
    content = f.read()
    
contentNew = content.replace(word, "######")

with open("newfile.txt", "w") as f:
    f.write(contentNew)