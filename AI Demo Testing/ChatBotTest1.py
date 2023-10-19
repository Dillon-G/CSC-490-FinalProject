# Source : https://github.com/AIAdvantage/chatgpt-api-youtube/blob/main/03%20chatgpt%20chat%20assistant%20website.py

# import sys
# print(sys.executable)

import openai
import gradio
import random

from pet import Pet
from player import Player
openai.api_key = "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"      ### Do not Edit, will not work without key.

### Pet and Player are Created, Pet is set to Unnamed
pet = Pet("Unnamed", "Full", 100, "Happy", "Cat-Dog", 2, "F", "Home", "NO OWNER")
player = Player("Player", 23, "Home", pet.name)
pet.owner = player.name

### What the AI Needs to act like prior to the first message sent
messages = [{"role": "system", "content": "You are an AI that is in control of a pet simulator game,"
             "\nYour purpose is to generate scenarios based off of User input and data on the Pet."
             f"\nHere is the current Pet Data: "
             f"\nName: {pet.name} Hunger: {pet.hunger} Mood: {pet.mood} Location: {pet.location} Animal Type: {pet.animal_type} Age: {pet.age} Owner: {pet.owner} Gender: {pet.gender}"
             f"\nHere is the current Player Data: "
             f"\nName: {player.name}"
             "\n Responses should be short and sweet, no need for a detailed paragraph"
             "\n When asking a pet, give a short description like \"Your pet hops in excitement and looks as if it wants to play\""}]

### Getting and Sending data to the AI
def CustomChatGPT(user_input):

    ##### No Name Testing, Must send "Set Name: " with correct casing to work #####
    if "Set Name: " in user_input:
        index = user_input.index("Set Name: ")  # Find the starting position of "Set Name: "
        name = user_input[index + len("Set Name: "):]  # Extract the name
        pet.name = name
        print("Entered name:", name)
    
    ##### Hunger Testing #####
    ##  Hunger drops per message after name set ###
    if pet.hunger_val > 80:
        pet.hunger = "Full"
    elif pet.hunger_val > 60:
        pet.hunger = "Satisfied"
    elif pet.hunger_val > 40:
        pet.hunger = "Peckish"
    elif pet.hunger_val > 20:
        pet.hunger = "Hungry"
    elif pet.hunger_val < 20:
        pet.hunger = "Starving"
    print(f"Hunge: {pet.hunger}")
    print(f"Hunger_Val: {pet.hunger_val}")

    ### Sets Pet hunger to full and refils the numerical value  ###
    if "Feed" in user_input or "feed" in user_input:
        pet.hunger = "Full"
        pet.hunger_val = 100
        print("Pet Fed")
    

    ##### ChatGPT Text Creation ######
    context =  f"Name: {pet.name}Animal Type: {pet.animal_type}Hunger: {pet.hunger}Mood: {pet.mood}Age: {pet.age}"
    messages.append({"role": "user", "content": f"{user_input} {context}"})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    
    ##### Checking Name and normal responses #####
    if "Unnamed" in pet.name:
        return "No pet name set, please set a name with 'Set Name: [Name]"
    else:    
        pet.hunger_val -= random.randint(4,10)
        ChatGPT_reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": ChatGPT_reply})
        return ChatGPT_reply
    
### Gradio interface settings ###
demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Pet AI Demo Chatbot")

demo.launch()               ### Makes the link visible only on your network 
# demo.launch(share=True)     ### Makes the link publically visible


#####   Code    Graveyard   #####
    # name_check = "pet name"
    # if name_check in response:
    #     print("Found 'pet name'")
    # else:
    #     print("Not found 'pet name'")