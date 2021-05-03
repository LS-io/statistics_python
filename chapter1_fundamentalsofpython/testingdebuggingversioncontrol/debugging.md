# Debugging
##The term *debugging* means to remove one or more bugs from a given computer program.
Most often, the debugging process happens after a failed test, when we determine there is a "bug" in our program.

There are multiple forms of debugging that a program could employ.
* **Print Debugging**
    - one of the most common and elementary methods, it involves identifying the variables that could be affecting and/or causing the bug, and placing `print` statements for those variables at various places so that we can track the changes of those variables as the program is being executed. Once we find a change in that variable that is undesirable, we can identify its location from the `print` statement.
* **Logging**
    - instead of printing the variables, we decide to write them to a log file.

* **Tracing**
    - in this case, we follow the low-level function call and execution stack of the program when it executes. By looking at the order that the variables and functions are used in from that low-level perspective, we can identify the source of the error as well.
    - in python, tracing can be implemented using the `sys.settrace()` method from the sys module

In python, it is quite easy to employ print debugging, we just use `print` statements. For more complex functionalities, we can use a debugger, which is a module/library that is specifically designed for debugging. The most dominant is the built-in `pdb` module, which used to be run via the `pdb.set_trace()` method.

Since python 3.7, we can also use the simpler syntax of placing calls to the built-in `breakpoint()` function. Each place at which we call the `breakpoint()` function pauses the execution of the program and allow us ot inspect the behaviour and the current characteristics of the program, including its variables.
Specifically, once the execution (of the program) reaches a `breakpoint()` function, and input prompt will appear, where we can enter a `pdb` command.

These are the commands that you can take advantage of:
* **h**: for *help*, which prints out the complete list of commands you can use
* **u/d**: for *up* and *down*, respectively, which move the running frame count one level in a direction
* **s**: for *step*, which executes the instruction that the program is currently at and only pauses at the next instruction in the current function and when the execution is returned. This is ery useful in terms of observingthe immediate effect of a line of code on the state of the program
* **n**: for *next*, which executes the instruction that the program is currently at and only pauses at the next instruction in the current function and when the execution is returned. This command is somewhat similar to **s**, although it skips through the instruction at a much higher rate
* **r**: for *return*, which continues the execution until the current function returns
* **c**: for *continue*, which continues the execution until the next `breakpoint()` statement is reached
* **ll**: for *longlist*, which prints out the source code for the current instruction
* **p [expression]**: for *print*, which evaluates and prints out the value of the given expression

Overall, once the execution of the program is paused by a `breakpoint()` statement, we can also use a combination of different commands to inspect the state of the program and identify a potential bug.