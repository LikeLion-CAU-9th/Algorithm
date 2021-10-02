def solution(s):
    unit=[]
    unitlen=[]

    for i in range(1,len(s)+1):
        split_data=[]
        while 1:
            split_data.append(s[:i])
            s=s[i:]
            if len(s)==0:
                break

        nlist=[]
        for j in range(1000):
            nlist.append(0)

        k=0
        r=len(split_data)-1

        for j in range(r):            
            if split_data[j]==split_data[j+1]:
                nlist[k]=nlist[k]+1
            else:
                k=k+1
                if j==len(split_data)-2:
                    nlist=nlist[:k+1]
        for j in range(len(nlist)):
            nlist[j]=nlist[j]+1

        print(nlist)
        ncomplete=""
        for j in range(len(nlist)):
            if nlist[j]!=1:
                ncomplete=ncomplete+str(nlist[j])+split_data[0]              
            else:
                ncomplete=ncomplete+split_data[0]
               
            split_data=split_data[nlist[j]:]
            
        unit.append(ncomplete)
        for j in range(len(unit)):
            unitlen.append(len(unit[j]))
            
    return min(unitlen)

solution("aaabbc")