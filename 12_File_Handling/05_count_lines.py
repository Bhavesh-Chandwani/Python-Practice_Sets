import argparse
def main():
    parser = argparse.ArgumentParser(description="Counting the number of line present in File.")
    parser.add_argument("filename", help="Name of the file we want to count the lines")
    parser.add_argument("--lines", action="store_true", help="Print the number of lines present in file")

    args = parser.parse_args()

    try:
        with open(args.filename, "r") as file:
            if args.lines:
                lines = file.readlines()
                print(f"The number of lines present in file : {len(lines)}")
            
            else:
                content = file.read()
                print(f"The content of the file\n : {content}")
    
    except FileNotFoundError:
        print(f"The file {args.filename} not found.")

if __name__ == "__main__":
    main()