def total_salary(path) -> ():
    try:
        with open(path, "r", encoding="utf-8") as fh:
            count_developers=0
            total_developers_salary=0
            while True:
                line=fh.readline()
                if not line:
                    break
                total_developers_salary+=int(line.split(',')[1])
                count_developers+=1
            return (total_developers_salary, total_developers_salary//3)
    except FileNotFoundError:
        print(f"File is not found by this path {path}")
    except ValueError:
        print("Invalid salary data in your file. Please, check it.")

total_salary, average_salary=total_salary('C:/Users/HP/OneDrive/Documents/goit-algo-hw-04/developers_salary.txt')
print(f"Загальна сума заробітної плати: {total_salary}, Середня заробітна плата: {average_salary}")
