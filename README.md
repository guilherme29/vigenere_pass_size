# Vigenére pass size

A small and simple python script to get some statistics on what could be the size of the cipher password.

This is more of a library sort of thing so you should call the get_pass_statistics function in your code. I left a ciphered text so you can see an example of the program running, you can then remove it. All you have to do is call 
```Python
get_pass_statistics()
```
on a string of ciphered text. It should print out the factors that occur the most by order. One of the most popular factors should be the password length.


I took some inspiration from the black chamber website, you can check it here: http://www.simonsingh.net/The_Black_Chamber/vigenere_cracking_tool.html

