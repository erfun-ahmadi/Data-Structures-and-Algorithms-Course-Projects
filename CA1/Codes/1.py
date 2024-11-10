row_col = list(map(int,input().split()))
row = row_col[0]
col = row_col[1]
titles = input()
titles_list = titles.split(",")
all_items = list()
for i in range(row):
    items = input()
    items_list = items.split(",")
    all_items.append(items_list)
last_line = input()
last_line_list = last_line.split(" ")    
sort_by = last_line_list[2]
which_item = titles_list.index(sort_by)
all_items = sorted(all_items, key=lambda x: x[which_item])
for i in range(row):
    print(*all_items[i], sep=',')