import os
from fastapi import FastAPI
import requests
import json
app = FastAPI()
IVR_method = os.environ['IVR_method']
IVR_login = os.environ['IVR_login']
IVR_psw= os.environ['IVR_psw']
IVR_address = os.environ['IVR_address']
@app.post("/")
def read_root(NUMBER: str,
              NAME:str| None = None,
              ID: int| None = 0,COMMENT: str| None = None,
              ):
    answ = callIVR(NUMBER,ID,NAME)
    return {"data": answ}
    
def callIVR(NUMBER,ID:int=0,NAME):
    print('start call:', NUMBER,ID)
    session = requests.Session()
    session.auth = (IVR_login, IVR_psw)
    call_data = {
        "method":IVR_method,
        "data":{"NUMBER":NUMBER,"ID":ID,"NAME":NAME}
    }
    answ = session.post(IVR_address,json=call_data)
    answ.close()
    return('mtt close connection')

