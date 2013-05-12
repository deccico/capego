from django.conf import settings

import logging
logger = logging.getLogger(settings.APP_NAME)

import re

import listener

class Corrector():
    def __init__(self):
        self.WORD_SEP = [" ", ".",",","'"]
        self.re_remove = re.compile("\W")
        self.correct = "crct"
        self.re_correct = re.compile("^%s(.*)%s$" % (self.correct, self.correct))
        self.ALL_GOOD = ["oh", "ah", "eh", "mmmh", "oops"]
        self.CONTRACTION_ALL_GOOD = "%s%s" % (self.correct, self.correct)
        self.contractions = listener.contractions
        self.EQUALITIES = {"geez": "jeez", "jeez": "geez",   #TODO: this should be loaded from a file
                           "okay": "ok", "ok": "okay",
                           "okey": "ok", "ok": "okey",
        }
    
    def correct_dialog(self, good_one, user_input):
        #todo: eventually we may need to split in "." and ","
        #todo: without spaces but keeping the signs
        good_one = good_one.strip()
        user_input = user_input.strip()
        rgo, rui = good_one, user_input
        good_one = good_one.split()
        user_input = user_input.split()
        
        out = []
        is_correct = True
        offset = [0,0]
        for i in range(len(user_input)):
            if (i+offset[0]) >= len(user_input):
                break  
            if (i+offset[1]) >= len(good_one):
                break  
            wu = self.get_word(user_input[i+offset[0]])   #worduser
            gw = self.get_word(good_one[i+offset[1]])     #goodword
            raw_word_user = user_input[i+offset[0]].strip()
            raw_good_one = good_one[i+offset[1]].strip()
            logger.debug("wu/gw %s vs %s" % (wu,gw))
            if gw in self.ALL_GOOD:
                out.append([True, raw_good_one])
                logger.debug("it's an all good word")
                continue
            if gw in self.EQUALITIES.keys() and self.EQUALITIES[gw] == wu:
                out.append([True, raw_good_one])
                logger.debug("is an equality")
                continue
            r=self.re_correct.match(gw)
            if r:
                out.append([True, self.strip_all_good_mark(raw_good_one)])
                logger.debug("it has the good mark")
                continue
            is_contraction = self.is_good_contraction(user_input, good_one, i, offset)
            if is_contraction[0]:
                out.append([True, raw_good_one])
                logger.debug("is a good contraction")
                offset[0] += is_contraction[1][0]
                offset[1] += is_contraction[1][1]
                if is_contraction[1] == [0,1]: #add the offsetted word
                    out.append([True, good_one[i+offset[1]]])
                continue
            result = (wu==gw)        
            out.append([result, raw_good_one if result else raw_word_user])
            is_correct = is_correct and result        
            logger.debug("is correct? %s" % result)

        #add an incomplete mark to the user input
        if len(self.strip_signs(rui)) < len(self.strip_signs(rgo)):
            is_correct = False
            out.append([False,""])
        return is_correct,out
        
    def strip_signs(self, line):
        lines = self.re_remove.split(line)
        lines = [l.lower() for l in lines if len(l)>0] 
        return lines

    def get_word(self, word):
        return None if word==None else self.re_remove.sub("", word).lower() 
    
    def strip_all_good_mark(self, word):
        return word.replace(self.correct,"")
        
    def is_good_contraction(self, user_input, good_one, iw, offset):
        logger.debug("user_input:%s, good_on:%s, iw:%s offset %s" % (user_input, good_one, iw, offset))
        jw = iw + offset[1]
        iw += offset[0]
        
        #check match in the first word 
        wu = user_input[iw].split("'",1)
        gw = good_one[jw].split("'",1)
        next_wu = None if len(user_input) < (iw+2) else self.get_word(user_input[iw+1])
        next_gw = None if len(good_one) < (jw+2) else self.get_word(good_one[jw+1]) 

        if next_wu==None and self.get_word(wu[0]) == self.get_word(gw[0]):
            offset = [0,0]
            if len(wu)>len(gw):
                offset = [0,1]
            return True,offset 
        
        wu = self.get_word(user_input[iw])
        gw = self.get_word(good_one[jw]) 
        
        to_check = [[wu, gw, next_gw, [0,1]],
                    [gw, wu, next_wu, [1,0]],
                    ]
        logger.debug("to_check %s" % to_check)
        
        for contraction in self.contractions:
            logger.debug("iterating over contraction: %s" % contraction)
            for check in to_check:
                logger.debug("iterating over check: %s" % check)
                is_correct = True
                for i in range(len(contraction)):
                    logger.debug("comparing: %s / %s" % (self.get_word(contraction[i]),self.get_word(check[i])))
                    if self.get_word(contraction[i]) != self.get_word(check[i]):
                        if contraction[i] != self.CONTRACTION_ALL_GOOD:
                            is_correct = False
                            break
                        else:
                            #a special case requires a special offset
                            check[-1] = [0,0]                     
                if is_correct:
                    return True,check[-1] 
        return False,[0,0]
            
    def get_next_word(self, good_one, user_input):
        out = self.correct_dialog(good_one, user_input)[1]
        good_one = good_one.split()
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
        