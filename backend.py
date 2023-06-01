import numpy as np
from sympy.solvers import solve
from sympy import Symbol
import warnings
import pickle



class prediction:

    def __init__(self,input):
        warnings.filterwarnings("ignore")# to ignore warnings while executing our ml models
        val=self.predict(input)
        self.value=val
      
       
    def __int__(self):
        return int(self.value)

    def cs_svm(self,input):
        model_lin=pickle.load(open('trained_SVM.sav', 'rb'))
        cs=model_lin.predict_proba(input)
        return cs
    
    
    
    def cs_gb(self,input):
        gauss_model=pickle.load(open('trained_GB.sav', 'rb'))
        cs=gauss_model.predict_proba(input)
        return cs
    
   


    def cs_nn(self,input):
        MLP=pickle.load(open('trained_NN.sav', 'rb'))
        cs=MLP.predict_proba(input)
        return cs


        

   
    def predict(self,input):
        cs1=self.cs_gb(input)
        cs2=self.cs_svm(input)
        cs3=self.cs_nn(input)
        pred = sugeno([0.8,0.5,0.2],cs1,cs2,cs3)
        return pred
        

def find_max(arr):
    class_0=arr[0]
    class_1=arr[1]

    if class_0>class_1:
        return 0
    elif class_0<class_1:
        return 1
    else:
        return 1
    


def sugeno(solution,pred1,pred2,pred3):
    fuzzymeasures = np.array([solution[0],solution[1],solution[2]])
    l = Symbol('l', real = True)
    lam = solve(  ( 1 + l* fuzzymeasures[0]) * ( 1 + l* fuzzymeasures[1]) *( 1 + l* fuzzymeasures[2]) - (l+1), l )
    if len(lam) < 3:
      lam = np.asarray(lam)
    else:
      if lam[0] >= 0:
          lam = np.asarray(lam[0])
      elif lam[1] >= 0:
          lam = np.asarray(lam[1])
      elif lam[2] >= 0:
          lam = np.asarray(lam[2])
    
    Ypred_fuzzy = np.zeros(shape = pred1.shape, dtype = float)
    for sample in range(0,pred1.shape[0]):
        for classes in range(0,2):
            scores = np.array([pred1[sample][classes],pred2[sample][classes],pred3[sample][classes]])
            permutedidx = np.flip(np.argsort(scores))
            scoreslambda = scores[permutedidx]
            fmlambda = fuzzymeasures[permutedidx]
            ge_prev = fmlambda[0]
            fuzzyprediction = min((scoreslambda[0], fmlambda[0]))
            for i in range(1,3):
                ge_curr = ge_prev + fmlambda[i] + lam * fmlambda[i] * ge_prev
                fuzzyprediction = max((fuzzyprediction,min((scoreslambda[i],ge_curr))))
                ge_prev = ge_curr

            Ypred_fuzzy[sample][classes] = fuzzyprediction
            


   
    ypred_fuzzy = np.argmax(Ypred_fuzzy, axis=1)
    pred_label = []
    for i in ypred_fuzzy:
      label = np.zeros((2))
      label[i] = label[i]+1
      pred_label.append(label)
    pred_label = np.array(pred_label)
    

    sugeno_predict=[]
    for i in range(len(pred_label)):
        arr=[]
        arr=pred_label[i]
        ans=find_max(arr)
        sugeno_predict.append(ans)
        
    
    
    
    return ypred_fuzzy




