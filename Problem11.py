def robbery(arr):
    sum1 =0
    sum2 =0
    for i in range(len(arr)):
        if arr[i] < 0:
            i += 1
            continue
        if i % 2 == 0:
            sum1 += arr[i]
        else:
            sum2 += arr[i]

    return max(sum1,sum2)


def robbery2(arr):
    maximum =0
    sums = 0
    for i in range(len(arr)):
        if arr[i] < 0:
            i += 1
            continue
        j = i+1
        sums = arr[i]
        demoMax = 0
        while (j<len(arr)):
            sums += arr[j]
            demoMax = max(demoMax,sums)
            j+=1

    maximum = max(maximum,demoMax)

    return max
         

        

houses =[2,9,1,-3,1]

# print(robbery(houses))
print(robbery2(houses))