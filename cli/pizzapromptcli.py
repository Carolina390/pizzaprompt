import argparse

def main():
    parser = argparse.ArgumentParser(description="A simple CLI example.")
    parser.add_argument("name", help="Your name")
    parser.add_argument("-g", "--greeting", default="Hello", help="Greeting message")
    args = parser.parse_args()
    print(f"{args.greeting}, {args.name}!")

if __name__ == "__main__":
    main()