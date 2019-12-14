theString = input()
if len(theString)/2 != int(len(theString)):
    x = int(((len(theString)-1)/2)-1)
    print(theString[x:x + 3])
elif len(theString)/2 == int(len(theString)):
    y = len(theString)/2
    print(theString[y-2:y+1])
