Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # ## 1.Write a python function to find max of three numbers.

# In[5]:


def max():
    a=int(input("Enter num1:"))
    b=int(input("Enter num2:"))
    c=int(input("Enter num3:"))
    if a==b==c:
        print("All are equal.No maximum number")
    elif (a>b and a>c):
        print("Maximum number is:",a)
    elif (b>c and b>a):
        print("Maximum number is:",b)
    else:
        print("Maximum number is:",c)
max()      


# ## 2.Write a python program to reverse a string.

# In[6]:


def reverse_string():
    A=str(input("Enter the string:"))
    return A[::-1]
reverse_string()


# ## 3.write a python function to check whether the number is prime or not.

# In[13]:


def prime():
    num=int(input("Enter any number:"))
    if num>1:
        for i in range(2,num):
            if (num%i==0):
                print(num ,"is not a prime number")
                break
        else:
                print(num ,"is a prime number")
    else:
        print(num ,"is not a prime number")
prime()


# ## 4.Use try,except,else and finally block to check whether the number is palindrome or not.

# In[25]:


def palindrome():
    try:
        num=int(input("Enter a number"))
    except Exception as ValueError:
        print("Invalid input enter a integer")
    else:
        temp=num
        rev=0
        while(num>0):
            dig=num%10
            rev=rev*10+dig
            num=num//10
        if(temp==rev):
            print("The number is palindrome")
        else:
            print("Not a palindrome")
            
    finally:
        print("program executed")
palindrome()


# ## 5.Write a python function to find sum of squares of first n natural numbers

# In[27]:


def sum_of_squares():
    n=int(input("Enter the number"))
    return (n*(n+1)*(2*n+1))/6
sum_of_squares()