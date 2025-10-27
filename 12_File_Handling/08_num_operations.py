import argparse
def main():
    parser = argparse.ArgumentParser(description= "Performing Basic Operations on Numbers")
    parser.add_argument("num_1", type= int, help= "First_Number")
    parser.add_argument("num_2", type= int, help= "Second_Number")
    parser.add_argument("--multiply", action= "store_true", help= "Enable Multiplication Output")

    args = parser.parse_args()

    if args.multiply:
        print(f"Product : {args.num_1*args.num_2}")
    else:
        print(f"Sum : {args.num_1 + args.num_2}")

if __name__ == "__main__":
    main()