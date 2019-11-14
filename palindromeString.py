# Gets a string as user input,
# and checks if that string is a palindrome
class PalindromeString:

	# Constructor that gets the user input
	# and calls the checkPalindrome() method
	def __init__(self):	
		str = input("Check if s string is a palindrome: ")
		self.checkPalindrome(str)	

	# Checks if a string is a palindrome
	def checkPalindrome(self, str):
		# get the length of the string
		strLength = len(str)
		
		# initializing lowIndex and highIndex
		lowIndex = 0
		highIndex = strLength-1

		# boolean that is used for the success message
		isStrPalindrome = True
		# loops the string and compares the chars
		for x in str:	
			if(str[lowIndex] != str[highIndex]):
				print("The string is NOT a palindrome")
				isStrPalindrome = False
				break

			# increasing the low index by 1
			lowIndex = lowIndex+1
			# decreasing the heig index by 1
			highIndex = highIndex-1

		# print success message
		if(isStrPalindrome):
			print("The string is a palindrome")

# initializing the class
strPalindrome = PalindromeString()
