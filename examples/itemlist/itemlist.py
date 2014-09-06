import random
import string
import pprint


class Container(object):

    def __init__(self,locatordict,item_class,*args):

        self.locators = locatordict
        self.__item_class = item_class
        self.__item_class_args = args


    def get_item_by_position(self,item_number):

        result = self.__item_class(
                    *self.__item_class_args,
                    item_number=item_number)
        return result


class Item(object):

    def __init__(self,locator_templates,item_number):

        self.locators = {}
        self.locator_templates = locator_templates
        self.__item_number = item_number

        self.update_item_number(item_number)

        # for simplicity, we give each item a fake value here
        self.v = {
            'name' : ''.join([random.choice(string.ascii_lowercase)
                                for i in range(5)]),
        }


    def __str__(self):

        s = {
                'item_number' : self.__item_number,
                'value' : self.v,
                'locators' : self.locators
            }

        return '%s %s' % (self.__class__.__name__,pprint.pformat(s))


    def update_item_number(self,item_number):

        self.__item_number = item_number

        for k,v in self.locator_templates.items():
            self.locators[k] = v.format(item_num=self.__item_number)


    def get_item_number(self):

        return self.__item_number


    def value(self):

        pass
