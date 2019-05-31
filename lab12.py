import re


def count_operations():
    first_pattern = r"24/Mar/2009:((14:39:3[5-9])|(14:[4-5][0-9]:[0-9][0-9])|(1[5-9]:\d\d:\d\d)|(2[0-3]:\d\d:\d\d)).*TH_photo.*200"
    second_pattern = r"25/Mar/2009:((0[0-9]:\d\d:\d\d)|(10:\d\d:\d\d)|(11:[0-3][0-9]:\d\d)|(11:4[0-2]:\d\d)|(11:43:[0-2][0-9])).*TH_photo.*200"
    file = open("access.log", "r")
    counter = 0
    count = 0
    for line in file.readlines():
        count += 1
        if re.search(first_pattern, line):
            counter += 1
            print(line)
        if re.search(second_pattern, line):
            counter += 1
            print(line)
    print(count)
    print(counter)


count_operations()
print(count_operations)
