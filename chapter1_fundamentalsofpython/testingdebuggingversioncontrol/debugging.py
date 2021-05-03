## The term debugging means to remove one or more bugs from a given computer program.
## Most often, the debugging process happens after a failed test, when we determine there is a "bug" in our program.
##
##
## There are multiple forms of debugging that a program could employ.
##
## * Print Debugging
## - one of the most common and elementary methods, it involves identifying the variables that could be affecting and/or causing the bug, and placing print statements for those variables at various places so that we can track the changes of those variables as the program is being executed. Once we find a change in that variable that is undesirable, we can identify its location from the print statement.
##
## * Logging
## - instead of printing the variables, we decide to write them to a log file.
##
## * Tracing
## - in this case, we follow the low-level function call and execution stack of the program when it executes. By looking at the order that the variables and functions are used in from that low-level perspective, we can identify the source of the error as well.
## - in python, tracing can be implemented using the sys.settrace() method from the sys module
##
##
## In python, it is quite easy to employ print debugging, we just use print statements. For more complex functionalities, we can use a debugger, which is a module/library that is specifically designed for debugging. The most dominant is the built-in pdb module, which used to be run via the pdb.set_trace() method.