def top_n(items,n):
    """
 Return the top n items in an arrayn in desc order.

    Args:
        items(array): list or array-like object
        n (int):number of items to return
    
    Retrun
        array:top n elements in items
    """
    for i in range(0,n):
        for j in range(len(items)-1-i):
            if items[j]>items[j+1]:
                items[j],items[j+1]=items[j+1],items[j]

    top_n=items[-n:]

    return top_n[::-1]


