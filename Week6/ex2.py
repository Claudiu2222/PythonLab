import os
import sys


def main():
    try:
        if len(sys.argv) != 2:
            raise ValueError("Please provide exactly one argument: a dir_path")
        dir_path = sys.argv[1]
        if not os.path.isdir(dir_path):
            raise NotADirectoryError(dir_path)
        for index, file in enumerate(os.listdir(dir_path)):
            try:
                if not os.path.isfile(os.path.join(dir_path, file)):
                    continue
                os.rename(
                    os.path.join(dir_path, file),
                    os.path.join(dir_path, f"{index + 1}_{file}"),
                )
            except Exception as e:
                print(f"Error renaming file {file}: {e}")
    except NotADirectoryError as nade:
        print(f"Directory {nade} does not exist or is not a directory")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
