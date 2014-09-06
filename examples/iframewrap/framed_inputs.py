# page object class for the example_input.html web page.
# uses IframeWrap() to decorate methods of the page objects
# representing input text boxes located inside of iframes,
# with calls to enter and exit the iframes as needed.

from hubcheck.pageobjects.basepageobject import BasePageObject
from hubcheck.pageobjects.basepageelement import Text
from hubcheck.pageobjects.widgets.iframewrap import IframeWrap

class FramedInputs(BasePageObject):

    def __init__(self,browser):

        super(FramedInputs,self).__init__(browser,None)

        # update this object's locator
        self.locators = { 'frame1' : 'css=#frame1' ,
                          'frame2' : 'css=#frame2' ,
                          'i0'     : 'css=#i0' ,
                          'i1'     : 'css=#i1' ,
                          'i2'     : 'css=#i2' , }

        # setup page object's components

        # i0 is a widget that represents the text input
        # element outside of the first iframe
        self.i0 = Text(self,{'base':'i0'})

        # i1 is a widget that represents the text input
        # element inside of the first iframe
        self.i1 = IframeWrap( Text(self,{'base':'i1'}),
                              ['frame1'] )

        # i2 is a widget that represents the text input
        # element inside of the second iframe
        self.i2 = IframeWrap( Text(self,{'base':'i2'}),
                              ['frame2', 'frame1'] )
