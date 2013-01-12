'''
Created on 12/01/2013

@author: adrian
'''

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

import os
import re


class Contractions:
    def __init__(self):
        contractions_file = os.path.dirname(os.path.realpath(__file__)) 
        contractions_file += os.sep + "contractions.txt" 
        self.contractions_dict = self.get_contractions()
        logging.info("contractions list:\n %s" % self.contractions_dict)
    
    def get_contractions(self, contractions_file):
        lines = open(contractions_file).readlines()
        contractions = {}
        for line in lines():
            l = line.strip()
            if len(l) < 1:
                continue
            if re.match("\s*#",l):
                continue
            l = l.split(" ",2)
            if len(l) < 2:
                logger.warning("line %s doesn't contain a valid contraction" % line)
                continue
            k = l[0].split("'")
            if len(k) != 2:
                logger.warning("line %s doesn't contain a valid contraction" % line)
                continue
            values = l[1].split(";")
            for v in values:
                v = v.split(" ")
                if len(v) != 2:
                    logger.warning("line %s doesn't contain a valid contraction" % line)
                    continue
                #build this entry [aren] = [t,are,not]
                contractions[k[0]] = [k[1], v[0], v[1]]
                #and this entry [are] = [not,aren,t] in order to facilitate searches
                contractions[v[0]] = [v[1], k[0], k[1]]
            
