

def read_info():
    info = []
    result = []
    with open("in.txt") as f:
        data = f.readlines()
        count_list = int(data[0])
        for i in range(1, count_list + 1):
            info.append(data[i])
    for data in info:
        list_adjacency = []
        for point in data.split(" "):
            list_adjacency.append(int(point))
        result.append(list_adjacency)
    return result


def create_matrix():
    list = read_info()
    result = []
    for i in range(0, len(list)):
        sm = []
        for j in range(0, len(list)):
            if i == j:
                sm.append(0)
            else:
                sm.append(abs(list[i][0] - list[j][0]) + abs(list[i][1] - list[j][1]))
        result.append(sm)
    return result


def search_min(tr, vizited):
    min = float("inf")
    index_to = 0
    index_from = 0
    for ind in vizited:
        for i in range(0, len(tr[ind])):
            if tr[ind][i] > 0 and tr[ind][i] < min and i not in vizited:
                min = tr[ind][i]
                index_to = i
                index_from = ind
    return [min, index_to, index_from]


def prim(matr):
    vizited = [0]
    result = []
    for i in range(len(matr) - 1):
        weight, index_to, index_from = search_min(matr, vizited)
        result.append([index_from + 1, index_to + 1, weight])
        vizited.append(index_to)
    result.sort(key=lambda a: a[0])
    return result


def create_result(result):
    list = []
    for i in range(len(a)):
        list.append([])
    sum = 0
    for element in result:
        list[element[0] - 1].append(element[1])
        list[element[1] - 1].append(element[0])
        sum += element[2]
    for element in list:
        element.sort()
    return list, sum


a = create_matrix()
b = prim(a)
result, sum = create_result(b)
with open("out.txt", "w") as f:
    for list in result:
        for element in list:
            f.write(str(element) + " ")
        f.write("0\n")
    f.write(str(sum))
