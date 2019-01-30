# Dove
Dove is an Assembly-like programming language built in Python. I thought it would be funny for such a low level lanuage to be compiled (*technically, its interpreted*) by such a high level language, like Python. The interpreter still needs work, I might just rewrite it from scratch. Or maybe in Scratch, that would be funny...

## How to Use

How to run:

`"FILE_PATH_OF_DOVE_FILE.txt" | python3 "~/compiler.py"`

Basic syntax:
```
@ use '@' for comment
@ use '#' to denote a label
@ use 'goto' to goto a label
@ use 'if' to denote a simple boolean expression (==, !=, <, >, <=, >=)
@ if false, skip next line
@ 'new' creates new variable
@ 'str' stores input into memory
@ 'add' calculates sum (or string concat) and stores in memory
@ 'sub' same but subtraction
@ 'lsft' preforms a left bit shift
@ 'rsft' preform right shift
@ 'ldr' loads the memory into inputted variable
```
