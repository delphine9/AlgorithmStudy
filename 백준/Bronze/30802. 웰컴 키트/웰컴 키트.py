n = int(input())

num = list(map(int, input().split()))

t, p = map(int, input().split())

sum_tShirt = 0
for tshirt in num:
    if tshirt % t == 0:
        sum_tShirt += tshirt//t
    else:
        sum_tShirt += tshirt//t + 1

penSet = n // p
penPiece = n % p

print(sum_tShirt)
print(penSet, penPiece)