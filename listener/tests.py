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
        cor = corrector.Corrector()
        maybe_correct_line = maybe
        correct_line = correct
        logger.debug("maybe correct:'%s' correct line:'%s'" % (maybe_correct_line, correct_line))
        out = cor.correct_dialog(correct_line, maybe_correct_line)
        self.assertTrue(out[0], """error in correction. Correct: '%s' check: '%s' 
        out: %s""" % (correct_line, maybe_correct_line, out))
        correct_line_list = correct_line.split(" ")
        self.assertEquals(len(out[1]), len(correct_line_list),
                          """Correct line has a different length than the output.
                          Correct:%s out:%s
                          """ % (correct_line, out)) 
        for i in range(len(correct_line_list)):
            self.assertEquals(correct_line_list[i], out[1][i][1],
                              """Correct line is different than the output.
                              Correct:%s out:%s. Correct line word:%s output word:%s 
                              """ % (correct_line, out, correct_line_list[i], out[1][i][1])) 
        return out[1]    
    
    def test_mistake(self):
        cor = corrector.Corrector()
        maybe_correct_line = "aren't Great"
        correct_line = "are not grate"
        logger.debug("maybe correct:'%s' correct line:'%s'" % (maybe_correct_line, correct_line))
        out = cor.correct_dialog(correct_line, maybe_correct_line)
        self.assertFalse(out[0], """error in correction correct line: '%s' check 
        line: '%s' out: %s""" % (correct_line, maybe_correct_line, out))
        last_word = maybe_correct_line.split(" ")[-1]
        self.assertEquals(last_word, out[1][-1][1],
                          """incorrect words should be preserved in the same format.
                          user input:%s out:%s. Correct line word:%s output word:%s 
                          """ % (maybe_correct_line, out, last_word, out[1][-1][1])) 
        
        