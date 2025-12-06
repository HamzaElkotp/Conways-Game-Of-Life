def next_state(cell, neighbors):
    if cell == 1:
        if neighbors < 2:
            return 0
        elif neighbors == 2 or neighbors == 3:
            return 1
        else:
            return 0
    else:
        if neighbors == 3:
            return 1
        else:
            return 0

#testing 
if __name__ == "__main__":
    print(next_state(1, 0))  
    print(next_state(1, 2))  
    print(next_state(1, 3))  
    print(next_state(1, 4)) 
    print(next_state(0, 3))  
    print(next_state(0, 2))  
