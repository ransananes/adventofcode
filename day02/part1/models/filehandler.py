from .dict import allowed_dict, rgb_mapping, rgb_max
import re

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
        return ''.join(i for i in line if (i.isdigit() or i in allowed_dict))

    def remove_alphabet_from_file(self, content):
        return [self.remove_alphabet_from_line(line) + '\n' for line in content]

    def replace_rgb_from_line(self, line):
        for key in rgb_mapping:
            line = line.replace(key,str(rgb_mapping[key]))
        return line

    def replace_rgb_from_file(self, content):
        return [self.replace_rgb_from_line(line) + '\n' for line in content]


    # sums solution
    def sumSolution(self,content):
        sum = 0
        for integer,line in enumerate(content):
            if(self.divide_into_groups(line)):
                sum += integer+1
        return sum

    # gets a line and divides it into groups by ';'
    def divide_into_groups(self, content):
        groups = content.split(";")
        for string in groups:
            if(not self.check_group_valid(string)):
                return False
        return True


    def check_group_valid(self,group):
        line = group
        # r
        r_found = self.validateNumber('r',line)

        # g
        g_found = self.validateNumber('g',line)


        # b
        b_found = self.validateNumber('b',line)


        if(rgb_max["red"] >= int(r_found) and rgb_max["green"] >= int(g_found) and rgb_max["blue"] >= int(b_found)):
            return True
        return False

    def validateNumber(self,char,line):
        try:
            char_start = line.index(char)
            num_found = line[char_start-2:char_start]
            if(char_start - 2 < 0):
                num_found = line[char_start-1]
            else:
                num_found = line[char_start-2:char_start]
            if(re.search('[a-zA-Z:]+',num_found)):
                num_found = int(line[char_start-1])
            return num_found
        except Exception as e:
            return 0

    def sort_solution(self):
        try:
            if self.file:
                content = self.file.readlines()
                modified_content = self.replace_rgb_from_file(content)
                modified_content = self.remove_alphabet_from_file(modified_content)
                self.modify_and_replace(str(self.sumSolution(modified_content)))
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