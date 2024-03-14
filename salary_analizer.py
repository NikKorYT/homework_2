def total_salary(path) -> tuple:
    """Takes a path to a file and returns the tuple with 1st element being the total salary and 2nd element being the average salary"""
    #setting the required variables
    total = 0
    employees = 0
    #reading the file
    try:
        with open(path, "r") as file:
            #iterating through the file
            while True:
                line = file.readline()           #reading the line
                if not line:                     #if the line is empty, break the loop
                    break
                employees += 1                    #incrementing the number of employees if the line is not empty
                line = line.removesuffix("\n")    #remove the newline character
                salary = line.split(",")[1]       #split the line and get the salary
                total += int(salary)              #add the salary to the total
            average = int(total/employees)        #calculate the average
            output = (total, average)             #set the output   
        return output                             #return the output
    except FileNotFoundError:
        return "File not found"                   #return the error message if the file is not found

if __name__ == "__main__":
    if total_salary("salary_file.txt") == "File not found":
        print("Файл не знайдено")
    else:
        total, average = total_salary("salary_file.txt")
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")



