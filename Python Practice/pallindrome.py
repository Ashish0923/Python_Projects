# Ask the user for a string and print out whether this string is a palindrome or not.

def palindrome_func(string):
    # Step to reverse the string
    string1 = string[::-1]
    if string == string1:
        print(f'{string} is Palindrome')
    else:
        print(f'{string} in not a Palindrome')


if __name__ == '__main__':
    string = input("Enter the string to be checked for palindrome: ")
    palindrome_func(string)

