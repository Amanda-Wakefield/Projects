# combo(['swallow', 'snake', 'parrot'], 'abc')
# Output:
# [('swallow', 'a'), ('snake', 'b'), ('parrot', 'c')]
# If you use list.append(), you'll want to pass it a tuple of new values.
# Using enumerate() here can save you a variable or two.

def combo(it1, it2):
    it2 = list(it2)
    my_list = []
    for num, animal in enumerate(it1):
        a = (animal, it2[num])
        my_list.append(a)
    print(my_list)

it1 = ['swallow', 'snake', 'parrot']
it2 = 'abc'
combo(it1, it2)