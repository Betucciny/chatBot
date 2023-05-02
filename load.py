import tensorflow as tf
import numpy as np
import pickle



def main():
    with open("chatbot.pickle", "rb") as archivo:
        chatbot = pickle.load(archivo)
    chatbot.interactive_mode()
