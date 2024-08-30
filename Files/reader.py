import pathlib

def func():
    extensions = (".cpp", ".hpp", ".h", ".cxx", ".hxx", ".py", ".pyc", ".pyd", ".pyo", ".pyw", ".pyx", ".pxd", ".pxi", ".pyzw", ".js", ".C", ".c")
    choices = ["read", "quit"]

    while True:
        choice = input("read to read the contents of a file or quit:\n").strip().lower()
        if choice not in choices:
            print("Invalid input. Please try again.")
            continue

        if choice == "quit":
            print("Quiting")
            return

        directory = input("What is the file you want to open (Please input the directory correctly):\n")
        file_path = pathlib.Path(directory)

        if not file_path.suffix in extensions:
            warning = input("Are you sure? The file you are entering could contain malware.Y/N:").strip().upper()
            if warning != "Y":
                print("Quiting for your safety")
                return

        try:
            text = file_path.read_text()
            print(text)
        except FileNotFoundError:
            print(f"File '{directory}' not found")
        except PermissionError:
            print(f"Permission denied for file '{directory}'")
        except IOError as e:
            print(f"Error reading file '{directory}': {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

func()
