'''
Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible, 
containing distinct letters, each taken only once - coming from s1 or s2. 

Examples: ``` a = "xyaabbbccccdefww" b = "xxxxyyyyabklmopq" longest(a, b) -> "abcdefklmopqwxy" 
a = "abcdefghijklmnopqrstuvwxyz" longest(a, a) -> "abcdefghijklmnopqrstuvwxyz" ```
'''
def longest(s1, s2):
    if(s1.isalpha == False):
        raise Exception('{} is not a string, please make sure you enter a string.'.format(s1))
    elif(s2.isalpha == False):
        raise Exception('{} is not a string, please make sure you enter a string.'.format(s2))
    else:
        new_list = []
        for x in s1:
            if(x in new_list):
                continue
            else:
                new_list.append(x)
        for y in s2:
            if(y in new_list):
                continue
            else:
                new_list.append(y)
        new_list.sort(key=None)
        official_list = ''.join(new_list)
        print(official_list)
        return(official_list)

"""
This is the consolodated solution.  set creates a unique set between the 2 strings and then sorted wraps around the created string.  done.
def longest(a1, a2):
    print("".join(sorted(set(a1 + a2))))
    return "".join(sorted(set(a1 + a2)))"""

longest('xyaabbbccccdefww', 'xxxxyyyyabklmopq')
