'''
Created on 12/01/2013

@author: adrian
'''

from django.conf import settings

# import the logging library
import logging
# Get an instance of a logger
logger = logging.getLogger(settings.APP_NAME)

import os
import re


class Contractions:
    def __init__(self):
        contractions_file = os.path.dirname(os.path.realpath(__file__)) 
        contractions_file += os.sep + "contractions.txt" 
        self.contractions_dict = self.get_contractions(contractions_file)
    
    def get_contractions(self, contractions_file):
        logger.info("retrieving contractions")
        lines = open(contractions_file).readlines()
        contractions = []
        for line in lines:
            line = line.strip()
            line = line.lower()
            l = line
            #skip comments and spaces
            if len(l) < 1:
                continue
            if re.match("\s*#",l):
                continue
            #from "what'll    what will; what shall" 
            #get [what'll,what will; what shall]
            l = l.split(" ",1)
            if len(l) < 2:
                logger.warning("line '%s' doesn't contain a valid contraction" % line)
                continue

            #from what'll
            #get [what,ll]
            k = l[0].split("'")
            if len(k) != 2:
                logger.warning("line '%s' doesn't contain a valid contraction" % line)
                continue
            values = l[1].strip().split(";")
            #from "what will; what shall" 
            #get [what will,what shall]
            for v in values:
                v = [x.strip() for x in v.strip().split(" ")]
                if len(v) != 2:
                    logger.warning("line %s doesn't contain a valid contraction" % line)
                    continue
                contractions.append(k+v)
                contractions.append(v+k)
        logger.info("Contractions processed: %s" % len(contractions))
        if logger.level >= logging.DEBUG:
            for c in contractions:
                logger.debug("Contractions: %s" % str(c))
        return contractions
            
