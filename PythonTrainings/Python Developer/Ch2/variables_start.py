# 
# Example file for variables

# Declare a variable and initialize it
f=0
print("f")
# # re-declaring the variable works

f="ABC"
print(f)

# # ERROR: variables of different types cannot be combined
print("this is a text" +f)

# Global vs. local variables in functions

def someFunction():
    global f
    f="def"
    print(f)

someFunction()
del(f)
print(f)