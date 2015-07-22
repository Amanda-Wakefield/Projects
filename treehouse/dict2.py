def word_count(my_string):
    dict={}
    my_string= my_string.lower()
    my_list = sorted(my_string.split())
    for num in range(0, len(my_list)):
        new_dict = {my_list[num]:0}
        dict.update(new_dict)
    for word in my_list:
        dict[word] = dict[word] + 1
        print('word:', word, 'is in dict:', dict)
    return dict

my_string = "I am that I am"
word_count(my_string)