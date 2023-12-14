# Python Essentials: Key Concepts & Techniques

## Class

- **What is a Class?** A class in Python is a blueprint for creating objects. Objects have properties and behaviors, defined as attributes and methods within the class.

- **Basic Syntax:**

  ```python
  class MyClass:
      def __init__(self, attribute):
          self.attribute = attribute
      
      def method(self):
          return "This is a method"
  ```

- **Usage:** Classes are used to create user-defined data structures, encapsulating data and functions that work on that data.

- **Example:**

  ```python
  class Dog:
      def __init__(self, name, age):
          self.name = name
          self.age = age
  
      def bark(self):
          return f"{self.name} says woof!"
  
  my_dog = Dog("Buddy", 3)
  print(my_dog.bark())  # Output: Buddy says woof!
  ```

## Decorators

- **What is a Decorator?** A decorator in Python is a function that modifies the behavior of another function. They are helpful for extending the capabilities of functions without modifying their structure.

- **Basic Syntax:**

  ```python
  def my_decorator(func):
      def wrapper():
          # Do something before
          result = func()
          # Do something after
          return result
      return wrapper
  
  @my_decorator
  def my_function():
      return "Hello"
  ```

- **Usage:** Decorators are widely used for logging, enforcing access control, instrumentation, and more.

- **Example:**

  ```python
  def uppercase_decorator(function):
      def wrapper():
          result = function()
          return result.upper()
      return wrapper
  
  @uppercase_decorator
  def say_hello():
      return 'hello'
  
  print(say_hello())  # Output: HELLO
  ```

## Understanding the `__main__`

- **What is it?** This is a common Python idiom used to ensure that code is only executed when a script is run directly, and not when it's imported as a module in another script.

- **Usage:** This allows for a clean separation between code that defines classes and functions, and code that actually runs a program or script.

- **Example:**

  ```python
  def function():
      print("Function is called.")
  
  if __name__ == "__main__":
      print("Script is run directly.")
      function()
  else:
      print("Script is imported into another module.")
  ```

## **kwargs

- **What is kwargs?** `**kwargs` in a function signature allows it to accept arbitrary keyword arguments. This means you can pass a variable number of named arguments to a function.

- **Basic Syntax:**

  ```python
  def function_with_kwargs(**kwargs):
      for key, value in kwargs.items():
          print(f"{key}: {value}")
  
  function_with_kwargs(arg1='value1', arg2='value2')
  ```

- **Usage:** Useful in functions that need to handle named arguments not defined in advance.

- **Example:**

  ```python
  def greet(**kwargs):
      for key, value in kwargs.items():
          print(f"{key}: {value}")
  
  greet(name="John", age=25)  # Output: name: John, age: 25
  ```

## *args

- **What is \*args?** `*args` allows a function to accept any number of positional arguments. It collects them into a tuple.

- **Basic Syntax:**

  ```python
  def function_with_args(*args):
      for arg in args:
          print(arg)
  
  function_with_args('arg1', 'arg2', 'arg3')
  ```

- **Usage:** Used when you're not sure how many arguments might be passed to your function.

- **Example:**

  ```python
  def sum_numbers(*args):
      return sum(args)
  
  print(sum_numbers(10, 15, 20))  # Output: 45
  ```

## DataFrame.map

- **What is dataframe.map?** In pandas, `map` is used to substitute each value in a Series with another value.

- **Basic Syntax:**

  ```python
  import pandas as pd
  series = pd.Series(['apple', 'banana', 'carrot'])
  series.map({'apple': 'fruit', 'banana': 'fruit', 'carrot': 'vegetable'})
  ```

- **Usage:** Commonly used for element-wise transformations and substituting values in a Series.

- **Example:**

  ```python
  import pandas as pd
  fruits = pd.Series(['apple', 'banana', 'cherry'])
  fruit_type = fruits.map({'apple': 'fruit', 'banana': 'fruit', 'cherry': 'fruit'})
  print(fruit_type)
  ```

  Outputs:

  ```vbscript
  0    fruit
  1    fruit
  2    fruit
  dtype: object
  ```

## DataFrame.apply

- **What is dataframe.apply?** The `apply` function in pandas is used to apply a function along an axis of the DataFrame.

- **Basic Syntax:**

  ```python
  import pandas as pd
  df = pd.DataFrame({
      'A': [1, 2, 3],
      'B': [4, 5, 6]
  })
  df.apply(lambda x: x * 2)
  ```

- **Usage:** Useful for applying a function to each row/column of a DataFrame.

- **Example:**

  ```python
  import pandas as pd
  df = pd.DataFrame({    'A': [1, 2, 3],    'B': [4, 5, 6] })
  df.apply(lambda x: x * 2)
  ```

  Outputs:

  ```vbscript
     A   B
  0  2   8
  1  4  10
  2  6  12
  ```

  

## pandas.merge

- **What is pandas.merge?** It's a function in pandas used to merge two DataFrames or Series based on a common key.

- **Basic Syntax:**

  ```python
  import pandas as pd
  df1 = pd.DataFrame({'key': ['K0', 'K1', 'K2'], 'A': ['A0', 'A1', 'A2']})
  df2 = pd.DataFrame({'key': ['K0', 'K1', 'K3'], 'B': ['B0', 'B1', 'B3']})
  pd.merge(df1, df2, on='key')
  ```

- **Usage:** Essential for combining data from different sources, similar to SQL JOIN operations.

- **Example:**

  ```python
  import pandas as pd
  df1 = pd.DataFrame({'Key': ['K0', 'K1', 'K2'], 'A': ['A0', 'A1', 'A2']})
  df2 = pd.DataFrame({'Key': ['K0', 'K1', 'K3'], 'B': ['B0', 'B1', 'B3']})
  merged_df = pd.merge(df1, df2, on='Key')
  print(merged_df)
  ```

  Outputs:

  ```vbscript
     Key   A   B
  0   K0  A0  B0
  1   K1  A1  B1
  ```

  