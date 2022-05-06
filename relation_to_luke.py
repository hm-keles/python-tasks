# Luke Skywalker has family and friends. Help him remind them who is who. Given a string with a name, create a function that returns the relation of that person to Luke.
# Person (relation)
# Darth Vader (father)
# Leia (sister)
# Han (brother in law)
# R2D2 (droid)

def relation_to_luke(name) :
    if name == "Darth Vader" :
        return "Luke, I am your father."
    elif name == "Leia" :
        return "Luke, I am your sister."
    elif name == "Han" :
        return "Luke, I am your brother in law."
        
     
print(relation_to_luke("Darth Vader"))
print(relation_to_luke("Leia"))
print(relation_to_luke("Han"))