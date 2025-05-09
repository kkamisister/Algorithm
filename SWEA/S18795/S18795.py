import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    def quick(arr, start, end):
        if start >= end:
            return
        pivot = start
        left = start+1
        right = end

        while left <= right:
            while left <= end and arr[left] <= arr[pivot]:
                left += 1
            while right > start and arr[right] >= arr[pivot]:
                right -= 1
            if left > right:
                arr[right], arr[pivot] = arr[pivot], arr[right]
            else:
                arr[left], arr[right] = arr[right], arr[left]

        quick(arr, start, right-1)
        quick(arr, right+1, end)

    arr = list(map(int, input().split()))
    quick(arr, 0, len(arr)-1)

    print(f'#{tc}', *arr)