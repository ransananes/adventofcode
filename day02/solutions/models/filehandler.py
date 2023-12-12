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
                self.file.seek(0)
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
            if(self.divide_into_groups(line, self.startFindingNum)):
                sum += integer+1
        return sum

    def multiplySolution(self,content):
        sum = 0
        for line in content:
            sum += self.divide_into_groups(line, self.FindingMax)
        return sum

    def FindingMax(self,groups):
        sum = 0
        r_max, g_max, b_max = 0,0,0
        for string in groups:
           r,g,b = self.check_group_valid(string,self.findMaxTup)
           r_max = max(r_max,int(r))
           g_max = max(g_max,int(g))
           b_max = max(b_max,int(b))
           sum = r_max * g_max * b_max
        return sum
    def findMaxTup(self,r,g,b):
        return (r,g,b)

    
    # gets a line and divides it into groups by ';'
    def divide_into_groups(self, content, func):
        groups = content.split(";")
        return func(groups)
    #region part1
    def startFindingNum(self,groups):
        for string in groups:
            if(not self.check_group_valid(string,self.validateExceed)):
                return False
        return True

    def check_group_valid(self,group,func):
        line = group
        # r
        r_found = self.validateNumber('r',line)

        # g
        g_found = self.validateNumber('g',line)


        # b
        b_found = self.validateNumber('b',line)


        return func(r_found,g_found,b_found)

    def validateExceed(self,r_found,g_found,b_found):
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
    #endregion
    def sort_solution(self,part1):
        # try:
        if self.file:
            content = self.file.readlines()
            modified_content = self.replace_rgb_from_file(content)
            modified_content = self.remove_alphabet_from_file(modified_content)
            if(part1):
                self.modify_and_replace(str(self.sumSolution(modified_content)))
            else:
                self.modify_and_replace(str(self.multiplySolution(modified_content)))
        # except Exception as e:
        #     print(f"Error sorting solution: {e}")

