# Python

## Docstrings
```
def dosomething():
  """ this is the area to document function specifics so when calling function you have a reminder of what it does and it's a good practicee in python coding """
  return something
```
## Local and Global scope (Namespaces)
### Global
```
variable_global = 5
```
### Local
```
def game():
  variable_local = 5
```

### Modify global variables inside a function (not recommended has it could lead to bugs in the code)
```
variable = 0

def game():
  global variable
  variable += 1
 
game()
print(variable) # Output should be 1
```

### Both variables are the same name but different scopes
```
enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}"))
```
```
enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")
  return enemies - 1

increase_enemies()
print(f"enemies outside function: {enemies}"))
```
