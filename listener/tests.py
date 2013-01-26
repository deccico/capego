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
        cor = corrector.Corrector()

        logger.debug("testing contractions")
        for c in cntrc:
            logger.debug("testing contraction: %s" % c)
            correct_line = "%s %s" % (c[0], c[1])
            maybe_correct_line = "%s %s" % (c[2], c[3])
            logger.debug("correct line:'%s' maybe correct:'%s'" % (correct_line, maybe_correct_line))
            is_correct = cor.correct_dialog(correct_line, maybe_correct_line)
            self.assertTrue(is_correct[0], """error in contraction engine or contraction data
            correct line: '%s' check line: '%s'""" % (correct_line, maybe_correct_line))

    def test_contraction_with_comodin(self):
        cor = corrector.Corrector()
        maybe_correct_line = "can't"
        correct_line = "cannot dream"
        logger.debug("correct line:'%s' maybe correct:'%s'" % (correct_line, maybe_correct_line))
        is_correct = cor.correct_dialog(correct_line, maybe_correct_line)
        self.assertTrue(is_correct[0], """error in contraction engine or contraction data
        correct line: '%s' check line: '%s'""" % (correct_line, maybe_correct_line))

    def test_is_preserved(self):
        correct_line = "All right, Gentlemen, I'll take your case. But I'm going to have to ask for a thousand dollar retainer."
        user_input = correct_line
        cor = corrector.Corrector()
        is_correct,out = cor.correct_dialog(correct_line, user_input)
        self.assertTrue(is_correct, "Error correcting %s even when the input and correct line are the same." % correct_line)
        logger.info("user_input: %s corrected: %s" % (user_input, out))
        for c in out:
            for u in user_input.split(" "):
                self.assertEquals(c[1], u, "Correct function does not match with user input in: %s vs %s" % (c[1], u))

        