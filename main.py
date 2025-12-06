import argparse
from pathlib import Path


def create_config_file():
    path = Path("castle.json")
    path.touch()


def copy_files():
    pass


def sync():
    pass


def main():
    parser = argparse.ArgumentParser(prog="castle")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("init", help="Create a castle.json file")

    args = parser.parse_args()

    if args.command == "init":
        create_config_file()


if __name__ == "__main__":
    main()
