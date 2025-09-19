import argparse

from generators import MemorablePassword, PinPassword, RandomPassword


def main():
    parser = argparse.ArgumentParser(description="Password Generator")
    subparsers = parser.add_subparsers(dest="mode", required=True, help="Type of password")

    # Subparser for PIN
    pin_parser = subparsers.add_parser("pin", help="Generate numeric PIN password")
    pin_parser.add_argument("--length", type=int, default=8, help="Length of PIN (min 1)")

    # Subparser for Random
    random_parser = subparsers.add_parser("random", help="Generate random password")
    random_parser.add_argument("--length", type=int, default=8, help="Length of password (min 1)")
    random_parser.add_argument("--no-numbers", action="store_true", help="Exclude numbers")
    random_parser.add_argument("--no-symbols", action="store_true", help="Exclude symbols")

    # Subparser for Memorable
    memorable_parser = subparsers.add_parser("memorable", help="Generate memorable (word-based) password")
    memorable_parser.add_argument("--words", type=int, default=4, help="Number of words (min 1)")
    memorable_parser.add_argument("--separator", default="-", help="Separator between words")
    memorable_parser.add_argument("--no-capitalize", action="store_true", help="Disable capitalization")

    args = parser.parse_args()

    # Validation for lengths
    if args.mode == "pin" and args.length < 1:
        parser.error("PIN length must be at least 1")
    if args.mode == "random" and args.length < 1:
        parser.error("Password length must be at least 1")
    if args.mode == "memorable" and args.words < 1:
        parser.error("Number of words must be at least 1")

    # Choose generator
    if args.mode == "pin":
        generator = PinPassword(length=args.length)
    elif args.mode == "random":
        generator = RandomPassword(
            length=args.length,
            numbers=not args.no_numbers,
            symbols=not args.no_symbols
        )
    elif args.mode == "memorable":
        generator = MemorablePassword(
            word_count=args.words,
            separator=args.separator,
            capitalization=not args.no_capitalize
        )
    else:
        parser.error("Unknown mode selected")

    print(generator.generate())


if __name__ == "__main__":
    main()
