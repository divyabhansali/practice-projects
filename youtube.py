# ##Concept : Extraction of digits
# # 1) Count the number of digits in the integer
# # # Method 1 -
# # n = int(input())

# # num = n
# # count = 0
# # while num > 0:
# #     num = num // 10
# #     count +=1
# # print(count)

# # # Method 2
# # from math import *
# # n= int(input())
# # print(int(log10(n)+1))

# #2) Check Palindrome TC: O(log10(N)) where N is number , not number of digits; SC: O(1) as we are taking constant and that is not dependent on size of number
# # n = int(input())

# # num = n
# # summ = 0
# # while num>0:
# #     ld = num%10
# #     num = num // 10
# #     summ = summ * 10 + ld

# # if n == summ:
# #     print("The number is palindrome")
# # else:
# #     print("The nummber is not palindrome")

# #3) Check Armstrong number: 153 = 1**3 + 5**3 + 3**3 TC : O(log10(N)) N is the number, SC: O(1)

# # n = int(input())
# # total = 0
# # nod =  len(str(n)) #number of digit
# # num = n

# # while num > 0:
# #     ld = num % 10
# #     num = num // 10
# #     total = total + ld ** nod

# # if n == total:
# #     print(" It is Armstrong")
# # else:
# #     print("Not an Armstrong") 

# # Concept: All Prime numbers of given number
# # # Method 1: TC: O(N), SC: O(k)
# # n = int(input())
# # result = []
# # for i in range(1, n+1):
# #     if n% i == 0:
# #         result.append(i)
# # print(result)

# # # Method 2: TC: O(N/2) ~ O(N) , SC: O(k)
# # n = int(input())
# # result = []
# # for i in range(1, n//2 + 1): # Use // because we want to convert remainder into integer
# #     if n% i == 0:
# #         result.append(i)
# # result.append(n)
# # print(result)

# # #Method 3: from sqrt function TC: O(N**2)+O(NlogN) ; SC: O(k)
# # from math import *
# # n = int(input())
# # result = []

# # for i in range(1,int(sqrt(n))+1):
# #     if n%i == 0:
# #         result.append(i)
# #         if n // i != i:
# #             result.append(n//i)
# # result.sort()  #TC: O(N*logN)
# # print(result)

# #Concept: Frequency in dictionary
# # # Method 1:
# # h ={}
# # n = [1,3,4,5,1,3,4,6,7,3,5,6,2,3]

# # for i in range(len(n)):
# #     if n[i] in h:
# #         h[n[i]]+=1
# #     else:
# #         h[n[i]] = 1

# # print(h)

# # # Method 2:
# # h = {}
# # n = [1,3,4,5,1,3,4,6,7,3,5,6,2,3]
# # for i in range(len(n)):
# #     h[n[i]] = h.get(n[i],0)+1

# # print(h)

# # Concept: Number Hashing - Prestoring values into some datastructure like List/ Set/ Dictionary and fetching it
# # Q1: Constraints - 1)1<=n[i]<=10, 2)n can have 10*8 elements, 3)m can have 10*8 elements
# # n = [5,3,2,2,1,5,5,7,1,5,10]  
# # m = [10, 111, 1, 9, 5, 67, 2] 
# # # Method 1: Two for loop TC: O(n*m);  SC:O(1)
# # d = {}
# # for num in m:
# #     count = 0
# #     for i in n:
# #         if num == i:
# #             count + = 1
# #     print(count)

# # # Method 2: Optimal considering the numbers in n should be between 1 to 10 TC: O(n+m); SC: O(11) - constant

# # hash_list = [0] * 11
# # for num in n:
# #   hash_list[num] += 1

# # for i in m:
# #   if i < 1 or i>10:
# #     print("Not exist")
# #   else:
# #     print(hash_list[i])

# # # Method 3: Using Dictionary
# # d = {}
# # for i in n:
# #     if i in d:
# #         d[i] += 1
# #     else:
# #         d[i] = 1
# # print(d)
# # for j in m:
# #     if j in d:
# #         print(d.get(j))
# #     else:
# #         print(0)

# # #Concept: Character hashing
# # s = "azxyyayzyyyaa"
# # q = ['d','a','x','y']

# # l = [0] * 26
# # for ch in s:
# #     ascii_val = ord(ch)
# #     index = ascii_val - 97
# #     l[index] += 1
# # for ch in q:
# #     ascii_val = ord(ch)
# #     index = ascii_val - 97
# #     print(l[index])  

