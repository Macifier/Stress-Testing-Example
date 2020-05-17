def get_max_product(n, array):
    product = 0
    for i in range(n):
        for j in range(i+1, n):
            product = max(product, array[i] * array[j])
    return product


if __name__ == "__main__":
    n = int(input())
    numbers = [int(x) for x in input().split()]
    product = get_max_product(n, numbers)
    print(product)
