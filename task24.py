n = (int(input('Введите количество кустов на грядке: ')))
my_list = []
for i in range(n):
    my_list.append(int(input('Вводите последовательно число ягод на кустах: ')))
    i += i
print(my_list)
my_sum = []
for i in range(n):
    a,b,c = i,i+1,i+2
    if i == n-2:
        c = 0
    elif i == n-1:
        b,c = 0,1 
    my_sum.append(my_list[a] + my_list[b] + my_list[c])
    i += i
print(f'максимальное число ягод {max(my_sum)}')