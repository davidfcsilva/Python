# Python

## Docstrings
def dosomething():
  """ this is the area to document function specifics so when calling function you have a reminder of what it does and it's a good practicee in python coding """
  
## Local and Global scope (Namespaces)
### Global
variable_global = 5

### Local
def game():
  variable_local = 5

### Modify global variables inside a function

variable = 0

def game():
  global variable
  variable += 1
 
game()
print(variable) # Output should be 1
