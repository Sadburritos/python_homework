start = 32  
end = 126  
count = 0  

current = start  
while current <= end:
    print(f"{current}: {chr(current)}", end="\t")           #Честно, эту сттроку я нагло украл
    count += 1

    if count % 5 == 0:
        print()

    current += 1
