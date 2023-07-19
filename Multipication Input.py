
import ctypes  # An included library with Python install.
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)
Mbox('Hello User', 'Welcome to this website', 1)

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)
Mbox('txt boxs', 'You will see a lotttt of these. No joke.', 1)


test_text = input ("Enter a number: ")

# Converts the string into a integer. If you need
# to convert the user input into decimal format,
# the float() function is used instead of int()
test_number = int(test_text)

# Prints in the console the variable as requested
print ("The number you entered is: ", test_number)
      
print ("Now enter a other number to multiply it.")



test_text2 = input ("Enter a number: ")

# Converts the string into a integer. If you need
# to convert the user input into decimal format,
# the float() function is used instead of int()
test_number2 = int(test_text2)

# Prints in the console the variable as requested
      
print(test_number*test_number2)

