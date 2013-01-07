'''
Created on 01/01/2013

@author: adrian
'''

import re

class Corrector():
    def __init__(self):
        self.WORD_SEP = [" ", ".",",","'"]
        self.re_remove = re.compile("\W")
        self.re_correct = re.compile("^crct(.*)crct$")
        self.EQUIV = {"ll": "will", "m":"am"}
        self.ALL_GOOD = ["oh", "ah", "eh", "mmmh", "oops"]
    
    def correct_dialog(self, good_one, user_input):
        """
        from the user dialog and correct dialog
        returns a list of [[result, user_input_word]..[]]
        """
        good_one = self.strip_signs(good_one)
        user_input = self.strip_signs(user_input)
        out = []
        is_correct = True
        for i in range(len(user_input)):
            wu = self.get_word(user_input[i])   #worduser
            gw = self.get_word(good_one[i])     #goodword
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

    def list_to_string(self, list_line):
        out = ""
        for l in list_line:
            out += l + " "
        return out
    
    #todo: use memoize pattern
    def get_word(self,word):
        return word if word not in self.EQUIV.keys() else self.EQUIV[word]
    
    def format_line(self, line):
        #todo this function
        return self.list_to_string([w[1] for w in line])

    def is_good_contraction(self, user_input, good_one, i):
        wu = self.get_word(user_input[i])
        gw = self.get_word(good_one[i]) 
        next_gw = None if len(good_one) < (i+2) else self.get_word(good_one[i+1]) 
        prev_gw = self.get_word(good_one[i-1]) #we get the same word if len(list) == 1
        next_uw = None if len(user_input) < (i+2) else self.get_word(user_input[i+1])
        prev_uw = self.get_word(user_input[i-1]) #we get the same word if len(list) == 1

        if gw == "shouldn" and wu == "should" and next_uw == "not":
            return True
        if gw == "haven" and wu == "have" and next_uw == "not":
            return True
        if wu == "shouldn" and gw == "should" and next_gw == "not":
            return True
        if wu == "haven" and gw == "have" and next_gw == "not":
            return True
        if wu == "t" and gw == "not" and prev_uw == ["shouldn"] and prev_gw in ["should"]:
            return True
        if wu == "t" and gw == "not" and prev_uw == ["haven"] and prev_gw in ["have"]:
            return True
        if gw == "t" and wu == "not" and prev_gw == ["shouldn"] and prev_uw in ["should"]:
            return True
        if gw == "t" and wu == "not" and prev_gw == ["haven"] and prev_uw in ["have"]:
            return True
        return False
        
        