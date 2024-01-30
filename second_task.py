def get_cats_info(path: str) -> []:
    try:
        with open(path, "r", encoding="utf-8") as fh:
            cats_list=[]
            while True:
                cat_dictionary={}
                line=fh.readline()
                if not line:
                    break
                try:    
                    cat_id, cat_name, cat_age=line.split(',')
                    cat_age=cat_age.strip()
                    cat_dictionary={'id': cat_id, 'name': cat_name, 'age': cat_age}
                    cats_list.append(cat_dictionary)
                except ValueError:
                    print("Not enough values to unpack, Please, check information about cats in every line on the file.")
            return cats_list
    except FileNotFoundError:
        print(f"File is not found by this path {path}")
    
cats_info=(get_cats_info('C:/Users/HP/OneDrive/Documents/goit-algo-hw-04/cats_information.txt'))
print(*cats_info, sep="\n")
