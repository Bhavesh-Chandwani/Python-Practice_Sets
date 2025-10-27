try:
    with open("notes.txt", "w+") as file:
        string = """I have leveled up in Python from basics to advance. I'm feeling good enough as I came far enough"""
        file.write(string)
        file.seek(0)           # move cursor to beginning
        content = file.read()
        print(content)
except Exception as e:
    print("Error:", e)

'''
"w+" is the file mode string passed to open(). Short summary:

Opens the file for both reading and writing.
Creates the file if it does not exist.
Truncates the file to zero length immediately (so any existing content is lost).
The file pointer starts at the beginning; after you write, the pointer is at the end — use seek(0) to read what you just wrote.
'''