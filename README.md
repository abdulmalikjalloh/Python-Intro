# Python-Intro

Python programming language basics/fundamentals to functions.

# What is Python?

Python is a programming language.

# What is programming and/or a program?

- Programming is writing instructions for a computer to execute.

- A program is a set of instructions.

# What is a computer?

A computer is an electronic device that performs I.P.O.

- I.P.O ---> Input Process Ouput.
  For this reason (IPO) and in my opinion, I believe the term computing devices is best suited to describe electronic devices as it covers a wide range of electronic devices (Smart Watch, Sat Nav, Tablet, Mobile Phones..etc) that perfroms input process and output.

# Sorry for that detour, back to instructions.

Humans carry out instructions daily, remember as a child, more often than you would have liked, you were instructed by your parents or guardians "It's time to go to bed". Only, with python, we are instructing a computer(computing device) instead of another person to do things. Thus, a programmer write some (code) instructions in python programming language for the computer(computing device) to carryout or execute. However, there is a way these instructions have to be written for it to be executed succssfully, or rules(syntax) that we have to follow when writing instructions in python or to put more aptly when programming in python.

# Syntax

As with every culture and society there are rules(written/unwritten.), take the rule(s) that govern the way we communicate with each other. For example, when we extend and/or exchange greetings with people, be it family, friends or strangers, we follow some sort of rule(s). Granted that when interacting with family members, loved ones or friends, these rules are less stringent as opposed to an interaction with a stranger or someone you know in a profesional capacity. It is important to note that, these instructions could be in any programming language, and that these rules(syntax) are specific to a programming language. Since python is the programming language of choice, it only makes sense it is reference specifically. Suffice to say "Syntax" in this instance are the rules specific to python programming language, in other words the spelling and grammar. Below are some python syntax examples:

# Python Syntax examples

- Colon :
- Parenthesis ().
- Quotation "" or ''.
- Backlash \n.
- print("Welcome to the Python Diaries series").
- print( 12 + 22).
- num4 = 45.
- num5 = 55.
- total = num4 + num5.
- print(f"The total {total} ").

# IDEs / Code Editors

Integrated development environment, makes it easier for programmers to write code, run code and debug(find errors) in different promgramming language. IDEs provide useful features such as; syntax higlighting (syntax structures), colour coding, auto complete lines of code using intellisense and even automatically indent your code. And indentation is very important when you write your code in python, and would lead to an indentation error if a line/block of code is not properly indented. Below is list of three IDEs and three code editors;

- Eclipse.
- Netbeans.
- Pycharm.
- VSCode.
- Sublime.
- Atom.

# Interpreter

Python is an interpreted programming language, thus use an interpreter to translate the code(instructions) written by programmers into a machine (code) readable format. When programmers write code, it is written in high level language(Python is an example of such language) and as computers can only executes machine code, thats why translator is required.

There is a saying that, computers are dumb. Therefore, when writing programs in python, if we don't follow the syntax of python programming language, we get syntax errors. The computer will not try to correct our syntax, rather expecting the programmer to use the correct syntax when writing code.

# Programming Constructs

Sequence, Selection and Iteration are the three basic programming constructs used to control the order in which statements or code are executed in a program.

# Sequence

- In python programming sequence is instructions perfromed or executed in the order in which they were written. Therefore, it is important to write the code in the correct sequence so that the predicted outcome matches the expected outcome, since the order of execution is from top to bottom.

# Variables

- A variable is a container that holds a value, the value can be of any data type (more on data type later), this (variable) is stored in a memory location and must be declared before it is used. The variable is then reference when the program is running, even though a variable holds one value at a time. However, during the execution(running) of a program the value of the variable can change.
  For example, this is how a variable is initiliased in python; number = 10 , num = 3, name = "Abu"
- Variable naming conventions and meaningful identifiers
  - Variable naming convention are a naming standards that should be adhered to when writing python code, to ensure your code is easily readable and understood by other programmers.
  - Meaningful identifiers, this means a variable must be named accordingly, for example num1 or num will be meaningful name for a variable that holds the number(numeric value) 1, 2, 3. Whereas, userName would be unsuitable as a name for a number variable, but appropriate for a variable that holds the value "Musa21".
    https://peps.python.org/pep-0008/#function-and-variable-names
- Variable Initialisation
  - Initialisation is when a variable is assinged an initial value.
- Variable Assignment

  - Is when the value of a variable is changed at the memory location.

- Data types.

  - Data types are variables used to reserve memory space.
    In python programming an explicit varaiable initialisation is not required to reserve memory space. This happens automatically when you initialised a value to a variable. Some of the data types in python are listed below.
    - String.
    - Numeric Types(int, float).
    - Boolean(True/False).
    - Sequence Types (list,tuple).
    - Set Types (set, frozenset).

- Input function.

  - input function: is used to capture user input in python and the default data type is string. Use the int, float, string and other data types to convert the default string input to the respective data type as required.

- Arithmetic Expression.

  - Arithmetic expressions evaluates to a number, think BIDMAS(evaluated in order of precedence) when using Arithmetic expression in python.
    - B - brackets
    - I - indices
    - D - division
    - M - multiplication
    - A - addition
    - S - subtract
  - Arithmetic operators.
    - (+) plus operator.
    - (-) subtraction operator.
    - (\*) muliplication operator.
    - (/) division operator (anwer with remainder).
    - (//) floor division/ integer quotient operator (round the answer with no remainder).
    - (%) operator : mod/modulus (outputs the remainder ).
    - (\*\*) powers.

- Logical Expressions
  - Logical expression evaluates to either True or False and used to control program flow(i.e the execution of the code based).
  - The three logical Operators are; and, or, not ".
- Comparison Operators.
  - Use comparison operators to compare values.
    - (==) equal to.
    - (<)less than.
    - (>)greater than.
    - (<) less than or equal to.
    - (>=) greater than or equal to.
    - (!=) Not equal to.
- The assignment operator
- The assignment operator '=' can be used to assigned the same value to multiple variables"
  - myNum1 = myNum2 = myNum3 = 12
- The coumpound assignment
  - Python uses several compound operators, the compound assignment operator, add the value stored in the variable on the right to the value stored in the variable on the left, then assign the total value to the variable on the left.
  - myNum4 += myNum5

# Selection

- Is used to control the flow of program using if, else and elif to ensure a block of code is executed if the condition is true.
- if and else statement.
  - if this condition is true(met) do something.
  - else do something different.
- if, else and elif statement.
  - if this condition is true(met) do something.
  - elif this other condition is true(met) do something else.
  - else do something different.
- Nested Selection.

  - This is when an if/else block(selection) is place inside another if/else block(selection).
  - Nested if only.

    - if this condition is true(met) do something.
      - if this condition is true(met) do something (This if is nested).
    - else do something different.

  - Nested if and else.
    - if this condition is true(met) do something.
      - if this condition is true(met) do something (This if is nested).
      - else do something different (This else is nested).
    - else do something different.

# Iteration

- To put simply iteration means repetition, python uses the for and while loops for repetition.

  - For Loop is used when the number of iteration is known.
  - While loop is used unitl a condition is met(unknown number of iterations).

- List & Strings Methods/functions.

  - List Methods are used to perform list operations.
  - String Methods are used to perform string operations.

# Python Data Structure: Record and Dictionary

- Data Structure is

  - Record is a static data structure. You must determine the attributes and the data

  - Dictionary
