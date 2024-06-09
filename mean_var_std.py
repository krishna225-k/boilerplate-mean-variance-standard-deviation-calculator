import numpy as np

def calculate(lst):
    calculations={}
    # print('lenght of list is : ',len(lst))
    if len(lst)!=9:
        raise ValueError("List must contain nine numbers.")
    else:
        arr=np.array(lst).reshape((3,3))
        calculations['mean']=[
            arr.mean(axis=0).tolist(),
            arr.mean(axis=1).tolist(),
            np.array(lst).mean()
        ]

        calculations['variance']=[
            arr.var(axis=0).tolist(),
            arr.var(axis=1).tolist(),
            np.array(lst).var()
        ]

        calculations['standard deviation']=[
            arr.std(axis=0).tolist(),
            arr.std(axis=1).tolist(),
            np.array(lst).std()
        ]

        calculations['max']=[
            arr.max(axis=0).tolist(),
            arr.max(axis=1).tolist(),
            np.array(lst).max()
        ]

        calculations['min']=[
            arr.min(axis=0).tolist(),
            arr.min(axis=1).tolist(),
            np.array(lst).min()
        ]

        calculations['sum']=[
            arr.sum(axis=0).tolist(),
            arr.sum(axis=1).tolist(),
            np.array(lst).sum()
        ]


    return calculations