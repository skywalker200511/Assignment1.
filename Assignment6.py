def ds(rollno,name):
    ls = [rollno,name]
    tp = (rollno,name)
    dt = {"rollno":rollno,"name":name}
    st = {rollno,name}
    print("\n\nBefore changes=\n")
    print(ls)
    print(tp)
    print(dt)
    print(st)
    ls[0] = 20
    ls[1] = "Student"
    tp = (20,"Student")
    dt.update({"rollno":20,"name":"Student"})
    st = {20,"Student"}
    print("\nAfter changes=\n")
    print(ls)
    print(tp)
    print(dt)
    print(st)
    
    del ls
    del tp
    del dt
    del st
nm = input("Enter name=")
rol = int(input("Enter rollno="))
ds(rol,nm)
    
