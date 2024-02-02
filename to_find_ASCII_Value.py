# Program to find the ASCII value of the given character

c = 'p'
print("The ASCII value of '" + c + "' is", ord(c))



'''
Here we have used ord() function to convert a character to an integer (ASCII value). This function returns the Unicode code point of that character.

Unicode is also an encoding technique that provides a unique number to a character. While ASCII only encodes 128 characters, the current Unicode has more than 100,000 characters from hundreds of scripts.
'''