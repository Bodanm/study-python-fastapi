n_start = 1
n_end = 50

n = n_start

prosti_num = []

while n < n_end:
    if n > 1:
        proste = True
        dilnyk = 2
        while dilnyk < n:
            if n % dilnyk == 0:
                proste = False
                break
            dilnyk += 1
        if proste:
            prosti_num.append(n)
    n += 1

print(prosti_num)
