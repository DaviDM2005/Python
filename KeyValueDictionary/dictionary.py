import json

# ჯერ გავარკვიოთ თუ რამდენი სტრიქონი უნდა დაწეროს User-მა:
lines = int(input("How many lines does your dictionary consist of? "))

key_list = []
value_list = []
dict = {}


# ფორ ლუპის გამოყენებით შევიტანოთ ეს სიტყვები დანაწევრებულად ლექსიკონში: 
for i in range(lines):
    text = input("Enter the words: ").split()
    key_list.append(text[0])
    value_list.append(text[1])

for i in range(len(key_list)):
    dict[key_list[i]] = value_list[i]

# შევქმნათ .json ფაილი სადაც იქნება მოცემული ლექსიკონი:
with open('dictionary.json', 'a') as file:
    file.write(json.dumps(dict))




while True:
# გავხსნათ .json ფაილი და მოვძებნოთ სასურველი key-ის მნიშვნელობა:
    search_word = input("\nSearch the word(or type 'exit' to exit):  ")

    if search_word.lower() == 'exit':
        break
    else:
        print(dict[str(search_word)])

