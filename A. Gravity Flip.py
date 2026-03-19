def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    result = []
    for i in range(n):
        result.append(arr[i])
    print(result)
if __name__ == "__main__":
    solve()