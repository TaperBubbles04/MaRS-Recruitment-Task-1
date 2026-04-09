#importing module for ease of calculation of median
import statistics as st

#getting sensor data input
data=list(map(float, input("Enter sensor data separated by commas: ").split(',')))

#Applying muchiko filter method
muchiko=[]
for i in range(len(data)-2):
    w= data[i:i+3]
    wavg=sum(w)/3
    muchiko.append(round(wavg, 2))

#Applying sanchiko filter method
sanchiko=[]
for i in range(len(data)-2):
    w=data[i:i+3]
    wmed= st.median(w)
    sanchiko.append(wmed)

#Applying hybrid method
hybrid=[]
if len(sanchiko)>=3:
    for i in range(len(sanchiko)-2):
        w=sanchiko[i:i+3]
        wavg= sum(w)/3
        hybrid.append(round(wavg, 2))

#displaying output
print("Muchiko Filter Output: ", muchiko)      #better for small fluctuations
print("Sanchiko Filter Output: ", sanchiko)    #gets rid of large random spikes
print("Hybrid Filter Output: ", hybrid)        #helps when both small fluctions and large random spikes are present