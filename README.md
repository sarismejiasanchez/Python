## Python

**Functions in Python: Introduction**

Explore how Python facilitates code reuse by using functions in this 17-video course, which shows learners how to define functions, learn passing arguments to functions, and returning values from functions. The functions you will examine change the state of the program, may have side effects, and have observable effects other than their return values. Since functions with side effects are hard to parallelize and use in a distributed environment, you will learn correct ways of returning values from functions. First, you will learn how to invoke functions by using both positional and keyword arguments. You will next work with positional input arguments in custom functions, and learn that these are required arguments, and how to order these arguments to invoke your function. You will next learn to use variable length arguments in defining custom functions. Finally, you will learn how keyword arguments or named arguments are a way to make the intent behind function invocation absolutely explicit, and help prevent bugs in programs that are especially hard to detect.

### Duration

2h 3m 6s2hours 3minutes 6seconds

### Prerequisites

None

### Expertise Level

Beginner

### Code

it_pyfcaldj_01_enus

### Objectives

-   discover the key concepts covered in this course
-   recall and implement custom functions
-   define, invoke, and name functions
-   recall how functions work as objects
-   define and invoke functions with input arguments
-   reference global variables from within a function
-   recall the characteristics of working with positional arguments
-   return information from functions
-   write functions with multiple return statements
-   return complex data types from functions
-   specify keyword arguments while invoking functions
-   recall nuances in invoking functions using keyword arguments
-   specify default values for function arguments
-   implement functions with *args variable length positional arguments
-   combine positional and variable length arguments
-   implement functions with **kwargs variable length keyword arguments
-   recall characteristics of functions, input arguments, and return values

### Instructor

Janani Ravi , Software engineer and big data expert

Janani Ravi has a master’s degree from Stanford and is a certified Google Cloud Architect and Data Engineer. She has worked for large technology companies, such as Google, Microsoft, and Flipkart. In fact, Janani was one of the original engineers for Google Docs and holds four patents related to its real-time collaborative editing framework. After spending years as a senior software engineer, Janani decided to combine her love for technology with her passion for teaching. She co-founded Loonycorn, a studio for high-quality technical video content, and has authored a vast array of Skillsoft courses. From the basics of Python to the intricacies of machine learning, Janani loves sharing her knowledge with learners of all abilities.

**Area(s) of expertise:**  Data science, machine learning, cloud computing, programming languages, full-stack development

**Interesting fact:**  Absolutely loves dogs and has 4 dogs of her own

## Exersice: Introduction to Functions in Python

### Describe what functions are, and how they are useful in programming.

#### Function
 - A piece of reusable codewhich may:
	 - Perform an action or a calculation.
	 - Can be customized to work on different inputs.
	 - Returns a result to the user.
 - Defining a function does not execute code.
 - A function once defined can be invoked.
 - Invoking a function will execute the code associated with the function.

### Describe how you pass information to, and get information from functions.

#### Input Arguments

 - Information can be passed into a function using **input arguments**.
 - Input arguments are specified at the time of function definition.
 - Input arguments are variables which can be accessed by the function to perform actions o calculations.
 - When a function is invoked, the user specifies values that are associated with the input arguments.
 - Input arguments can be any data type - primitive types (float, int) or complex types (lists, dictionaries, and even custom types).

#### Return Values

 - Information is returned from a function using the **return** statement.
 - The default return value is the special Python value **None**.
 - The return values are typically the result of the calculation or operation.
 - Return values can be any kind of data.
 - Basic primitive types or complex types such as lists, dictionaries or strings.

### List the differences between positional arguments and keyword arguments.

#### Positional Arguments

 - Input arguments are specified along with the function definition.
 - Values assigned to positional arguments are based on their **position** in the function definition.
 - Values are assigned to arguments at the time of **function invocation**.
 - Arguments are NOT referred to by the variable names.
 - The **order of the values should match the order of the arguments**.
 - Unless default values are specified, positional arguments are the **requiered** arguments.
 - Positional arguments should be specified **before** keyword arguments.

#### Keyword Arguments

 - No change  in the custom function definition.
 - Values assigned to keyword arguments by **variable name** during **function invocation**.
 - Arguments are referred to by the variable name.
 - The order of the values need NOT match the original order of the arguments in the function definition.
 - Unless default values are specified, keyword arguments are required arguments.
 - Keyword arguments should always be specified **after** positional arguments.
