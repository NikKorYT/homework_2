def get_cats_info(path):
    """
    The function reads the file with the information about cats and returns a list of dictionaries with the information about each cat.
    """
    try:  
        with open(path, "r") as file:
            cats = []
            #Iterating through the file and adding the information about each cat
            while True:
                #Creating a dictionary for each cat
                cat = {"id": "-", "name": "-", "age": "-"}
                
                line = file.readline()
                
                #If the line is empty, the end of the file is reached
                if not line:
                    break
                
                #Removing the newline character from the end of the line
                line = line.removesuffix("\n")
                
                #Adding the information about the cat to the dictionary
                cat["id"], cat["name"], cat["age"] = line.split(",")
                
                #Adding the dictionary to the list
                cats.append(cat)
                
        return cats
    
    #If the file is not found, the function returns "Error"
    except IOError:
        return "Error"


if __name__ == "__main__":
    path = "./cats_file.txt"
    cats_info = get_cats_info(path)
    if cats_info == "Error":
        print("File not found")
    else:
        print(cats_info)

    
            
        