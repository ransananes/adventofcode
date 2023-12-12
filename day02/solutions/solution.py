from models.filehandler import FileHandler
if  __name__ == "__main__":
    file_handler = FileHandler("./input.txt", "r") 
    file_handler.open_file()
    file_handler.copy_to("solution01.txt")
    file_handler.copy_to("solution02.txt")
    file_handler.close_file()

    # PART ONE
    solution_handler = FileHandler("solution01.txt", "r+") 
    solution_handler.open_file()
    solution_handler.sort_solution(True)

    # PART TWO
    solution_handler = FileHandler("solution02.txt", "r+") 
    solution_handler.open_file()
    solution_handler.sort_solution(False)