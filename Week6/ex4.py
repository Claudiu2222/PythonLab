import sys
import os


def main():
    try:
        if len(sys.argv) != 2:
            raise ValueError("Please provide exactly one argument: a dir_path")
        dir_path = sys.argv[1]
        if not os.path.isdir(dir_path):
            raise NotADirectoryError(dir_path)
        file_extensions = dict()

        try:
            for file_name in os.listdir(dir_path):
                if not os.path.isfile(os.path.join(dir_path, file_name)):
                    continue
                file_extension = os.path.splitext(file_name)[1]
                if file_extension not in file_extensions:
                    file_extensions[file_extension] = 0
                file_extensions[file_extension] += 1
        except OSError as e:
            print(f"Error reading directory {dir_path}: {e}")
        if len(file_extensions) == 0:
            print(f"No files found in directory {dir_path}")
        else:
            print(f"File extensions in directory {dir_path}:")
            for file_extension, count in file_extensions.items():
                print(f"{file_extension}: {count}")
    except NotADirectoryError as nade:
        print(f"Directory {nade} does not exist or is not a directory")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
