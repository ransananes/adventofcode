from models.filehandler import FileHandler

if  __name__ == "__main__":
    file_handler = FileHandler("../input.txt", "r") 
    file_handler.open_file()
    file_handler.copy_to("solution.txt")
    file_handler.close_file()

    solution_handler = FileHandler("solution.txt", "r+") 
    solution_handler.open_file()
    solution_handler.sort_solution()
    solution_handler.sum_numbers()
