def twoNumberSum(array, targetSum):
    # Write your code here.
    for i in range(0,len(array)):
        for j in range(i,len(array)):
            if array[i]+array[j] == targetSum and array[i] != array[j]:
                return [array[i],array[j]]
    return []
		
if __name__ == "__main__":
    array = [3,5,-4,8,11,1,-1,6]
    targetSum = 10
    result = twoNumberSum(array,targetSum)
    print(result)
