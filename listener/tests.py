"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.conf import settings

# import the logging library
import logging
# Get an instance of a logger
logger = logging.getLogger(settings.APP_NAME)

from django.test import TestCase

import listener
import corrector


class ListenerTest(TestCase):
    
    def test_contractions(self):
        """
        Test contractions.
        """
        cntrc = listener.contractions
        logger.debug("testing contractions")
        is_kv = True
        for c in cntrc:
            if is_kv:
                correct_line = "%s" % (c[0])
                maybe_correct_line = "%s %s" % (c[1], c[2])
                is_kv = False
            else:
                correct_line = "%s %s" % (c[0], c[1])
                maybe_correct_line = "%s" % (c[2])
                is_kv = True    
            logger.debug("correct line:'%s' maybe correct:'%s'" % (correct_line, maybe_correct_line))
            self.try_correction(maybe_correct_line, correct_line)
    
    def test_cannot_contraction(self):
        self.try_correction("can't dream", "cannot dream")

    def test_cannot(self):
        self.try_correction("can't", "can not")

    def test_you_have(self):
        self.try_correction("listen you've to", "listen you Have to")

    def test_you_have_to_listen(self):
        self.try_correction("you've to listen", "you Have to Listen")

    def test_have_you(self):
        self.try_correction("You Have", "You've")

    def test_arent_contraction(self):
        self.try_correction("aren't", "are not")

    def test_long_sentence(self):
        correct_line = "All right, Gentlemen, I'll take your case. But I'm going to have to ask for a thousand dollar retainer."
        user_input = correct_line
        self.try_correction(user_input, correct_line)
    
    def try_correction(self,maybe, correct):
        out = self.correct(correct, maybe)
        self.assertTrue(out[0], """error in correction. Correct: '%s' check: '%s' 
        out: %s""" % (correct, maybe, out))
        correct_line_list = correct.split(" ")
        self.assertEquals(len(out[1]), len(correct_line_list),
                          """Correct line has a different length than the output.
                          Correct:%s Maybe:%s out:%s
                          """ % (correct, maybe, out)) 
        for i in range(len(correct_line_list)):
            self.assertEquals(correct_line_list[i], out[1][i][1],
                              """Correct line is different than the output.
                              Correct:%s out:%s. Correct line word:%s output word:%s 
                              """ % (correct, out, correct_line_list[i], out[1][i][1])) 
        return out[1]    
    
    def correct(self, correct, maybe_correct):
        cor = corrector.Corrector()
        logger.debug("maybe correct:'%s' correct line:'%s'" % (maybe_correct, correct))
        return cor.correct_dialog(correct, maybe_correct)
    
    def test_mistake(self):
        maybe_correct_line = "aren't Great"
        correct_line = "are not grate"
        out = self.correct(correct_line, maybe_correct_line)
        self.assertFalse(out[0], """error in correction correct line: '%s' check 
        line: '%s' out: %s""" % (correct_line, maybe_correct_line, out))
        last_word = maybe_correct_line.split(" ")[-1]
        self.assertEquals(last_word, out[1][-1][1],
                          """incorrect words should be preserved in the same format.
                          user input:%s out:%s. Correct line word:%s output word:%s 
                          """ % (maybe_correct_line, out, last_word, out[1][-1][1]))
    
    def test_incomplete_correction(self):
        correct = "All right, Gentlemen, I'll take your case. But I'm going to have to ask for a thousand dollar retainer." 
        maybe_correct = "all right"
        out = self.correct(correct, maybe_correct)
        self.assertFalse(out[0], "Output should be wrong. %s" % str(out))
        
    def test_tst_spaces(self):
        self.try_correction("hi    There", "Hi there")

    def test_tst_without_spaces(self):
        self.try_correction("hi There", "Hi there")
        
    def test_skipping_signs(self):
        maybe = r"All right, Gentlemen, I'll take your case. But I'm going to have to ask for a thousand dollar retainer" 
        correct = maybe + "." 
        self.try_correction(maybe, correct)

    def test_partial_contraction(self):
        correct = "I'll" 
        maybe = "I"
        out = self.correct(correct, maybe)
        self.assertTrue(out[1][0][0], "First word should be correct. %s Correct: %s Maybe: %s" 
                        % (str(out), correct, maybe))
    
    def test_get_next_word(self):
        correct = "All right, Gentlemen, I'll take your case. But I'm going to have to ask for a thousand dollar retainer." 
        lcorrect = correct.split()
        cor = corrector.Corrector()
        for i in range(len(lcorrect)):
            maybe = (" ").join(lcorrect[:i])
            out = cor.get_next_word(correct, maybe)
            msg = "i:%s Maybe:%s out:%s Correct:%s " % (i,maybe,out,correct)
            for j in range(i+1):
                self.assertEquals(lcorrect[j], out[1][j][1], "incorrect next word. " + msg)
                 
    def test_correct_extreme(self):
        maybe = "All right, gentlemen I will take your case but i am going to have to ask for a thousand dollar retainer"
        correct = "All right, Gentlemen, I'll take your case. But I'm going to have to ask for a thousand dollar retainer."        
        self.correct(correct, maybe)                     

        