# math-symbol-replacer
A small Python script that converts keywords into their actual symbols, using the Pynput library
Designed for maths students who don't want to bother with LaTeX but still need some symbols, but adding your own symbols is easy

## How do I use it?
Just download and run the Python file in the background.

To "activate" it, type the open square bracket `[` to initialise it.
Then, type the name of the symbol to use. It's recommended to check the list in "INDEX" for what shorthand gives you what symbol. These were made under my preferences, but feel free to change the abbreviation
Then, type the closing square bracket `]` to finalise it. The program then overwrites what you typed for the actual symbol.


## How do I add my own?
It's very simple, you don't even need Python to add one! Open the python file and then navigate to the "INDEX". Add a new line within the curly brackets of the form:

`"abbreviation_name": "symbol",`


# Further development
I'll work on this to make it more friendly for those who are unable to use Python, as well as provide a windowed method of access.
