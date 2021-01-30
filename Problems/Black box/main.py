# use the function blackbox(lst) that is already defined
lst = [1, 2, 3, 4]
old_id = id(lst)
new_lst = blackbox(lst)
if id(new_lst) == old_id:
    print("modifies")
else:
    print("new")
