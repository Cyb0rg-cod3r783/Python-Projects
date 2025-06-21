# Breakdown of text[::-1]:
# text — is your string (e.g., "hello").

# [:] — is slice syntax: [start:stop:step].

# [::-1] means:

# start: not specified → start from the end.

# stop: not specified → go until the beginning.

# step: -1 → move backwards one character at a time.

text = input("Enter a word: ")
if (text == text[::-1]):
    print("Entered word is a palindrome")
else:
    print("The entered string is not a palindrome")