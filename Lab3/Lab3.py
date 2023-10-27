import pickle as pk 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv

def ex1():
    file = open("raw_text.txt",mode='r')
    raw_data=file.readlines()
    for row in raw_data:
        lines=row.split()
        if lines:
            print(lines[0])
    file.close()

def ex1_4():
    data=pd.read_csv('sampleCSV.csv')
    
    numpydata=data.to_numpy()
    print(numpydata)
    max=numpydata.max()
    min=numpydata.min()
    print(max)
    print(min)
    print(np.shape(numpydata))
    print(np.shape(numpydata)[0])
    print(np.shape(numpydata)[1])
    
def ex1_6():
    data = pd.read_excel('sampleExcel.xlsx')
    numpydata=data.to_numpy()
    max=numpydata.max()
    min=numpydata.min()
    print('max ',max)
    print('min ',min)
    print('shape: ',np.shape(numpydata))
    print('num of rows ',np.shape(numpydata)[0])
    print('num of cols ',np.shape(numpydata)[1])



def ex1_8():
    file=open('samplePickel.pkl', mode='rb')
    data=pk.load(file)
    print(type(data))
    print(len(data))
    print(data[0,0])
    print(data[-1][-1])


def ex2():
    data=np.random.rand(50,30)
    pdData=pd.DataFrame(data)
    print(pdData)
    pdData.to_csv('my_csv_dataset.csv', index=False, header=False)
    pdData.to_excel('my_excel_dataset.xlsx')
    
    
def ex2_4():
    data=np.random.rand(30,70)
    print(type(data))
    list=data.tolist()
    print(type(list))
    file=open('my_pikle_dataset.pkl', mode='wb')
    pk.dump(list,file)
    file.close()


def ex3():
    data=pd.read_csv('traffic_anomaly_lab.csv')
   
    #print(type(data))
    #print(data)
    #print(data.quantile(0.25))
    #Q1,Q2,Q3=data.quantile(0.25,0.5,0.75)
    #print(Q1)
    #print(Q2)
    #print(Q3)
    
    #numpyData=data.to_numpy()
    #q25,q50,q75=np.percentile(numpyData,[25,50,75])
    #datasort=np.sort(data)
    #print(data)
    #IQR=q75-q25
    #print('three q')
    #print(q25,q50,q75)
    #print("IQR 1")
    #print(IQR)
    
    #lowerRange=(q25-1.5*IQR)
    #upperRange=(q75+1.5*IQR)
    #print('lower upper')
    #print(lowerRange, upperRange)

    


    #METHOD 2 

    dataset= pd.read_csv('traffic_anomaly_lab.csv')
    q1= np.quantile(dataset['traffic'],0.25,method= 'nearest')
    q2= np.quantile(dataset['traffic'],0.50,method= 'nearest')
    q3= np.quantile(dataset['traffic'],0.75,method= 'nearest')
 

    print('q1',q1)
    print('q2',q2)
    print('q3',q3)

    iqr=q3-q1
    print('IQR', iqr)
    lRange=q1-1.5*iqr
    
    uRange= q3+1.5*iqr
    print('lower Range: ', lRange)
    print('Upper Range: ', uRange)
    abnormalIndex = np.where((dataset['traffic']>uRange) | (dataset['traffic']<lRange))
    plt.plot(dataset['time'],dataset['traffic'])
    plt.plot(dataset.loc[abnormalIndex,'time'],dataset.loc[abnormalIndex,'traffic'], linestyle='', marker='*')
    plt.legend(['normal traffic','Anomalies'])
    plt.xlabel('Time')
    plt.ylabel('network traffic ')
    plt.title('Anomaly Dectection')
    plt.show()


    print('number of anomalies: ',len(abnormalIndex[0]))


def ex3_2():
    flierprops=dict(marker='o',)
    dataset= pd.read_csv('traffic_anomaly_lab.csv')
    plt.boxplot(dataset['traffic'], flierprops=flierprops)
    plt.ylabel('network traffic ')
    plt.title('Anomaly Dectection')
    plt.show()
    
  



