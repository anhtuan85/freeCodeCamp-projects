import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
  calculations = {}
  calculations["mean"] = []
  calculations["variance"] = []
  calculations["standard deviation"] = []
  calculations["max"] = []
  calculations["min"] = []
  calculations["sum"] = []
  arr = np.array(list).reshape((3, 3))

  #Caculate mean
  calculations["mean"].append(np.mean(arr, axis= 0).tolist())
  calculations["mean"].append(np.mean(arr, axis= 1).tolist())
  calculations["mean"].append(np.mean(arr))

  #Caculate variance
  calculations['variance'].append(np.var(arr, axis= 0).tolist())
  calculations['variance'].append(np.var(arr, axis= 1).tolist())
  calculations['variance'].append(np.var(arr))

  #Calculate std 
  calculations['standard deviation'].append(np.std(arr, axis= 0).tolist())
  calculations['standard deviation'].append(np.std(arr, axis= 1).tolist())
  calculations['standard deviation'].append(np.std(arr))

  #Calculate max
  calculations['max'].append(np.amax(arr, axis= 0).tolist())
  calculations['max'].append(np.amax(arr, axis= 1).tolist())
  calculations['max'].append(np.amax(arr))

  #Calculate min
  calculations['min'].append(np.amin(arr, axis= 0).tolist())
  calculations['min'].append(np.amin(arr, axis= 1).tolist())
  calculations['min'].append(np.amin(arr))

  #Calculate sum
  calculations['sum'].append(np.sum(arr, axis= 0).tolist())
  calculations['sum'].append(np.sum(arr, axis= 1).tolist())
  calculations['sum'].append(np.sum(arr))
  return calculations