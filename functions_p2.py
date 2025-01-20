def dad_loves(kid1, kid3, kid2):
    print("My children are", kid1, kid2, "and", kid3)
    print("The smalles one is ", kid3)

dad_loves(kid1 = "morita", kid2 ="paris", kid3 = "Rambo") # <-- keyword arguments 


def mom_loves(**kids):
    print("My children are", kids["a"], kids["b"], "and", kids["c"])
    print("The smalles one is ",kids["a"])

mom_loves(a = "morita", b ="paris", c = "Rambo") # <-- keyword argument