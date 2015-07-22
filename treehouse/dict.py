# You can check for dictionary membership using the
# "key in dict" syntax from lists.

### Example
my_dict = {'apples': 1, 'bananas': 2, 'coconuts': 3}
my_list = ['apples', 'coconuts', 'grapes', 'strawberries']
def members(my_dict, my_list):
    count = 0
    for num in range(len(my_list)):
        if my_list[num] in my_dict:
            count +=1
            print(my_list[num])
    return(count)
members(my_dict,my_list)