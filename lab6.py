
def find_min(L, m = 1):
    #return bs(L)
    return help_min(L,m)

def bs(L, item=None, left = 0, right = None):
    if item is None: item = L[0]
    if right is None: right = len(L)
    if right - left == 0: return item
    if right - left == 1:
        if L[left] < item:
            return L[left]
        return item
    median = (right + left) // 2

    if L[median] < item:
        item = L[median]
    bs1 = bs(L, item, left, median)
    #bsh = bs(L, item, median, right)
    return bs1 #min(bs1,bsh)
    pass

def help_min(L, m = 1):
    
    len_list = len(L)
    if len_list == 1: return L[0]
    elif (len_list == 2):
        if L[0] < L[1]:
            return L[0]
        else:
            return L[1]
    
    median = len_list // 2
    frst_half = L[:(median+1)]
    sec_half = L[(median+1):]
    
    if L[median] <= L[median + 1]:
        return help_min(frst_half, m)
    else:
        return help_min(sec_half, m)
    pass


def help2_min(L, m=1):
    len_lst = len(L)
    median = len_lst // 2
    if len_lst==1:
        return L[0]
    elif len_lst >= 2:
        if L[median]<=L[median+1]:
            return help2_min(L[:(median+1)], m=1)
        else:
            return help2_min(L[median:], m=1)
    pass
    
#print(help_min([7,4, 3, 2, 6, 8, 9]))
#print(help_min([8,6,3,2,1]))
