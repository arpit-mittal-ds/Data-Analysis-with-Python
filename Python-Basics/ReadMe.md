

When we run a Python program, two steps happen,
The code gets converted to another representation called ‘Byte Code’
‘Byte Code’ gets converted to Machine Code (which is understandable by the computer)
The second step is being done by PVM or Python Virtual Memory. So PVM is nothing but a software/interpreter that converts the byte code to machine code for given operating system.
 
PVM is also called Python Interpreter and this is the reason Python is called an Interpreted language.

![image](https://user-images.githubusercontent.com/68102477/119583324-b5dbdc00-be09-11eb-8b7e-e962a26724ee.png)

D:\> python -m py_complie x.py
 
Here we are calling the Python compiler with the  -m option. -m represents module and the module name is py_compile. This module generates the .pyc file for .py file. *.pyc file contains the byte code of the Python program. One can open and see the byte code representation of the python program. To convert byte code into machine code/output use:
 
D:\> python <nameofpycfile>.pyc
 
Here Python would skip the step of byte code generation and would convert byte code directly to machine code.
  
