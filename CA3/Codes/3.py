inputs = list(map(int,input().split()))
black_tables = set()
rectangles = 0
for x in range(inputs[2]):
    table = tuple(map(int,input().split()))
    if not (table[0], table[1]) in black_tables:
        if not (table[0]-1, table[1]) in black_tables and not (table[0]+1, table[1]) in black_tables and not (table[0], table[1]-1) in black_tables and not (table[0], table[1]+1) in black_tables:
            rectangles += 2
        elif (table[0]-1, table[1]) in black_tables and not (table[0]+1, table[1]) in black_tables and not (table[0], table[1]-1) in black_tables and not (table[0], table[1]+1) in black_tables:
            rectangles += 1
        elif not (table[0]-1, table[1]) in black_tables and (table[0]+1, table[1]) in black_tables and not (table[0], table[1]-1) in black_tables and not (table[0], table[1]+1) in black_tables:
            rectangles += 1
        elif not (table[0]-1, table[1]) in black_tables and not (table[0]+1, table[1]) in black_tables and (table[0], table[1]-1) in black_tables and not (table[0], table[1]+1) in black_tables:
            rectangles += 1
        elif not (table[0]-1, table[1]) in black_tables and not (table[0]+1, table[1]) in black_tables and not (table[0], table[1]-1) in black_tables and (table[0], table[1]+1) in black_tables:
            rectangles += 1
        elif not (table[0]-1, table[1]) in black_tables and (table[0]+1, table[1]) in black_tables and (table[0], table[1]-1) in black_tables and (table[0], table[1]+1) in black_tables:
            rectangles -= 1
        elif (table[0]-1, table[1]) in black_tables and not (table[0]+1, table[1]) in black_tables and (table[0], table[1]-1) in black_tables and (table[0], table[1]+1) in black_tables:
            rectangles -= 1
        elif (table[0]-1, table[1]) in black_tables and (table[0]+1, table[1]) in black_tables and not (table[0], table[1]-1) in black_tables and (table[0], table[1]+1) in black_tables:
            rectangles -= 1
        elif (table[0]-1, table[1]) in black_tables and (table[0]+1, table[1]) in black_tables and (table[0], table[1]-1) in black_tables and not (table[0], table[1]+1) in black_tables:
            rectangles -= 1
        elif (table[0]-1, table[1]) in black_tables and (table[0]+1, table[1]) in black_tables and (table[0], table[1]-1) in black_tables and (table[0], table[1]+1) in black_tables:
            rectangles -= 2
        black_tables.add(table)
    print(rectangles)