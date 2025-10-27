try:
    with open("tasks.txt", "w") as file:
        string ="""The task is to write the task.\n
Then append the task\n
Then read the file and print the line as list using  readlines()."""

        file.write(string)
    
    with open("tasks.txt", "a+") as file:
        string = """\nTasks Completed"""
        file.write(string)
        file.seek(0)
        content = [line.strip() for line in file.readlines()]
        print(content)

except FileNotFoundError:
    print(f"File {file} not found")        