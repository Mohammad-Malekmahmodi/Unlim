def sd(n):
    n_st = str(n)
    ss = [n_st[max(i -3,0):i] for i in range(len(n_st),0,-3)][::-1]
    result = ','.join(ss)
    print(result)
user = input("")
nn = int(user)

sd(nn)
