import nltk


def built_in_engines(which_one: str):
    if which_one == 'eliza':
        nltk.chat.eliza.demo()
    elif which_one == 'iesha':
        nltk.chat.iesha.demo()
    elif which_one == 'rude':
        nltk.chat.rude.demo()
    elif which_one == 'suntsu':
        nltk.chat.suntsu.demo()
    elif which_one == 'zen':
        nltk.chat.zen.demo()
    else:
        print("No such engine: ", which_one)


def my_engine():
    chatpairs = (
        (r"(.*?)Stock price(.*)",
         ("Today stock price is 100",
            "I am unable to find out the stock price.")),
        (r"(.*?)not well(.*)",
            ("Oh, take care. May be you should visit a doctor",
            "Did you take some medicine ?")),
        (r"(.*?)raining(.*)",
            ("Its monsoon season, what more do you expect ?",
            "Yes, its good for farmers")),
        (r"How(.*?)health(.*)",
            ("I am always healthy.",
            "I am a program, super healthy!")),
        (r".*",
            ("I am good. How are you today ?",
            "What brings you here ?"))
    )

    def chat():
        print("!"*80)
        print(">> My name is Chatterbot and I'm a chatbot.")
        print(">> I like to chat and make friends.")
        print(">> Please type lowercase English language to start a conversation. Type quit to leave ")
        print("!"*80)
        print("Hi")
        chat = nltk.chat.util.Chat(chatpairs, nltk.chat.util.reflections)
        chat.converse()
    chat()


def main():
    for engine in ["eliza", "iesha", "rude", "suntsu", "zen"]:
        print("Downloading engine: ", engine)
        built_in_engines(engine)
        print()
    my_engine()


if __name__ == "__main__":
    main()
