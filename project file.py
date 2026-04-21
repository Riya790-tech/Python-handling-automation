import os
import shutil
import csv

# ---------------- FILE READ/WRITE (TXT) ----------------

def write_txt_file(filename, content):
    try:
        # Open file in write mode ('w') → creates file if not exists
        with open(filename, 'w') as file:
            file.write(content)
        print("TXT file written successfully")

    except Exception as e:
        print("Error writing TXT file:", e)


def read_txt_file(filename):
    try:
        # Open file in read mode ('r')
        with open(filename, 'r') as file:
            data = file.read()
        print("TXT file content:")
        print(data)

    except FileNotFoundError:
        print("Error: TXT file not found")
    except Exception as e:
        print("Error reading TXT file:", e)


# ---------------- FILE READ/WRITE (CSV) ----------------

def write_csv_file(filename):
    try:
        # Writing CSV file using csv.writer
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)

            # Writing rows (list of lists)
            writer.writerow(["Name", "Age", "City"])
            writer.writerow(["Riya", 20, "Delhi"])
            writer.writerow(["Aman", 22, "Mumbai"])

        print("CSV file written successfully")

    except Exception as e:
        print("Error writing CSV file:", e)


def read_csv_file(filename):
    try:
        # Reading CSV file
        with open(filename, 'r') as file:
            reader = csv.reader(file)

            print("CSV file content:")
            for row in reader:
                print(row)

    except FileNotFoundError:
        print("Error: CSV file not found")
    except Exception as e:
        print("Error reading CSV file:", e)


# ---------------- FILE OPERATIONS ----------------

def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)  # Rename file
        print(f"Renamed '{old_name}' → '{new_name}'")

    except FileNotFoundError:
        print("Error: File not found for renaming")
    except Exception as e:
        print("Error renaming file:", e)


def move_file(source, destination):
    try:
        shutil.move(source, destination)  # Move file
        print(f"Moved '{source}' → '{destination}'")

    except FileNotFoundError:
        print("Error: File not found for moving")
    except Exception as e:
        print("Error moving file:", e)


def delete_file(filename):
    try:
        os.remove(filename)  # Delete file
        print(f"Deleted '{filename}'")

    except FileNotFoundError:
        print("Error: File not found for deletion")
    except Exception as e:
        print("Error deleting file:", e)


# ---------------- MAIN EXECUTION ----------------

# TXT operations
write_txt_file("sample.txt", "Hello! This is a sample text file.")
read_txt_file("sample.txt")

# CSV operations
write_csv_file("data.csv")
read_csv_file("data.csv")

# File automation operations
rename_file("sample.txt", "renamed.txt")
move_file("renamed.txt", "C:/Users/Public/renamed.txt")
delete_file("C:/Users/Public/renamed.txt")