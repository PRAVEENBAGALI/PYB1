multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)

language = 'Python'
print(language)
first_three= language[-3:]
print(first_three)
first_three= language[0:3] # this is to print range
first_three= language[3:6] # this is to print range
first_three= language[1:4] # this is to print range
print(first_three)

challenge = 'thirty days of python'
print(challenge.capitalize())
print(challenge.endswith("of"))
print(challenge.count('o')) #checks the occurance of o in string
print(challenge.find('o')) #finds out the location of o in string
print(challenge.isalnum())
print(challenge.isalpha())
print(challenge.islower()) # is it lower
print(challenge.isupper()) # is it upper
print(challenge.swapcase())
print(challenge.title())
print(challenge.split())
print(challenge.strip())
print(challenge.replace('days','number'))
print("##############################################")
num = '10'
print(num.isnumeric())      # True
print('ten'.isnumeric())
print("#############################################")
challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
