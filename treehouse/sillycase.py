# The first half of the string, rounded with round(), should be lowercased.
# The second half should be uppercased.
# E.g. "Treehouse" should come back as "treeHOUSE"

def sillycase(iList):
    halfLen= round(len(iList)/2,0)
    aList = iList[0:int(halfLen)]
    aList = [x.lower() for x in aList]
    bList = iList[int(halfLen):]
    bList = [x.upper() for x in bList]
    cList = aList + bList
    rString = ''.join(cList)
    return(rString)
inlist = list('kenneth')
sillycase(inlist)