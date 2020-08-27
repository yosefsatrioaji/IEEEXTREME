from itertools import combinations

okei = 0
t = int(input())
for i in range(t):
    c, n = input().split()
    list = {}
    list_c_sum = {}
    a_list = {}
    for j in range(int(n)):
        w, f = input().split()
        list[int(w)] = int(f)
        for k in range(1, len(list) + 1):
            for l in combinations(list, k):
                list_c = str(l).replace('(', '').replace(')', '').replace(',', '')
                list_c_sum[list_c] = sum(l)
                res = {key: value for key, value in list_c_sum.items() if value < int(c) + 1}
                for m, n in res.items():
                    if len(m) > 1:
                        parted = m.split()
                        for o in parted:
                            p = list[int(o)]
                            okei = p
                            a_list[okei] = n
                            final = max(a_list.keys())
                    else:
                        okei = list[int(m)]
                        a_list[okei] = n
                        final = max(a_list.keys())
    print(final)
