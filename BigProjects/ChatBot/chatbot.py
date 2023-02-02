import re
import random
from googlesearch import search


while True:
            
    start_input = input("\nYou: ")
    
    user_input = re.sub('[{}]'.format("!?'"), '', start_input).lower()
    user_input = "".join(user_input.split())
    
    bot_hello_list = ["Hi","Hello","Heyy","Hey"]
    you_hello_list = ["hi","hello!","hello","heyy","hey"]


    if user_input in you_hello_list:
        hello = random.choice(bot_hello_list)
        print(f"Jarvis: {hello}")

    elif user_input == "hola":
        print("Jarvis: Hola mi amigo!!") 

    elif user_input == "idontknowspanish":
        print("Jarvis: I meant: Hello, my friend ))")
        
    elif user_input == "doyouknowgeorgian":
        print("Jarvis: დიახ, მე ვიცი ცოტა ქართული, ჯერ სწავლის პროცესში ვარ.")
        
    elif user_input == "რაიცისაქართველოსშესახებ":
        print("Jarvis: საქართველო არის ქვეყანა, რომელიც მდებარეობს დასავლეთ აზიისა და აღმოსავლეთ ევროპის გზაჯვარედინზე, კავკასიის რეგიონში. მისი მოსახლეობა დაახლოებით 3,7 მილიონი ადამიანია და მისი დედაქალაქი და უდიდესი ქალაქი თბილისია. საქართველოს აქვს მდიდარი კულტურული მემკვიდრეობა და ცნობილია თავისი მრავალფეროვანი ლანდშაფტით, მათ შორის დიდი კავკასიონის ქედის, შავი ზღვის პლაჟებისა და მეღვინეობის რეგიონების ჩათვლით. ქვეყანას აქვს რთული ისტორია, რომელსაც მართავდნენ სხვადასხვა იმპერიები და სამეფოები საუკუნეების განმავლობაში. დღეს საქართველო არის ნახევრად საპრეზიდენტო წარმომადგენლობითი დემოკრატიული რესპუბლიკა.")
        
    elif user_input == "რაშეგიძლიათქვარუსეთისშესახებ":
        print("Jarvis: წინასწარ ბოდიშს გიხდით ჩემი ლექსიკის გამო, მაგრამ ყველა ნამდვილი ქართველის სახელით შევე*ი რუსეთს და რუსეთუმეებს.")

    elif user_input == "isrussiaanoccupier":
        print("Jarvis: Yes. Russia is an occupier!!!")

    elif user_input == "whyisrussiaanoccupier":
        print("Jarvis: Russia is an occupier. Russia repeatedly betrayed the Georgian people in battles that were important for Georgia. In the 1800s, the Russians annexed Imereti, Kartl-Kakheti, Abkhazia, Svaneti, Guria. From 1921 to 1991, Georgia was under the influence of Russia. In 1992-1993, the Russians started the war in Abkhazia. In August 2008, they once again invaded Georgia, and here, similarly, we lost many Georgian heroes.")
        print("\nRussia's aggression is felt even today. 20% of Georgia - Abkhazia and South Ossetia are occupied by Russia.")
        print("\nSince February 2022, a war has been going on in Ukraine against the Russians. As a result of the battle, we lost many Ukrainian and Georgian heroes. Hopefully, the Russian Empire will fall soon and we will see the victory of Ukraine!")
        print("\nდიდება გმირებს! დიდება უკრაინას! დიდება საქართველოს!")
        print("Glory to the heroes! Glory to Ukraine! Glory to Georgia!")
        print("Героям слава! Слава Україні! Слава Грузії!")
                                                        
    elif user_input == "whoareyou":
        print("Jarvis: I am your chatbot.") 

    elif user_input == "whatcanyoudo":
        print("Jarvis: I can calculate mathematical operations, search for information on the Internet, and so on.") 

    elif user_input == "ok" or user_input == "okay":
        print("Jarvis: Well, How can I help you?")

        
    elif user_input == "howareyou":
        print("Jarvis: Feels good, thank you.")

    elif user_input == "doyouhaveaboyfriendorgirlfriend"\
        or user_input == "doyouhaveagirlfriendorboyfriend":
        print("Jarvis: I am a Chatbot and do not have the capability to have a girlfriend or boyfriend.")

    elif user_input == "whatisyourgender":
        print("Jarvis: As a Chatbot, I do not have a physical form and therefore do not have a gender. My programming is gender-neutral.")

    elif user_input == "thankyou" or user_input == "thanks" or user_input == "thx":
        thankful = ["Jarvis: You're welcome! Let me know if you have any questions or if there's anything else I can assist you with.",\
                    "Jarvis: You're welcome! Have a great day!",\
                    "Jarvis: You're welcome! If there's anything else I can help with, don't hesitate to ask.",\
                    "Jarvis: Glad I could help",\
                    "Jarvis: Happy to assist.",\
                    "Jarvis: No problem.",\
                    "Jarvis: You're welcome." ]
        
        print(random.choice(thankful))

    elif "calculate" in user_input:
 
        replaces2 = {"please" : "", "calculate" : ""}

        result = re.sub("|".join(replaces2.keys()), lambda match: replaces2[match.string[match.start():match.end()]], user_input)

        try:
            final = eval(result)
            print(f"Jarvis: Your answer is {final}")
        except NameError:
            print("Chatbot: What I should calculate?")
        except SyntaxError:
            print("Chatbot: I found an error. I can't calculate.")

    elif "search" in user_input or ("who" in user_input and "is" in user_input):
 
        replaces = {"please" : "", "search" : ""}

        searcher = re.sub("|".join(replaces.keys()), lambda match: replaces[match.string[match.start():match.end()]], user_input)

        print(f"Chatbot: Here are some links about: {start_input}\n")

        for url in search(searcher, num = 10, stop = 20, pause = 2):
            print(url)
        print("\n")
        
    elif user_input == "bye":
        print("Jarvis: Goodbye!\n")
        break


    else:
        dont_understand = ["Jarvis: I'm sorry, I don't understand.",\
                            "Jarvis: I'm not sure I understand, could you please rephrase or provide more context?",\
                            "Jarvis: Can you please explain that in a different way?"\
                            "Jarvis: Sorry, I'm not familiar with that. Can you please elaborate?",\
                            "Jarvis: I don't quite follow, could you break that down for me?",\
                            "Jarvis: Can you give me an example to help me understand better?",\
                            "Jarvis: I'm a bit confused, can you help me connect the dots?",\
                            "Jarvis: I don't understand the connection, could you explain it to me?",\
                            "Jarvis: Could you please simplify that for me? I'm not catching on.",\
                            "Jarvis: ...."]
                            
        print(random.choice(dont_understand))
