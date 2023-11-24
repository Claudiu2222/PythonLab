import sys
import os


def main():
    try:
        if len(sys.argv) != 2:
            raise ValueError("Please provide exactly one argument: a dir_path")
        dir_path = sys.argv[1]
        if not os.path.isdir(dir_path):
            raise NotADirectoryError(dir_path)
        total_size = 0
        for path_name, subdirs, files in os.walk(dir_path):
            for file in files:
                try:
                    total_size += os.path.getsize(os.path.join(path_name, file))
                except Exception as e:
                    print(f"Error opening file {file}")

        print(f"Total size of all files in {dir_path} is {total_size} bytes")

    except NotADirectoryError as nade:
        print(f"Directory {nade} does not exist or is not a directory")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
