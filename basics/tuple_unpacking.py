def employee(tup):
    current_max = 0
    best_employee = ""
    
    for employee,hours in tup:
        if hours>current_max:
            current_max = hours
            best_employee = employee
        else:
            pass
    return employee

tup1 = [("Shoham",10),("Parag",20),("Swapnil",30)]
result = employee(tup1)
print(result)
