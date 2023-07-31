# Python-OOP-Ex
Objected Oriented Programming using Python. 
## **Serial Generator**

Classes are a great way to combine data and functionality.
We’ll use a class to make a “serial number generator” — you should be able to initialize it with a start number.

## **Random Word**

You’ll need to make a class that works like this:

- it is instantiated with a path to a file on disk that contains words, one word per line
    - it reads that file, and makes an attribute of a list of those words
    - it prints out “[num-of-words-read] words read”
    
    (it doesn’t need to do all of this directly in the ***__init__*** method; it might be a good idea for the ***__init__*** method to call other functions to do some of this.)
    
- it provides a method, ***random()***, which returns a random word from that list of words
    
    Note: the ***random*** method **should not** re-read the list of words each time; it should work with the already-read-in list of words.
  ## **Subclass The RandomWordFinder**

Our RandomWordFinder is nice, but we’ve received a new requirement: sometimes, we’ll be provided with files that have blank lines, as well as lines that start with a `#` symbol to make a comment.
