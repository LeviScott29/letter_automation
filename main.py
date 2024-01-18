# strips only names from the text document and puts them in a list
with open ("names.txt") as names_list:
    names = names_list.readlines()
    print(names)
    only_names = []
    for name in names:
        split_group = name.split()
        the_names = split_group[1].strip()
        only_names.append(the_names)
        
#takes invite template and makes a new document replacing the name block for each person on the names list
    for replacement in only_names:
        file_name= f"letter to_{replacement}"
        with open("starting_letter.txt", "r") as file:
            content = file.read()
            replace = content.replace("name", replacement)
            print(replace)
            with open(file_name, "w") as new:
                new.write(replace)
