import unittest
from inventory import Inventory
from item import Food

class InventoryAndFoodTest(unittest.TestCase):

    def setUp(self):
        self.inv = Inventory("Conner")
        self.cheese = Food("cheese")
        self.bread = Food("bread")
        self.cake = Food("cake")
        print ("testInits executed!")
        self.inv.put_in(self.cheese)
        print ("test_put_in executed!")
        self.inv.put_in_quiet(self.bread)
        self.inv.put_in_quiet(self.cake)
        print ("test_put_in_quiet executed!")

    # def test_put_in(self):
    #     self.inv.put_in(self.cheese)
    #     print ("test_put_in executed!")
    #
    # def test_put_in_quiet(self):
    #     self.inv.put_in_quiet(self.bread)
    #     self.inv.put_in_quiet(self.cake)
    #     print ("test_put_in_quiet executed!")

    def test_check_inventory(self):
        self.assertEqual(self.inv.check_inventory("cheese"), True)

    def test_look_for_type_and_poplar(self):
        self.assertEqual(self.inv.poplar("bread"), self.bread)
        self.assertEqual(self.inv.poplar("cake"), self.cake)

        self.assertEqual(self.inv.look_for_type(Food),self.cheese)

    def test_list_inventory(self):
        self.inv.list_inventory()
        print("Listed Inventory!")

    def test_look(self):
        self.inv.look("cheese")
        self.inv.look("bread")
        self.inv.look("cake")
        self.cheese.look()
        self.bread.look()
        self.cake.look()
        print("look tested!")



if __name__ == "__main__":
    unittest.main()
