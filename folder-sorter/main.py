from core import folder_sorter
import argparse


def main():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("folder_path", nargs="?", default="D:\Training", help="Path to the folder you want to sort.")
    parser.add_argument("dry_run", nargs="?", default=True, help="Move or simulate moving files.")
 
    args = parser.parse_args()
    folder_sorter(folder_path=args.folder_path, dry_run=args.dry_run)

if __name__ == "__main__":
    main()