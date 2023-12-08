class FileHandler:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def open_file(self):
        try:
            self.file = open(self.filename, self.mode)
            print(f"File '{self.filename}' opened in '{self.mode}' mode.")
        except FileNotFoundError:
            print(f"File '{self.filename}' not found.")
        except Exception as e:
            print(f"Error opening file: {e}")

    def close_file(self):
        if self.file:
            self.file.close()
            print(f"File '{self.filename}' closed.")
        else:
            print("No file is currently open.")

    def copy_to(self, new_filename):
        try:
            if self.file:
                with open(new_filename, 'w') as new_file:
                    new_file.write(self.file.read())
                print(f"Data copied to '{new_filename}' successfully.")
            else:
                print("No file is currently open.")
        except Exception as e:
            print(f"Error copying data: {e}")

    def modify_and_replace(self, data):
        try:
            if self.file:
                self.file.seek(0)
                self.file.truncate()
                self.file.writelines(data)
                print("File content modified and replaced successfully.")
            else:
                print("No file is currently open.")
        except Exception as e:
            print(f"Error modifying and replacing content: {e}")

    def remove_alphabet_from_line(self, line):
        return ''.join(i for i in line if i.isdigit())

    def remove_alphabet_from_file(self, content):
        return [self.remove_alphabet_from_line(line) + '\n' for line in content]

    def remove_double_digits(self, line):
        if line[-2] == line[0]:
            return line[0] * 2
        return line[0] + line[-2]

    def remove_unnecessary_digits(self, content):
        return [self.remove_double_digits(line) + '\n' for line in content]

    def sort_solution(self):
        try:
            if self.file:
                content = self.file.readlines()
                modified_content = self.remove_alphabet_from_file(content)
                modified_content = self.remove_unnecessary_digits(modified_content)
                self.modify_and_replace(modified_content)
                
        except Exception as e:
            print(f"Error sorting solution: {e}")

    def sum_numbers(self):
        try:
            self.file.seek(0)
            content = self.file.readlines()
            total_sum = sum(int(line.strip()) for line in content)
            print(f"Total sum of numbers: {total_sum}")
        except Exception as e:
            print(f"Error calculating sum: {e}")