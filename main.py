import yaml
import logging
from yaml.loader import SafeLoader
logging.basicConfig(filename="output.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
with open('Milestone1A.yaml') as f:
    data=yaml.load(f,Loader=SafeLoader)
    for i in data:
        logger.info(i)
    k=data['M1A_Workflow']
    h=k['Activities']
    l=list(data)
    for i,j in h.items():
        logger.info(i)








