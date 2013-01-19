'''
Created on 01/01/2013

@author: adrian
'''

from django.conf import settings

# import the logging library
import logging
# Get an instance of a logger
logger = logging.getLogger(settings.APP_NAME)

import re

import listener

class Corrector():
    def __init__(self):
        self.WORD_SEP = [" ", ".",",","'"]
        self.re_remove = re.compile("\W")
        self.re_correct = re.compile("^crct(.*)crct$")
        self.ALL_GOOD = ["oh", "ah", "eh", "mmmh", "oops"]
        self.CONTRACTION_ALL_GOOD = "crctcrct"
        self.contractions = listener.contractions
    
    def correct_dialog(self, good_one, user_input):
        good_one = self.strip_signs(good_one)
        user_input = self.strip_signs(user_input)
        out = []
        is_correct = True
        for i in range(len(user_input)):
            wu = user_input[i]   #worduser
            gw = good_one[i]     #goodword
            if gw in self.ALL_GOOD:
                out.append([True, gw])
            else:
                r=self.re_correct.match(gw)
                if r:
                    out.append([True, r.group(1)])
                elif self.is_good_contraction(user_input, good_one, i):
                    out.append([True, wu])
                else:
                    result = (wu==gw)        
                    out.append([result, wu])
                    is_correct = is_correct and result        
        #add an incomplete mark to the user input
        if len(user_input) < len(good_one):
            out.append([False,""])
            is_correct = False 
        return is_correct,out 
    
    def strip_signs(self, line):
        lines = self.re_remove.split(line)
        lines = [l.lower() for l in lines if len(l)>0] 
        return lines

    
    def is_good_contraction(self, user_input, good_one, i):
        logger.debug("user_input:%s, good_on:%s, i:%s" % (user_input, good_one, i))
        wu = user_input[i]
        gw = good_one[i] 
        next_gw = None if len(good_one) < (i+2) else good_one[i+1] 
        prev_gw = good_one[i-1] #we get the same word if len(list) == 1
        next_wu = None if len(user_input) < (i+2) else user_input[i+1]
        prev_wu = user_input[i-1] #we get the same word if len(list) == 1
        
        #verify if the contraction has the structure:
        #[aren] = [t,are,not] or
        #[are] = [not,aren,t]
        to_check = [[wu, next_wu, gw, next_gw],
                    [gw, next_gw, wu, next_wu],
                    [prev_wu, wu, prev_gw, gw],
                    [prev_gw, gw, prev_wu, wu]
                    ]
        ctrc = self.contractions 
        for chk in to_check:
            for con in ctrc:
                logger.debug("checking '%s' vs '%s'" % (chk, con))
                if chk == con:
                    return True
                if self.CONTRACTION_ALL_GOOD in con:
                    is_good=True
                    for i in range(len(to_check)):
                        if chk[i] != con[i] and con[i]!=self.CONTRACTION_ALL_GOOD:
                            is_good=False
                    if is_good:
                        return True 
        return False

    def correct_next_word(self, good_one, user_input):
        is_correct,out = self.correct_dialog(good_one, user_input)
        good_one = self.strip_signs(good_one)
        for i in range(len(out)):
            if not out[i][0]:
                out[i] = [True, self.get_good_word(good_one[i])]
                break
        is_correct = out[-1][0] and len(out) == len(good_one)
        if not is_correct:
            out.append([False,""])
        return is_correct,out

    def get_good_word(self, good_word):
        r=self.re_correct.match(good_word)
        return r.group(1) if r else good_word
        