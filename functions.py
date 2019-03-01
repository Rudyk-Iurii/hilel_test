#task 1
def task1(list):
    return list.count(1)

#task 2
def task2(list):
    def median(list):
        l = len(list)
        if l % 2 == 1:
            return sorted(list)[l // 2]
        else:
            return sum(sorted(list)[l // 2 - 1:l // 2 + 1]) / 2.0
    return min(list), max(list), (sum(list)/len(list)), median(list)