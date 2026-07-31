# Functions
A function is a reusable block of code that performs a specific task.

## Syntax
def function_name():
    # code

function_name()

## Advantages
- Code Reusability
- Easy to Read
- Easy to Maintain
- Reduces Repetition

## Parameters
Parameters allow us to pass data to a function.

Syntax
def function_name(parameter):
    # code

function_name(argument)
Parameter -> Variable in function definition
Argument -> Actual value passed while calling the function

## Return
The return keyword sends a value back from a function.

Syntax
def function_name():
    return value

Difference
print() -> Displays output
return -> Sends output back

## Scope
Scope defines where a variable can be accessed.

### Global Variable
Declared outside a function.
Accessible everywhere.

### Local Variable
Declared inside a function.
Accessible only inside that function.

## Lambda Function
A lambda function is an anonymous (unnamed) function.

Syntax
lambda parameters: expression

Example
square = lambda x: x * x