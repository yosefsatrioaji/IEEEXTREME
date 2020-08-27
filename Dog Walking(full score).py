T = int(input())
for i in range(T):
    N, K = [int(q) for q in input().split()]
    dogs = []
    for j in range(N):
        size = int(input())
        dogs.append(size)
    dogs.sort()
    hitung = dogs[-1]-dogs[0]
    gatau = []
    for a,b in zip(dogs,dogs[1:]):
        doggy = a-b
        gatau.append(doggy)
    gatau.sort()
    print(hitung+sum(gatau[:K-1]))