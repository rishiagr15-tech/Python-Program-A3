#18. Find missing number in a list

def missing_number():
    n=int(input("Enter the number of elements in the list:\n"))
    lst=[]
    for i in range(n):
        x=int(input("Enter the integer:\n"))
        lst.append(x)
    lst.sort()
    print("The list is:\t",lst)
    for i in range(lst[0],lst[-1]):
        if i not in lst:
            print("The missing number in the list is:\t",i)
            break

if __name__ == "__main__":
    missing_number()