# #Concept : Recursion
# #Question : Print 1 to n numbers
# # #Method 1: Head Recursion 
# # def func(i,n):
# #     if i > n:
# #         return
# #     print(i)
# #     func(i+1,n)

# # func(1,4)

# # #Method 2: Tail Recursion/ Back Tracking
# # def func(i,n):
# #     if i > n:
# #         return
# #     func(i+1,n)
# #     print(i)

# # func(1,4)

# #Concept : Functional Recursion TC: O(N); SC: O(N) stack space
# # #func(10) = 10+9+8+7+6..+1 = 55

# # def func(n):
# #     if n == 1:
# #         return 1
# #     return n + func(n-1)

# # print(func(4))

# # #Question : 1 Factorial TC = O(n); SC = O(n) stack space
# # #1) Flow
# # #2) Base case

# # def fac(n):
# #     if n <=1:
# #         return 1
# #     return n * fac(n-1)

# # print(fac(4))

# # Question 2: Reverse an array using recursion
# # num = [5,7,3,2,6,1,5,9] 
# # (a) left = 2 ; right = 5

# # def func(nums, left, right):
# #     if left >= right:
# #         return
# #     nums[left], nums[right] = nums[right], nums[left]
# #     func(nums, left +1, right-1)
    
# # func(num,2,5)
# # print(num)

# # (b) left = 0 ; right = 7 ; TC : O(N/2), Sc: O(N/2) - stack space

# # def func(nums, left, right):
# #     if left >= right:
# #         return
# #     nums[left], nums[right] = nums[right], nums[left]
# #     func(nums, left + 1, right -1)

# # func(num, 0, 7)
# # print(num)


# # Question 2: Check if a string is palindrome or not:
# # Method 1: Loop -  TC: O(N/2) - jitni baar loop chala ; SC: O(1)
# # s = 'anitina'
# # l = 0
# # r = len(s) -1
# # b = True
# # while l < r:
# #     if s[l] != s[r]:
# #         b = False
# #     l += 1
# #     r -= 1
# # print(b)

# #Method 2: Recursion TC: O(N/2) ~ O(n); SC : O(N/2) - stack space
# # def func(s,l,r):
# #     if l >= r:
# #         return True
# #     if s[l]!= s[r]:
# #         return False
# #     return func(s,l+1,r-1)

# # h = func(s,0,len(s)-1)
# # print(h)

# # Question 3: Fibonacci - 0 1 1 2 3 5 8 13 21 34 - f(7) = f(6) + f(5)  TC : O(2^n) ; SC: O(2^n)
# # def func(num):
# #     if num == 0 or num == 1:
# #         return num
    
# #     return func(num-1) + func(num-2)

# # s = func(8)
# # print(s)

# #Concept : Sorting Algorithm take i,,min_index  
# # Selection Sort - TC : O(n*(n+1)/2) ~ O(n^2) ; Sc: O(1)


# # def selec(nums):
# #     n = len(nums)
# #     for i in range(0,n):
# #         min_index = i
# #         for j in range(i+1,n):
# #             if nums[j] < nums[min_index]:
# #                 min_index = j
# #         nums[i],nums[min_index] = nums[min_index], nums[i]
# #     return nums

# # selec(nums)
# # print(nums)

# # Bubble Sort [Adjacent Swap] - in-place  - TC : O(n*(n+1)/2) ~ O(n^2) ; Sc: O(1)

# # def bubble(nums):
# #     n = len(nums)
# #     is_swap = False  # If the list is already sorted and we need to avoid the iteration- best case TC: O(n) ; SC : O(1)
# #     for i in range(n-2, -1,  -1):
# #         for j in range(0,i+1):
# #             if nums[j+1] < nums[j]:
# #                 nums[j+1], nums[j] = nums[j], nums[j+1]
# #                 is_swap = True
# #     if is_swap == False:
# #          return

# # bubble(nums)    
# # print(nums)

# # Insertion sort - TC: O(n*(n+1)/2) ~ O(n^2); SC:O(1)
# nums = [9,5,1,2,8,6,4,7]

# # def insertion(nums):
# #     for i in range(1,len(nums)):
# #         key = nums[i]
# #         j = i-1
# #         while j>=0 and nums[j]> key:
# #             nums[j+1] = nums[j]
# #             j = j-1
# #         nums[j+1] = key
# # insertion(nums)
# # print(nums)

# # Merge Sort [Divide and Merge] -