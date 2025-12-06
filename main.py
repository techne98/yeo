import argparse
import json
import shutil
from pathlib import Path


def create_config_file():
    # TODO: Possibly improve this to add an empty starting structure
    # to add config file paths.
    path = Path("castle.json")
    path.touch()


def copy_files():
    with open("castle.json", "r") as f:
        config_dict = json.load(f)

    config_files = config_dict["paths"]

    for file in config_files:
        src_file = Path.home() / file
        dest_file = Path.cwd() / Path(file)

        dest_file.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(src_file, dest_file)


def sync():
    pass


def main():
    parser = argparse.ArgumentParser(prog="castle")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("init", help="Create a castle.json file")
    subparsers.add_parser("sync", help="Sync your dotfiles to the current directory")

    args = parser.parse_args()

    if args.command == "init":
        create_config_file()
    elif args.command == "sync":
        copy_files()


if __name__ == "__main__":
    main()
