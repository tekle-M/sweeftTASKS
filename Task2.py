def bigger_Is_greater(a):
    x=list(str(a))[::-1]
    for i in range(len(x)-1):
        if x[i]>x[i+1]:
            for j in range(len(x[:i+1])):              
                if x[j]>x[i+1]:
                    x[i+1],x[j]=x[j],x[i+1]
                    ans=''.join((x[:i+1][::-1]+x[i+1:])[::-1])
                    return ans
                    
    return 'no answer'