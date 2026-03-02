def NextGreaterElement(arr):
    stack = []
    final_ans = []
    for i in range(len(arr)-1 , -1 , -1):
        while(len(stack)>0 and stack[-1] < arr[i]):
            stack.pop()
        if (len(stack)==0):
            final_ans.insert(0 , -1)
            stack.append(arr[i])
        else:
            final_ans.insert(0 , stack[-1])
            stack.append(arr[i])
    return final_ans

arr = list(map(int , input("Enter your Array :- ").split()))
print(NextGreaterElement(arr))
