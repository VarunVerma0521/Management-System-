def bill():
    pcode=int(input('Enter pCode Of Product : '))
    quantity=int(input('Enter Quantity Sold : '))
    import mysql.connector as a
    obj= a.connect(host='localhost',user='root',database='project')
    
    cursor= obj.cursor()
    cursor.execute('select price from stocks where pcode='+str(pcode))
    for i in cursor:
        pr=i
    bill= pr[0]*quantity
    data= (quantity,pcode)
    query='update stocks set quantity= quantity-%s where pcode=%s'
    cursor.execute(query,data)
    obj.commit()
    return bill

def add_item():
    import mysql.connector as a
    obj= a.connect(host='localhost',user='root',database='project')

    pcode= int(input("Enter The pCode For Product : "))
    product= input("Enter Product Name : ")
    price= int(input("Enter The Price : "))
    quantity= int(input("Enter the Quantity : "))

    data=(pcode,product,price,quantity)
    query='insert into stocks values(%s,%s,%s,%s)'
    cursor=obj.cursor()
    cursor.execute(query,data)
    obj.commit()
    print(f'{product} Added Sucessfully')

def update_quantity():
    import mysql.connector as a
    obj= a.connect(host='localhost',user='root',database='project')

    pcd=int(input('pcode? '))
    qua=int(input('Enter New Quantity : '))
    
    data=(qua,pcd)
    query='update stocks set quantity=%s where pcode=%s'
    
    cursor=obj.cursor()
    cursor.execute(query,data)

    obj.commit()
    print('Update Sucessful')

def update_price():
    import mysql.connector as a
    obj= a.connect(host='localhost',user='root',database='project')

    pcd=int(input('pcode? '))
    pr=int(input('Enter New Price : '))
    
    data=(pr,pcd)
    query='update stocks set price=%s where pcode=%s'
    
    cursor=obj.cursor()
    cursor.execute(query,data)

    obj.commit()
    print('Update Sucessful')


print('''
                HEADING
1. Generate Bill
2. Update stocks data''')

choice=int(input("Enter Your Choice : "))

if choice==1 :
    try:
        b=0
        while True: 
            a=bill()
            ques=input("Any More Entry?  ")
            b+= a
            if ques not in ('y','Y'):
                break
        print(f"Amount To Be Recieved : {b}")
    except:
        print("B01:There's some error in database")

if choice==2:
    print('''
    1.Add New Product
    2.Update Stock Quantity
    3.Update Prices ''')
    choice=int(input("Enter Your Choice : "))
    try:
        if choice==1:
            add_item()
    except:
        print("A02:There's Some Error In database ")
    try:
     if choice==2:
        update_quantity()
    except:
        print("U03: There's Some Error In Database")

if choice==3:
    try:
        update_price()
    except:
        print("P04: There's Some Error In Database")
