def display_numbers(file_path: str):
    """
    Reads each line from the file specified by file_path.
    Display every encountered comma-separated numbers line by line.

    Args:
        file_path (str): Path of the file that will be read.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If any item in any line is not a number/
    """
    with open(file_path, "r") as f:
        for line in f:
            number_list = line.split(",")
            for number in number_list:
                if not number.strip().isdigit():
                    raise ValueError(f"{number.strip()} is not a number")
                print(number.strip())


if __name__ == "__main__":
    try:
        file_path = "numbers.txt"
        display_numbers(file_path)
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as error:
        print(f"An error occurred: {error}")
