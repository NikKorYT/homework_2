


def total_salary(path) -> tuple:
    """Takes a path to a file and returns the tuple with 1st element being the total salary and 2nd element being the average salary"""
    output = ()
    total = 0
    average = 0
    with open(path, "r") as file:
        while True:
            line = file.readline()
            if not line:
                break
            print(line)

if __name__ == "__main__":
    total_salary("salary.txt")


