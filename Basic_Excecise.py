def first_last_num(numb_list):
    print("Given the list", numb_list)

    first_num = numb_list[0]
    last_num = numb_list[-1]

    if first_num == last_num:
        return True
    else:
        return False


numbers1 = [10, 20, 44, 66, 10]
print("The expected result is", first_last_num(numbers1))


def count_word(str_x):
    checking_word = "Emma"
    cnt = str_x.count(checking_word)
    print(cnt)


count_word("Emma is good developer. Emma is a writer")

for i in range(6):
    for j in range(i):
        print(i,end=' ')
    print('\n')

for i in range(1,6,1):
    for j in range(1,i+1):
        print(j,end='')
    print('\n')