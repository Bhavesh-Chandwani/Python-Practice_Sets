import argparse
def main():
    parser = argparse.ArgumentParser(description="Counting the appearance of word in a file.")
    parser.add_argument("filename", help="Name the file we want the count the same word.")
    parser.add_argument("word", help="The word we want to count.")

    args = parser.parse_args()

    try:
        with open(args.filename, "r") as file:
            content = file.read()
            count = content.lower().count(args.word.lower())
            print(f"The word {args.word} appeared : {count} times")
    except FileNotFoundError:
        print(f"File {args.filename} not found")

if __name__ == "__main__":
    main()