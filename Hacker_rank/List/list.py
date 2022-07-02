#Consider a list (list = []). You can perform the following commands:

# 1. insert i e: Insert integer  at position .
# 2. print: Print the list.
# 3. remove e: Delete the first occurrence of integer .
# 4. append e: Insert integer  at the end of the list.
# 5. sort: Sort the list.
# 6. pop: Pop the last element from the list.
# 7. reverse: Reverse the list.
#Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above.
# Iterate through each command in order and perform the corresponding operation on your list.

if __name__ == '__main__':
 N =  int(raw_input())
    list = []
for i in range():
    s = raw_input().split(N)
    for i in range(1,len(s)):
        s[i] = int(s[i])       
    if s[0] == "insert":
        list.insert(s[1],s[2])
    elif s[0] == "append":
        list.append(s[1])
    elif s[0] == "remove":
        list.remove(s[1])
    elif s[0] == "sort":
        list.sort()
    elif s[0] == "pop":
        list.pop()
    elif s[0] == "reverse":
        list.reverse()
    elif s[0] == "print":
        print(list)
