# Day 4: 30 Days of python programming

# sentence = " ".join(['Thirty', 'Days', 'Of', 'Python'])
# print(sentence)

# sentence = "{} {} {} {}".format('Thirty', 'Days', 'Of', 'Python')
# print(sentence)

company = "Coding For All"

# print(company)

# print(len(company))

# print(company.upper())

# print(company.lower())

# print(company.capitalize())

# print(company.title())

# print(company.swapcase())

# print(company[:6])

word = "Coding"
# if company.find(word) != -1 and company.index(word) != -1 and company.count(word) != 0:
#   print(f'{word} is present in {company}')
# else:
#   print(f'{word} is not present in {company}')

# print(company.replace(word, "Python"))

# sentence = "Python for Everyone"
# words = sentence.split()
# words[-1] = "All"
# print(" ".join(words))

# words = company.split()
# print(words)

# mncs = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
# print(mncs.split(","))

# charAt0 = company[0]
# print(charAt0)

# charAtEnd = company[-1]
# print(charAtEnd)

# print(len(company)-1)

# print(company[10])

# sentence = 'Python For Everyone'
# words = sentence.split()
# print(words[0][0]+words[1][0]+words[2][0])

# words = company.split()
# print(words[0][0]+words[1][0]+words[2][0])

# print(company.index('C'))

# print(company.index('F'))

# sentence = "Coding For All People"
# print(sentence.rfind('l'))

# sentence = 'You cannot end a sentence with because because because is a conjunction'
# print(sentence.find("because"))
# print(sentence.index("because"))

# sentence ='You cannot end a sentence with because because because is a conjunction'
# print(sentence.rfind('because'))
# print(sentence.rindex('because'))

# sentence = 'You cannot end a sentence with because because because is a conjunction'
# word = 'because'
# start = sentence.find(word)
# end = sentence.rfind(word) + len(word)
# print(sentence[ start: end])

# sentence = 'You cannot end a sentence with because because because is a conjunction'
# word = "because"
# print(sentence.find(word))

# sentence = 'You cannot end a sentence with because because because is a conjunction'
# word = 'because'
# print(sentence[sentence.find(word) : (sentence.rfind(word) + len(word))])

# substring1 = "Coding"
# print(company.startswith(substring1))

# substring2 = "coding"
# print(company.endswith(substring2))

# text = '   Coding For All     '
# print(text.strip())

# var1 = "30DaysOfPython"
# var2 = "thirty_days_of_python"
# print(var1.isidentifier())
# print(var2.isidentifier())

# py_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
# print(" # ".join(py_libraries))

# sentence = "I am enjoying this challenge.\nI just wonder what is next."
# print(sentence)

# sentence = "Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"
# print(sentence)

# radius = 10
# area = 3.14 * radius ** 2
# print(f"The area of a circle with radius {radius} is {area} meters square.")

a = 8
b = 6
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")
