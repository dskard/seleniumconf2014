# example script of using the IframeTracker to interact
# with elements in nested iframes

import logging
import os

import hubcheck
#from hubcheck.browser import Firefox

from framed_inputs import FramedInputs


installdir = os.path.dirname(os.path.realpath(__file__))

# setup logging
dc = hubcheck.utils.create_dictConfig('out.log','DEBUG')
logging.config.dictConfig(dc)
logger = logging.getLogger(__name__)

# open a web browser and load our example web page
browser = hubcheck.browser.Firefox()
browser.get('file://'+ os.path.join(installdir,'iframe_example.html'))

# create a page object to hold the widgets
po = FramedInputs(browser)

# print out the current text in the widgets
print "t0.value = %s" % (po.i0.value)
print "t1.value = %s" % (po.i1.value)
print "t2.value = %s" % (po.i2.value)

# update the text in the widgets
t0_new_text = 't0 text'
t1_new_text = 'new t1 text'
t2_new_text = 'new t2 text too'
print "updating t0 to say: %s" % (t0_new_text)
print "updating t1 to say: %s" % (t1_new_text)
print "updating t2 to say: %s" % (t2_new_text)

po.i0.value = t0_new_text
po.i1.value = t1_new_text
po.i2.value = t2_new_text

# print out the new text in the widgets
print "t0.value = %s" % (po.i0.value)
print "t1.value = %s" % (po.i1.value)
print "t2.value = %s" % (po.i2.value)

browser.close()
