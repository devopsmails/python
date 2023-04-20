import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data.to_dict())
phonetic_dict = {row.letter : row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)
word = input("Enter a word: " ).upper()
#Helps excepting a keyerror & to re take the input
def phonetic_alphabet():
    try:
        output = [phonetic_dict[char] for char in word]
    except KeyError:
        print("Only Alphabet letters please!")
        phonetic_alphabet()
    print(output)
phonetic_alphabet()
