
def Ex1():
    import pandas as pd
    import numpy as np 
    
    data = pd.read_csv('mini-KDD.csv')
    data=data.to_numpy()
 
    return(data)

def Ex2_3(data):
    import numpy as np
    
    prediction=[]

    for i in range(0,data.shape[0]):

        row = data[i,:]
        if row[0]>0:
            if row[1]<0:
                prediction.append('attack')
            else:
                prediction.append('normal')
        else:
            if row[2]>1:
                prediction.append('attack')
            else:
                prediction.append('normal')
    prediction = np.array(prediction)
    prediction = prediction == 'normal'
    labels = np.array(data[:,-1])
    print('Tree accuracy = ', np.mean(labels==prediction)*100,'%')



def Ex4(data):
    import numpy as np
    
    prediction=[]

    for i in range(0,data.shape[0]):

        row = data[i,:]
        if row[0]>1:
            if row[1]<2:
                prediction.append('attack')
            else:
                prediction.append('normal')
        else:
            if row[2]>1:
                prediction.append('attack')
            else:
                prediction.append('normal')
        
    prediction = np.array(prediction)
    prediction = prediction == 'normal'
    labels = np.array(data[:,-1])
    print('Tree accuracy = ', np.mean(labels==prediction)*100,'%')




def Ex5():
    import pandas as pd
    import numpy as np 
    
    data = pd.read_csv('lab9sol - Copy.csv')
    data=data.to_numpy()
    data=data[1:]
    return(data)

def Ex6(data):
    from sklearn.tree import DecisionTreeClassifier
    import numpy as np 
    from sklearn import tree 
    import matplotlib.pyplot as plt



    model= DecisionTreeClassifier()

    model.fit(data[:,0:-1],data[:,-1])

   # model.predict(data[:,:-1])

    print('Decision Tree model accuracy =', model.score(data[:,0:-1],data[:,-1])*100,'%')

    plt.figure(figsize=(10,8))
    tree.plot_tree(model, filled=True)
    plt.show()

def Ex7(data):
    import pandas as pd
    import numpy as np
    from sklearn.model_selection import train_test_split
    from sklearn.tree import DecisionTreeClassifier
    from sklearn import tree 
    import matplotlib.pyplot as plt
    
    data=data[:100,:100]

    x=data[:,0:-1]
    y=data[:,-1:]
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)

    plt.figure(figsize=(10, 8))
    tree.plot_tree(clf, filled=True)
    plt.show()


#Ex1 
#data=Ex1()
#print(data)

#Ex2 & 3 
#data=Ex1()
#Ex2_3(data)

#Ex4
#data=Ex1()
#Ex4(data)

#Ex5
#data=Ex5()
#print(data)

#Ex6
#data=Ex5()
#Ex6(data)

#Ex7
data=Ex5()
Ex7(data)
