def average(array):
    # your code goes here
    arr = set(array)
    summ = sum(arr)
    N = len(arr)
    summ1 = "{:.3f}".format(summ)
    n1 = "{:.3f}".format(N)
    avg=float(summ1)/float(n1)
    avg1 = "{:.3f}".format(avg)
    return avg1

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
