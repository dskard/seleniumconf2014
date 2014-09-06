from tools_list import ToolsList
from ticket_list import TicketList


# create a ToolList object

t1 = ToolsList(None)

print "\ncreate ToolItem objects from the ToolList\n"

t1i1 = t1.get_item_by_position(5)
t1i2 = t1.get_item_by_position(6)
t1i3 = t1.get_item_by_position(8)

print t1i1
print t1i2
print t1i3


# create a TicketList object

s1 = TicketList(None)

print "\ncreate TicketItem objects from the TicketList\n"

s1i1 = s1.get_item_by_position(2)
s1i2 = s1.get_item_by_position(4)
s1i3 = s1.get_item_by_position(9)

print s1i1
print s1i2
print s1i3


print "\nupdate the item_number of the TicketItem objects\n"

s1i1.update_item_number(12)
s1i2.update_item_number(14)
s1i3.update_item_number(19)

print s1i1
print s1i2
print s1i3

