str=""

def seq(dict):
    for i in dict:
        if dict[i]['Type'] == "Task":
            logger.info(str+"."+i+" Entry")
            logger.info(str+"."+i+" Executing TimeFunction ("+dict[i]['Inputs']['FunctionInput']+", "+dict[i]['Inputs']['ExecutionTime']+")")
            logger.info(str+"."+i+" Exit")
        if dict[i]['Type'] == "Flow":
            seq(dict[i]['Activities'])    


import yaml
import logging
from yaml.loader import SafeLoader
logging.basicConfig(filename="output.log",
                    format='%(asctime)s.0000; %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
with open('Milestone1A.yaml') as f:
    data=yaml.load(f,Loader=SafeLoader)
    for i in data:
        k=data[i]
        str=i
        if(k['Type']=="Flow"):
            if(k['Execution']=="Sequential"):
                logger.info(i+" Entry")
                seq(k['Activities'])
                logger.info(i+" Exit")
        elif(k['Type']=="Task"):
            logger.info(i+" Entry")
            logger.info(i+" Executing TimeFunction ("+k['Inputs']['FunctionInput']+", "+k['Inputs']['ExecutionTime']+")")
            logger.info(i+" Exit")
