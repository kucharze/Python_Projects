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

#String slicing is a way to extract a portion of a string. You can use the slice operator [] to extract a substring from a string. The slice operator takes two arguments: the start index and the end index. The start index is inclusive, and the end index is exclusive.
print(name[0:4]) # Prints the first four characters of the string. The slice operator [0:4] extracts the substring from index 0 to index 4 (exclusive).
print(name[5:10]) # Prints the characters from index 5 to index 10 (exclusive).

url="https://google.com"
print(url[8:13]) # Prints the characters from index 8 to index 13 (exclusive).
print(url[:-4]) # Prints the characters from the beginning of the string to index -4 (exclusive). The negative index counts from the end of the string.
#4 characters from the right of the string are removed. The slice operator [:-4] extracts the substring from the beginning of the string to index -4 (exclusive).

print(url[8:-4]) # Prints the characters from index 8 to index -4 (exclusive). The slice operator [8:-4] extracts the substring from index 8 to index -4 (exclusive).

name = "Root user root admin"
print(name.count("root")) # Counts the number of occurrences of a substring. The count() method returns the number of occurrences of a substring in a string.