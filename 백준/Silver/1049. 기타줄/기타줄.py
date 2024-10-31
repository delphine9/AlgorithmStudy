n, m = map(int, input().split())

brand = []
for i in range(m):
    brand.append(list(map(int, input().split())))

package = float('inf')
single = float('inf')
for pack, sing in brand:
    package = min(pack, package)
    single = min(sing, single)

price = min((n//6 + (1 if n % 6 else 0)) * package,
            (n//6) * package + (n % 6)*single, n * single)
print(price)