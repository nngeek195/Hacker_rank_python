if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    array = []
    array = list(arr)
    array.sort()
    i = 0
    while n-i >= 0:
        if array[n-1] != array[n-1-i]:
            print(array[n-1-i])
            break
        i+=1
        
                
