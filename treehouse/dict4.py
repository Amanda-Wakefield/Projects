# The dictionary will be something like:
my_dict = {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],
           'Kenneth Love': ['Python Basics', 'Python Collections']}


def most_classes(teacher_dict):
    teacher_list = []
    class_list = []
    for teacher in teacher_dict:
        class_count = len(teacher_dict[teacher])
        teacher_list.append(teacher)
        class_list.append(class_count)
    location = class_list.index(max(class_list))
    # print(location)
    return teacher_list[location]

most_classes(my_dict)


def num_teachers(teacher_dict):
    # print(len(teacher_dict))
    return len(teacher_dict)

num_teachers(my_dict)


def stats(teacher_dict):
    stringList = []
    for teacher in teacher_dict:
        temp = ['', '']
        num = len(teacher_dict[teacher])
        temp[0] = teacher
        temp[1] = num
        # dict_temp= {'name':teacher, 'number of classes':num}
        # temp[0] = '<{name}>, <{number of classes}>'.format(**dict_temp)
        stringList.append(temp)
    # print(stringList)
    return stringList

stats(my_dict)


def courses(teacher_dict):
    course_list = []
    for teacher in teacher_dict.values():
        for course in teacher:
            course_list.append(course)
    print(len(course_list))
    return course_list

courses(my_dict)
