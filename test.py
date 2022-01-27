def tower_builder(n_floors):
    increament = 1
    decreament = n_floors - 1
    tower_list = []
    for i in  range(n_floors):
       tower_list.append((" " * decreament) + ("*" * increament) + (" " * decreament))
       increament += 2
       decreament -= 1
    return tower_list
        
        
        
if "__main__" == __name__:
    tower_builder(9)
    
    
    # print(((" " * decreament) + "*" * (increament)).center((2*n_floors) - 1) + (" " * decreament))
    # tower_list.append(((" " * decreament)+ "*" * (increament)).center((2*n_floors) - 1) + (" " * decreament))