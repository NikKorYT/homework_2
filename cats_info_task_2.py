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
    elif cats_info == [
    {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
    {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
    {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
    {"id": "60b90c3b13067a15887e1ae4", "name": "Simon", "age": "12"},
    {"id": "60b90c4613067a15887e1ae5", "name": "Tessi", "age": "5"},]:
        
        print("The function works correctly")
        print(cats_info)
    else:
        print("The function works incorrectly")
        print(cats_info)

    
            
        