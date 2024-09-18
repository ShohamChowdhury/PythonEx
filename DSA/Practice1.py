def avg_temp(day_amount):
    temp_list = []
    for i in range(day_amount):
        temp_list.append(int(input(f"Day {i+1}'s highest temp : ")))
    return temp_list
def above_avg_temp(temp_list):
    k = 0
    avg_tem = sum(temp_list)/len(temp_list)
    for i in temp_list:
        if avg_tem < i:
            k+=1
    print(f"\nAverage Temperature : {avg_tem}")
    print(f"{k} day(s) above average Temperature")

day_amount = int(input("How many day's Temp?\n"))
above_avg_temp(avg_temp(day_amount))




    
        
    
        
    