string=input(str("please enter a string:"))
import operator
def most_frequent(string):
    d = dict()
    
    for i in string:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
        d_sorted = dict(sorted(d.items(), key = operator.itemgetter(1),reverse = True))

    return d_sorted

   
print(most_frequent(string))
