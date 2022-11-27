import numpy as np

def calculate(list):
  if len(list)<9:
    raise ValueError("List must contain nine numbers.")
  calculations={}
  row1=np.array(list[:3])
  row2=np.array(list[3:6])
  row3=np.array(list[6:])
  matrix=np.array((row1,row2,row3))

  print(matrix)
  matrix_mean=[ np.mean(matrix,axis=0).tolist(), np.mean(matrix,axis=1).tolist(), np.mean(matrix).tolist() ]
  matrix_var=[ np.var(matrix,axis=0).tolist(), np.var(matrix,axis=1).tolist(), np.var(matrix).tolist() ]
  matrix_std=[ np.std(matrix,axis=0).tolist(), np.std(matrix,axis=1).tolist(), np.std(matrix).tolist() ]
  matrix_max=[ np.max(matrix,axis=0).tolist(), np.max(matrix,axis=1).tolist(), np.max(matrix).tolist() ]
  matrix_min=[ np.min(matrix,axis=0).tolist(), np.min(matrix,axis=1).tolist(), np.min(matrix).tolist() ]
  matrix_sum=[ np.sum(matrix,axis=0).tolist(), np.sum(matrix,axis=1).tolist(), np.sum(matrix).tolist() ]
  
  # fill results dictionary
  calculations["mean"]=matrix_mean
  calculations["variance"]=matrix_var
  calculations["standard deviation"]=matrix_std
  calculations["max"]=matrix_max
  calculations["min"]=matrix_min
  calculations["sum"]=matrix_sum
  
  return calculations


# result=calculate([2,6,2,8,4,0,1,5,7])
# print(result)