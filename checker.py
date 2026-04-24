import os
from datetime import datetime

path = './assets'
warning_size = 5 * 1024 * 1024 # 5MB in bytes
error_size = 20 * 1024 * 1024 # 10MB in bytes
errors_and_warnings = [] # List to store errors and warnings

def get_files():
    files = []

    if not os.path.exists(path): # Checks if the directory exists
        errors_and_warnings.append(f"Directory '{path}' does not exist.")
        return
    
    for file in os.listdir(path): # if the directory exists, goes through all the files
        if os.path.isfile(os.path.join(path, file)): # If it's a file
            files.append(file) # Adds it to the list
            print(file) # prints the file name

        else: # If it's a directory
            if not os.listdir(path + '/' + file): # If the directory is empty
                errors_and_warnings.append(f"WARNING: Directory '{file}' is empty.")
                continue # skips the empty directory

            for inside_file in os.listdir(path + '/' + file): # goes inside the directory, file for file
                if os.path.isfile(os.path.join(path + '/' + file, inside_file)): # If it's a file
                    for existing_file in files: # chekcs the added files
                        file_name = existing_file.split('/')[-1] # gets the file name without the path
                        if inside_file == file_name: # if theres a file with the same name
                            errors_and_warnings.append(f"WARNING: File '{inside_file}' already exists in the directory in '{file}'. Check for duplicates.")

                    files.append(file + '/' + inside_file) # adds it to the list
                    print(file + '/' + inside_file) # prints the file name

    return files

def validate_file_name(file_name):
    if ' ' in file_name: # If the file name has spaces
        print(f"File name '{file_name}' contains spaces. Renaming...")
        rename_file_empty_spaces(file_name) # replace the splaces with underscores and rename the file

    elif 'ñ' in file_name: # If the file name has 'ñ' (cause I forget to change my keyboard and forget my english jeje)
        print(f"File name '{file_name}' contains 'ñ'. Replacing with 'n'...")
        rename_file_n(file_name) # replace 'ñ' with 'n' and rename the file

def rename_file_empty_spaces(file_name):
    new_name = file_name.replace(' ', '_')
    os.rename(os.path.join(path, file_name), os.path.join(path, new_name))
    print(f"Renamed '{file_name}' to '{new_name}'.")

def rename_file_n(file_name):
    new_name = file_name.replace('ñ', 'n')
    os.rename(os.path.join(path, file_name), os.path.join(path, new_name))
    print(f"Renamed '{file_name}' to '{new_name}'.")

def get_file_size(file_name):
    file_size = os.path.getsize(os.path.join(path, file_name))

    if file_size > warning_size and file_size <= error_size: # file greater than 5MB and less than 20MB
        errors_and_warnings.append(f"WARNING: File '{file_name}' is larger than 5MB.")

    elif file_size > error_size: # file greater than 20MB
        errors_and_warnings.append(f"ERROR: File '{file_name}' is larger than 20MB.")

def generate_report(files):
    if not os.path.exists('reports'): # if the reports directory exists
        os.mkdir('reports') # Creates a reports directory if it doesn't exist

    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_file = f'reports/report_{now}.txt' # Creates a report file with the current date and time
    total_warnings = len([item for item in errors_and_warnings if item.startswith("WARNING")])
    total_errors = len([item for item in errors_and_warnings if item.startswith("ERROR")])

    with open(report_file, 'w') as f:
        f.write("Vancouver Film School\n")
        f.write("Pipelines\n")
        f.write("Assignment 2\n")
        f.write("Diana Lucia Fernandez Villatoro\n")
        f.write("PG29\n\n")

        f.write("---------------------------------------------------\n\n")
        f.write("ASSET HEALTH CHECK REPORT\n\n")

        f.write("==================================================\n")
        f.write(f"Report generated on: {now}\n")
        f.write("==================================================\n\n")

        f.write(f"Total files checked: {len(files)}\n\n")
        f.write(f"WARNINGS generated: {total_warnings}\n")
        f.write(f"ERRORS generated: {total_errors}\n")
        f.write("==================================================\n\n")

        if(errors_and_warnings): # If there are errors or warnings
            f.write("Details:\n")
            for line in errors_and_warnings:
                f.write(line + '\n') # Writes the errors and warnings to a text file
        else:
            f.write("No errors or warnings found.\n")

if __name__ == "__main__":
    files = []
    files = get_files() # Searches and gets all the files in the folder and the subfolders

    if files: # If it finds files
        for file in files: 
            validate_file_name(file) # Validates the file name
            get_file_size(file) # Gets the file size

    generate_report(files) # Generates the report with the errors and warnings