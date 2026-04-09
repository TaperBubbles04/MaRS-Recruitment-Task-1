#getting the inputs
lim=input("Enter Limits: ")
lim=list(map(int, lim[1:len(lim)-1].split(', ')))

wfac= input("Enter Wear Factors: ")
wfac=list(map(int, wfac[1:len(wfac)-1].split(', ')))

targ= input("Enter Targets: ")
targ= list(map(int, targ[1:len(targ)-1].split(', ')))

d=int(input("Enter D: "))

#assigning the different weights and limits to different variables
l1, l2, l3 =lim
w1, w2, w3 =wfac

wcost={(0, 0, 0): 0}

#computing the configuration for each target
for t in targ:
    nw={}
    for i in range(l1+1):
        for j in range(l3+1):
            m= t-i-j
            if 0<=m<=l2 and abs(i-j)<=d:
                minc= float('inf')                  #ensures that the first value is always smaller as we store the minc value as infinity
                for(pi, pm, pj), pc in wcost.items():
                    cost= pc+abs(i-pi)*w1+abs(m-pm)*w2+abs(j-pj)*w3    #calculating with change in configuration
                    if cost<minc:
                        minc=cost
                if minc!=float('inf'):
                    nw[(i, m, j)]=minc
    wcost=nw

print(min(wcost.values()))      #displaying the minimum total wear cost