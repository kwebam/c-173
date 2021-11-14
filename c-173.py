class parent():
    def __init__(self):
        print("This is Parent Class")
    
    def menu(dish):
        if dish == "burger":
            print("You can add following toppings")
            print("add More Cheese | jalopeno")
        elif dish == "iced_americano":
            print("You can add following toppings")
            print("add Choclate flavour | caramel flavour")
        else:
            print("Please Enter valid Dish")
    def final_amount(dish, add_ons):
        if dish == "burger" and add_ons == "cheese":
            print("You need to pay 250 USD")
        elif dish == "burger" and add_ons == "jalpeno":
            print("You need to pay 350 USD")
        elif dish == "iced_americano" and add_ons == "choclate":
            print("You need to pay 250 USD")
        elif dish == "iced_americano" and add_ons == "caramel":
            print("You need to pay 450 USD")
            
class child1(parent):
    def __init__(self, dish):
        self.new_dish = dish
        
    def get_menu(self):
        parent.menu(self.new_dish)
        
class child2(parent):
    def __init__(self, dish, addons):
        self.new_dish = dish
        self.addons = addons
        
    def get_menu(self):
        parent.menu(self.new_dish)
    
    def get_final_amount(self):
        parent.final_amount(self.new_dish, self.addons)




child1_object = child1("burger")
child1_object.get_menu()

child2_object = child2("burger","jalpeno")
child2_object.get_final_amount()