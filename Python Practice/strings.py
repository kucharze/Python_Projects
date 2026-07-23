# This file will be about strings and methods to manipulate them.
# Strings are a sequence of characters. They are used to represent text. Strings are enclosed in quotes. You can use single or double quotes.

name = "Root Admin User"
print(len(name)) # Prints the length of the string. The len() function returns the number of characters in a string.

print(name.upper()) # Converts the string to uppercase. The upper() method returns a new string with all characters in uppercase.
print(name.lower()) # Converts the string to lowercase. The lower() method returns a new string with all characters in lowercase.
print(name.capitalize())# Capitalizes the first character of the string. The capitalize() method returns a new string with the first character in uppercase and the rest in lowercase.
print(name.title())# Converts the string to title case. The title() method returns a new string with the first character of each word in uppercase and the rest in lowercase.

print(name.find("Admin")) # Returns the index of the first occurrence of a substring. The find() method returns -1 if the substring is not found.
print(name.replace("Admin", "Super Admin")) # Replaces a substring with another substring. The replace() method returns a new string with the substring replaced.