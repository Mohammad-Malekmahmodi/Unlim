my_lis = list(input(""))
result = []
for i in range(len(my_lis)-1):
    if my_lis[i] == '+' and my_lis[i+2] == '+':
        result = result.append('-')
    if my_lis[i] == '-' and my_lis[i+2] == '-':
        result = result.append('+')
    if my_lis[i] == '?' and my_lis[i+2] == '?':
        result = result.append('+')
    if my_lis[i] == '+' and my_lis[i+2] == '-':
        result = result.append('?')
    if my_lis[i] == '?' and my_lis[i+2] == '-':
        result = result.append('?')
    if my_lis[i] == '?' and my_lis[i+2] == '+':
        result = result.append('?')
    if my_lis[i] == '-' and my_lis[i+1] == '+':
        result = result.append('-')
    if my_lis[i] == '+' and my_lis[i+1] == '+':
        result = result.append('+')
    if my_lis[i] == '-' and my_lis[i+1] == '-':
        result = result.append('-')
print(result)