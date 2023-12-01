import pandas as pd
import numpy as np
import csv
import sklearn

#file = open("KDD_full.csv",mode='r')

def ex1():
    import pandas as pd
    import numpy as np
    import csv
    data = pd.read_csv('KDD_full.csv')
    #print (data)
    return(data)

def ex3():
    import pandas as pd
    import numpy as np
    import csv
    data = ex1()
    max = data['duration'].max()
    #print(max)
   
    x = data['duration']
    
    print(np.min(x))
    print(np.max(x))
    normalized = (x-x.min())/(x.max()-x.min())
    print(normalized)
    print(np.max(normalized))
    data['duration']=normalized
    return(normalized,data)
   

def ex4():
    import pandas as pd
    normalized, data = ex3()
    print("max",normalized.max())
    print("min", normalized.min())

def ex5():
    import numpy as np
    from sklearn.preprocessing import OneHotEncoder
    normalized, data = ex3()
    tcp=np.reshape(data['tcp'].to_numpy(),(-1,1))
    encoder=OneHotEncoder(sparse_output=False)
    result=encoder.fit_transform(tcp)
    #print(result)
    print(data['tcp'])
    data['tcp']=result
    print(result)
    return(data)


def ex6():
    import numpy as np
    from sklearn.preprocessing import OneHotEncoder
    data = ex5()

    label=np.reshape(data['label'].to_numpy(),(-1,1))
    encoder=OneHotEncoder(sparse_output=False)
    result=encoder.fit_transform(label)
    
    print(result)
    data['label']=result
    print(data)



#test = np.array([1,2,3,4,5,6,7,8,9,10,11])
#test -= 5
#print(test)
   

def GibData():
    import pandas as pd
    import numpy as np
    from sklearn.preprocessing import OneHotEncoder

    data = pd.read_csv('KDD_full.csv')
    
    x = data['duration']

    normalized = (x-x.min())/(x.max()-x.min())
   
    data['duration']=normalized
    
  
    tcp=np.reshape(data['tcp'].to_numpy(),(-1,1))

    encoder=OneHotEncoder(sparse_output=False)

    result=encoder.fit_transform(tcp)

    data['tcp']=result
    
    label=np.reshape(data['label'].to_numpy(),(-1,1))
    encoder=OneHotEncoder(sparse_output=False)
    result=encoder.fit_transform(label)
    
    data['label']=result
    
    return(data)

def ex7():
    import pandas as pd
    import numpy as np
    data=GibData()
    data.to_csv('lab9.csv',sep=",",index=False,encoding='utf-8')
ex7()