# Outer loop: Iterate through numbers 1 to 9
for num in range(1, 10):  
    print(f"\nMultiplication Table for {num}:")  # Header for each table
    
    # Inner loop: Iterate through 1 to 10 for multiplication
    for i in range(1, 11):  
        print(f"{num} x {i} = {num * i}")  # Print multiplication result

