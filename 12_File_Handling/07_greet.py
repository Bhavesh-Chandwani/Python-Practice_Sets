import argparse
def main():
    parser = argparse.ArgumentParser(description="Greeting User:")
    parser.add_argument("name", help="First Name")
    parser.add_argument("--shout", action="store_true", help="Enable shout output")
    args = parser.parse_args()

    if args.shout:
        print(f"Hello, {args.name}".upper())
    else:
        print(f"Hello, {args.name}")

if __name__ == "__main__":
    main()