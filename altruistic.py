import random
import json
import pickle
import numpy as np
import sys
import nltk
from nltk.stem import WordNetLemmatizer
import os
import getpass
import tensorflow as tf
from components import split_str,google,youtube,cricket,weather
lemmatizer = WordNetLemmatizer()
intents = json.loads(open('./assets/intents.json').read())

words = pickle.load(open('words.pkl' , 'rb'))
classes = pickle.load(open('classes.pkl' , 'rb'))

model = tf.keras.models.load_model('chatbot_model.h5')

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words
def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i,word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)
def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key = lambda x:x[1] , reverse = True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]] , 'probability' : str(r[1])})
    return return_list
def get_response(intents_list , intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result
def check(bot_response,user_input):
    if bot_response == 'Redirecting to Google...':
        google.google_search(user_input)
        return ''
    elif bot_response == '...':
        resp = cricket.cricket_score()
        return resp
    elif bot_response == 'Here is the youtube video':
        print('yt section')
        youtube.yt_search(user_input)
        return
    elif bot_response == 'Weather Report - ':
        return weather.weather_today()
        
        
print('Bot is running!')

#App window
import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 600
WHITE = (144, 238, 144)
BLACK = (0, 0, 0)
FONT_SIZE = 15
FONT_COLOR = BLACK

# Create the Pygame screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Altruistic')

# Font
font = pygame.font.Font('./assets/times.ttf', FONT_SIZE)

# Text box
text_box = pygame.Rect(10, 550, 300, 30)
user_input = ""

# Send button
button_rect = pygame.Rect(320, 550, 50, 30)
button_color = (100, 100, 100)
button_text = "Send"

# Chat history
chat_history = []
max_visible_messages = 10  # Maximum visible messages
scroll_offset = 0

# Scrolling parameters
scroll_speed = 1
user_name = os.getlogin()

# Using getpass module
user_name = getpass.getuser()
# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                # Add user input to chat history and get a bot response
                chat_history.append((user_name, user_input))
                # Simulate a bot response (you can replace this with actual bot logic)
                ints = predict_class(user_input)
                bot_response = get_response(ints , intents)
                resp = check(bot_response,user_input)
                if resp == None:
                    resp = ''
                bot_response += resp
                chat_history.append(("Altruistic", bot_response))
                user_input = ""
            elif event.key == K_BACKSPACE:
                user_input = user_input[:-1]
            else:
                user_input += event.unicode

        if event.type == MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                # Add user input to chat history and get a bot response
                chat_history.append((user_name, user_input))
                # Simulate a bot response (you can replace this with actual bot logic)
                ints = predict_class(user_input)
                bot_response = get_response(ints , intents)
                bot_response = check(bot_response,user_input)
                if resp == None:
                    resp = ''
                bot_response += resp
                chat_history.append(("Altruistic", bot_response))
                user_input = ""

    screen.fill(WHITE)

    # Render text box
    pygame.draw.rect(screen, FONT_COLOR, text_box, 2)
    text_surface = font.render(user_input, True, FONT_COLOR)
    screen.blit(text_surface, (text_box.x + 5, text_box.y + 5))

    # Draw the Send button
    pygame.draw.rect(screen, button_color, button_rect)
    button_text_surface = font.render(button_text, True, WHITE)
    button_text_rect = button_text_surface.get_rect(center=button_rect.center)
    screen.blit(button_text_surface, button_text_rect)

    # Calculate the number of messages to display
    display_messages = chat_history
    print(display_messages)
    chat_y = 10

    # Render visible chat history
    for sender, message in display_messages:
        if len(message) > 35:
            list_message = split_str.split_string(message,50)
            c = 0
            for i in list_message:  
                text_surface = font.render(sender + ": " + i, True, FONT_COLOR)
                screen.blit(text_surface, (10, chat_y))
                chat_y += text_surface.get_height() + 5
        else:   
            text_surface = font.render(sender + ": " + message, True, FONT_COLOR)
            screen.blit(text_surface, (10, chat_y))
            chat_y += text_surface.get_height() + 5

    pygame.display.flip()

# Quit Pygame
pygame.quit()





    # message = input("")
    # ints = predict_class(message)
    # res =  get_response(ints , intents)
    # print(res)