iterable = list(range(20))


def first_4(iterable):
    return iterable[:4]
first_4(iterable)

def odds(iterable):
    return( iterable[1:len(iterable):2])

def first_and_last_4(iterable):
    answer=iterable[:4]
    answer.append(iterable[-4])
    answer.append(iterable[-3])
    answer.append(iterable[-2])
    answer.append(iterable[-1])
    print(answer)
    return answer

first_and_last_4(iterable)