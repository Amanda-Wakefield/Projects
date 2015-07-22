the_list = ["a", 2, 3, 1, False, [1, 2, 3]]

loop_count = 0
num_track = 0

while (loop_count <= len(the_list)+1):
    if type(the_list[num_track]) == int:
        loop_count +=1
        num_track +=1
    else:
        del the_list[num_track]
        loop_count +=1
print(the_list)
