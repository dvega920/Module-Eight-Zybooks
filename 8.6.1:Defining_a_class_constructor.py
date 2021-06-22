
# defines a PhonePlan object
class PhonePlan:
    # init PhonePlan object with default params num_mins and num_messages
    def __init__(self, num_mins=0, num_messages=0):
        self.num_mins = num_mins  # default param assigned to self.num_mins
        self.num_messages = num_messages # default param assigned to self.num_messages

    def print_plan(self): # method that prints num_mins and num_messages
        print('Mins:', self.num_mins, end=' ')
        print('Messages:', self.num_messages)

my_plan = PhonePlan(int(input()), int(input()))  # creates instance of PhonePlan with user input and passes it to PhonePlan object
dads_plan = PhonePlan() # creates an instance of PhonePlan with no params
moms_plan = PhonePlan(int(input())) # creates an instance of PhonePlan and passes one param which will be assigned to num_mins

print('My plan...', end=' ')
my_plan.print_plan()  # calling print_plan method from the my_plan instance of PhonePlan

print('Dad\'s plan...', end=' ')
dads_plan.print_plan() # calling print_plan method from the dads_plan instance of PhonePlan

print('Mom\'s plan...', end=' ')
moms_plan.print_plan() # calling print_plan method from the moms_plan instance of PhonePlan®