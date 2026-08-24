import os

# Loop from 1 to 4
for i in range(1, 3):
    filename = f"11-teht{i}.py"
    
    # 'w' mode creates an empty file; 'pass' leaves it blank
    with open(filename, "w") as f:
        pass
        
    print(f"Created empty file: {filename}")
