#19. Find duplicate elements in a list

def find_duplicates():
    n=int(input("Enter the number of elements in the list:\n"))
    lst=[]
    for i in range(n):
        x=int(input("Enter the integer:\n"))
        lst.append(x)
    print("The list is:\t",lst)
    d=[]
    for i in lst:
        if lst.count(i)>1 and i not in d:
            d.append(i)
    print("The duplicate elements in the list are:\t",d)

if __name__ == "__main__":
    find_duplicates()