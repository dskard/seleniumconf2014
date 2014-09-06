from itemlist import Container, Item


class ToolsList(Container):

    def __init__(self,locatordict):

        item_args = {
            'title'          : "css=tr:nth-of-type({item_num}) .entry-title",
            'details'        : "css=tr:nth-of-type({item_num}) .entry-details",
            'alias'          : "css=tr:nth-of-type({item_num}) .entry-alias",
            'status'         : "css=tr:nth-of-type({item_num}) .entry-status",
            'time'           : "css=tr:nth-of-type({item_num}) .entry-time",
            'resource'       : "css=tr:nth-of-type({item_num}) .entry-page",
            'history'        : "css=tr:nth-of-type({item_num}) .entry-history",
            'wiki'           : "css=tr:nth-of-type({item_num}) .entry-wiki",
        }

        super(ToolsList,self).__init__(locatordict,ToolsItem,item_args)


class ToolsItem(Item):

    def value(self):

        return self.v

