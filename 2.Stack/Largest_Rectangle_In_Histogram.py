'''84. Largest Rectangle in Histogram   Hard
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.


'''

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = heights
        left_boundary = []
        right_boundary  = []
        stack  = []
        for i in range(len(n)-1 , -1 , -1):
            while(len(stack) > 0 and n[stack[-1]] >= n[i]):
                stack.pop()
            if(len(stack) == 0):
                right_boundary.append(len(n))
                stack.append(i)
            else:
                right_boundary.append(stack[-1])
                stack.append(i)
        stack = []
        for j in range(len(n)):
            while(len(stack) > 0  and n[stack[-1]]>=n[j]):
                stack.pop()
            if(len(stack)==0):
                left_boundary.append(-1)
                stack.append(j)
            else:
                left_boundary.append(stack[-1])
                stack.append(j)
        right_boundary = right_boundary[::-1]
        max_area = 0
        for k in range(len(n)):
            width = right_boundary[k] - left_boundary[k] - 1
            curr_area = width * n[k]
            max_area = max(max_area , curr_area)
        return max_area
arr = list(map(int , input("Enter your Array to find largest Rectangle Area :- ").split()))
c = Solution()
print("Maximum area :- " , c.largestRectangleArea(arr) )   



        
        