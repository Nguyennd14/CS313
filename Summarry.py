import pandas as pd
import numpy as np
def Summarry() :
  dataset = pd.read_csv('text.txt', sep=",")
  dataset.head()
  log = open('log.txt', 'w')
  log.write(str(len(dataset)) + '\n')
  len(dataset)
  headers = list(dataset.columns)
  data_length = len(headers)
  log.write(str(data_length) + '\n')
  data_length
  column_types = ""
  for item in headers:
    data_type = 'numeric' if np.issubdtype(dataset[item].dtype, np.number) else 'nominal'
    print(item + ' ' + data_type)
    column_types += item + ' ' + data_type + '\n'
  log.writelines(column_types)
  log.close()
Summarry()