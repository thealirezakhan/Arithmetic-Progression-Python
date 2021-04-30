t1 = int(input("First term of the A.P. : "))
t2 = int(input("Second term of the A.P. : "))
t3 = int(input("Third term of the A.P. : "))
n = int(input("Which term do you want to find?: "))

D1 = t2 - t1 
D2 = t3 - t2
a = t1 



def find_difference():
    if  D1 == D2:
        print("It is an A.P. ")

    else:
        return None    

def find_nth_term():
    tn = a+(n-1)*D1
    print(tn)

if __name__ == "__main__":
    find_difference()
    find_nth_term()