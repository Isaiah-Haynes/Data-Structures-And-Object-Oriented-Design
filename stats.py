
def compute_mean(collection, n=1):
    len_collection = len(collection)
    sum_collection = 0
    for num in collection:
        sum_collection += num
    mean = round((sum_collection / len_collection), n)
    return mean
    pass

def compute_median(collection):
    len_collection = len(collection)
    collection.sort()
    if (len_collection%2 != 0):
        x = (len_collection // 2)
        median = collection[x]
        
    elif (len_collection%2 == 0):
        x = (len_collection // 2) - 1
        y = x + 1
        if (collection[x] < collection[y]):
            median = collection[x]
        elif (collection[y] < collection[x]):
            median = collection[y]
        else:
            median = collection[x]

    return median
    pass

def compute_mode(collection):
    time_in_collect = []
    for num in collection:
        a = collection.count(num)
        time_in_collect.append(a)
    frst_mode = max(time_in_collect)
    index_mode = time_in_collect.index(frst_mode)
    mode = collection[index_mode]
    return mode
    pass

def compute_stats(collection):
    mean_final = compute_mean(collection)
    median_final = compute_median(collection)
    mode_final = compute_mode(collection)
    return (mean_final, median_final, mode_final)
    pass















