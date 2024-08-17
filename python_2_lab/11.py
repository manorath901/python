def count_elements(sentence):
    words = sentence.split()
    words = len(words)
    digits = sum(c.isdigit() for c in sentence) 
    uppercase = sum(c.isupper() for c in sentence)
    lowercase = sum(c.islower() for c in sentence)

    print(f"This sentence has {words} words")
    print(f"This sentence has {digits} digits")
    print(f"This sentence has {uppercase} upper case letters")
    print(f"This sentence has {lowercase} lower case letters")

sentence = input("Enter a sentence: ")
count_elements(sentence)