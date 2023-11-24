import os
import sys

text_extensions = {
    ".txt",
    ".py",
    ".c",
    ".cpp",
    ".java",
    ".js",
    ".html",
    ".css",
    ".xml",
    ".json",
    ".csv",
}


def main():
    try:
        if len(sys.argv) != 3:
            raise ValueError(
                "Please provide exactly two arguments: a dir_path and a file_extension"
            )
        dir_path, file_extension = sys.argv[1], sys.argv[2].lower()
        if not os.path.isdir(dir_path):
            raise NotADirectoryError(dir_path)
        if not file_extension.startswith("."):
            raise ValueError("The file extension should start with a dot (.)")
        for path_name, subdirs, files in os.walk(dir_path):
            for file in files:
                if file.endswith(file_extension):
                    read_file_and_print(os.path.join(path_name, file), file_extension)
    except NotADirectoryError as nade:
        print(f"Directory '{nade}' does not exist or is not a directory")
    except Exception as e:
        print(e)


def read_file_and_print(file_name, file_extension):
    try:
        mode = "r" if is_text_file(file_extension) else "rb"
        with open(file_name, mode) as fd:
            print(f"File contents of file {file_name}: ")
            print(fd.read())
        print("-" * 50)
    except IOError:
        print(f"Error opening file {file_name}")


def is_text_file(file_extension):
    if file_extension in text_extensions:
        return True
    return False


if __name__ == "__main__":
    main()
