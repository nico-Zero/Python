def insertion_sort(the_list):
    if  isinstance(the_list, dict):
        sort_list = list(the_list.values())
    else:
        sort_list = the_list

    for i in range(1, len(sort_list)):
        if sort_list[i - 1] > sort_list[i]:
            for j in range(i, 0, -1):
                if sort_list[j] < sort_list[j - 1]:
                    sort_list[j], sort_list[j - 1] = sort_list[j - 1], sort_list[j]
                else:
                    break

    if isinstance(the_list, dict):
        for i,j in zip(the_list.keys(),sort_list):
            the_list[i] = j
        return the_list
    else:
        return sort_list

