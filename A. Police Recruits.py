
def solve(l):
    plice = 0
    cremenal = 0
    for i in l:
        if i<0:
            if plice>0:
             plice-=1   
            else:
             cremenal+=1         
        else:
            plice+=i
    print(cremenal) 
if __name__ == "__main__":
    solve(l=[])