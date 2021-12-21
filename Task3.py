
def bomb(n,li):
    new = [row[:] for row in li]

    for i in range(2,n+1):
        
        
            if i%2==0:
                for j in range(len(li)):
                    for k in range(len(li[j])):
                        if li[j][k]=='.':
                            li[j][k] ='o'
            else:
                for j in range(len(li)):
                    if j>0 and j<(len(li)-1):
                        for k in range(len(li[j])):
                            if k>0 and k<len(li[j])-1:
                                if new[j][k]=='o':
                                    li[j][k],li[j+1][k],li[j-1][k],li[j][k+1],li[j][k-1]='.','.','.','.','.'
                            elif k==0: 
                                if new[j][k]=='o':
                                    li[j][k],li[j+1][k],li[j-1][k],li[j][k+1]='.','.','.','.'
                            else:
                                if new[j][k]=='o':
                                    li[j][k],li[j+1][k],li[j-1][k],li[j][k-1]='.','.','.','.'
                    else:
                        if j==0:
                            for k in range(len(new[j])):
                                if k>0 and k<len(new[j])-1:
                                    if new[j][k]=='o':
                                        li[j][k],li[j+1][k],li[j][k+1],li[j][k-1]='.','.','.','.'
                                elif k==0: 
                                    if new[j][k]=='o':
                                        li[j][k],li[j+1][k],li[j][k+1]='.','.','.'
                                else:
                                    if new[j][k]=='o':
                                        li[j][k],li[j+1][k],li[j][k-1]='.','.','.'
                        else:
                            for k in range(len(new[j])):
                                if k>0 and k<len(new[j])-1:
                                    if new[j][k]=='o':
                                        li[j][k],li[j-1][k],li[j][k+1],li[j][k-1]='.','.','.','.'
                                elif k==0: 
                                    if new[j][k]=='o':
                                        li[j][k],li[j-1][k],li[j][k+1]='.','.','.'
                                else:
                                    if new[j][k]=='o':
                                        li[j][k],li[j-1][k],li[j][k-1]='.','.','.'
                         
                new = [row[:] for row in li]


                                    
                                    
    for j in li:
        print(*j)

li=[list('.......'),list('...o...'),list('....o..'),list('.......'),list('oo.....'),list('oo.....')]
                
bomb(3,li)                                
                                    
