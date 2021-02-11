if __name__ == '__main__':
    n = int(input())
    arr = set(map(int, input().split()))
    lst = list(arr)
    lst.sort()
    print(lst[-2])