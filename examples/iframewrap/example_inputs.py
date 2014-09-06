# example script of using the IframeTracker to interact
# with elements in nested iframes

import logging
import os

import hubcheck
from hubcheck.browser import Firefox
from hubcheck.pageobjects.basepageobject import BasePageObject
from hubcheck.pageobjects.basepageelement import Text
from hubcheck.pageobjects.widgets.iframewrap import IframeWrap


installdir = os.path.dirname(os.path.realpath(__file__))

# setup logging
dc = hubcheck.utils.create_dictConfig('out.log','DEBUG')
logging.config.dictConfig(dc)
logger = logging.getLogger(__name__)

# open a web browser and load our example web page
browser = Firefox()
browser.get('file://'+ os.path.join(installdir,'iframe_example.html'))

# create a page object to hold the widgets
po = BasePageObject(browser,None)
po.locators = { 'frame1' : 'css=#frame1' ,
                'frame2' : 'css=#frame2' ,
                't0'     : 'css=#i0' ,
                't1'     : 'css=#i1' ,
                't2'     : 'css=#i2' , }


# t0 is a widget that represents the text input
# element outside of the first iframe
t0 = Text(po,{'base':'t0'})

# t1 is a widget that represents the text input
# element inside of the first iframe
t1 = IframeWrap( Text(po,{'base':'t1'}),
                 ['frame1'] )

# t2 is a widget that represents the text input
# element inside of the second iframe
t2 = IframeWrap( Text(po,{'base':'t2'}),
                 ['frame2', 'frame1'] )


# print out the current text in the widgets
print "t0.value = %s" % (t0.value)
print "t1.value = %s" % (t1.value)
print "t2.value = %s" % (t2.value)

# update the text in the widgets
t0_new_text = 't0 text'
t1_new_text = 'new t1 text'
t2_new_text = 'new t2 text too'
print "updating t0 to say: %s" % (t0_new_text)
print "updating t1 to say: %s" % (t1_new_text)
print "updating t2 to say: %s" % (t2_new_text)

t0.value = t0_new_text
t1.value = t1_new_text
t2.value = t2_new_text

# print out the new text in the widgets
print "t0.value = %s" % (t0.value)
print "t1.value = %s" % (t1.value)
print "t2.value = %s" % (t2.value)

browser.close()
