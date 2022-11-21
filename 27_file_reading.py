f = open("testing_text_file.txt", "rt")
# rt -  means read in text mode also rb - read in binary mode
content = f.read()
# comment out 1st content to print below content
content = f.readline(3)
print(content)
# watch tutorial