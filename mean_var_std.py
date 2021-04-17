import numpy as np

def calculate(list):

  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")

  #calc_array = np.array(list)
  calc_matrix = np.array(list).reshape(3,3)

  #print(calc_matrix.mean(axis=0))    does the same...
  #print(np.mean(calc_matrix, axis=0))  ...as this

  #calculations = {
   # "mean": [calc_matrix.mean(axis=0).tolist(), calc_matrix.mean(axis=1).tolist(), np.mean(calc_matrix).tolist()],
    #"variance": [calc_matrix.var(axis=0).tolist(), calc_matrix.var(axis=1).tolist(), np.var(calc_matrix).tolist()],
   # "standard deviation": [calc_matrix.std(axis=0).tolist(), calc_matrix.std(axis=1).tolist(), np.std(calc_matrix).tolist()],
   # "max": [calc_matrix.max(axis=0).tolist(), calc_matrix.max(axis=1).tolist(), np.max(calc_matrix).tolist()],
   # "min": [calc_matrix.min(axis=0).tolist(), calc_matrix.min(axis=1).tolist(), np.min(calc_matrix).tolist()],
   # "sum": [calc_matrix.sum(axis=0).tolist(), calc_matrix.sum(axis=1).tolist(), np.sum(calc_matrix).tolist()]
 # }

  calculations = {
    "mean": [np.mean(calc_matrix, axis=0).tolist(), np.mean(calc_matrix, axis=1).tolist(), np.mean(calc_matrix).tolist()],
    "variance": [np.var(calc_matrix, axis=0).tolist(), np.var(calc_matrix, axis=1).tolist(), np.var(calc_matrix).tolist()],
    "standard deviation": [np.std(calc_matrix, axis=0).tolist(), np.std(calc_matrix, axis=1).tolist(), np.std(calc_matrix).tolist()],
    "max": [np.max(calc_matrix, axis=0).tolist(), np.max(calc_matrix, axis=1).tolist(), np.max(calc_matrix).tolist()],
    "min": [np.min(calc_matrix, axis=0).tolist(), np.min(calc_matrix, axis=1).tolist(), np.min(calc_matrix).tolist()],
    "sum": [np.sum(calc_matrix, axis=0).tolist(), np.sum(calc_matrix, axis=1).tolist(), np.sum(calc_matrix).tolist()]
  }

  return calculations
