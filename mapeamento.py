import os
import re

servidor = input("Local: ")
comp = []
number = None

# Walk and read file names
for (root, dirs, files) in os.walk(servidor, topdown=True):
    for file in files:
        path = root
        extension = str(file).split(".")[-1]
        try:
            client = str(root).split("\\")[5]
        except:
            client = None

        # If Windows system file, ignore
        if file.lower() == "thumbs.db":
            pass

        else:
            # Check if has contract number
            try:
                number = re.search(r'(((400)\w{5}))|(\d{7,})', file)[0]
            except:
                number = None
            # Compile results
            result = f"{number}|{client}|{file}|{extension}|{path}"
            comp.append(result)

        print(file)

# Write list to TXT file
with open('results.txt', 'w') as f:
    for item in comp:
        f.write("%s\n" % item)
