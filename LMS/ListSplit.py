def list():
    global bookname
    global authorname
    global quantity
    global cost
    bookname=[]
    authorname=[]
    quantity=[]
    cost=[]
    
    with open("list.txt","r") as books:
        
        lines=books.readlines()
        lines=[x.strip('\n') for x in lines]
        for i in range(len(lines)):
            ind=0
            for a in lines[i].split(','):
                if(ind==0):
                    bookname.append(a)
                elif(ind==1):
                    authorname.append(a)
                elif(ind==2):
                    quantity.append(a)
                elif(ind==3):
                    cost.append(a.strip("$"))
                ind+=1
    print(lines)
    print()

