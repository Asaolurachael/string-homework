str = "MY NAME IS RACHAEL"

print(str.casefold())                                       # converts string into lower case


str = "This is coding. This is a coding class. This"
print(str.count("This"))                                    # Returns the number of times a specified value occurs in a string

str = "This is coding"
print(str.find("coding"))                                   # Searches the string for a specified value and returns the position of where it was found

str = "This coding. This is a coding class"
print(str.endswith("coding"))                               # Returns true if the string ends with the specified value

str = "c\to\td\ti\tn\tg"
print(str.expandtabs())                                     # Sets the tab size of the string

str = "This is coding"
print(str.index("s"))                                       # Searches the string for a specified value and returns the position of where it was found

str = "coding002"
print(str.isalnum())                                        # Returns true if all characters in the string are alphanumeric

str = "coding2"
print(str.isalpha())                                        # Returns true if all characters in the string are alphabet

str = "3.4"
print(str.isdecimal())                                      # Returns true if all characters in the string are decimals

str = "2334"
print(str.isdigit())                                        # Returns true if all characters in the string are digits