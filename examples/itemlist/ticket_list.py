from itemlist import Container, Item


class TicketList(Container):

    def __init__(self,locatordict):

        item_args = {
            'ticketnumber' : "css=tr:nth-of-type({item_num}) .ticket-id",
            'summary'      : "css=tr:nth-of-type({item_num}) .ticket-content",
            'status'       : "css=tr:nth-of-type({item_num}) .status",
            'group'        : "css=tr:nth-of-type({item_num}) .ticket-group",
            'assignee'     : "css=tr:nth-of-type({item_num}) .ticket-owner",
            'activity'     : "css=tr:nth-of-type({item_num}) .ticket-activity",
            'delete'       : "css=tr:nth-of-type({item_num}) .delete",
            'tags'         : "css=tr:nth-of-type({item_num}) .tags",
        }

        super(TicketList,self).__init__(locatordict,TicketItem,item_args)


class TicketItem(Item):

    def value(self):

        return self.v

