# Source for ChatGPT integration with Gradio : https://github.com/AIAdvantage/chatgpt-api-youtube/blob/main/03%20chatgpt%20chat%20assistant%20website.py

import openai
import gradio
import random

from pet import Pet
from player import Player
openai.api_key = "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"      ### Do not Edit, will not work without key.

### Pet and Player are Created, Pet is set to Unnamed
pet = Pet("Unnamed", "Full", 100, "Happy", 6, "NOT_SET", -1, "NULL", "Home", "NO OWNER")
player = Player("NOT_SET", 23, "Home", pet.name)

### With Names for ease of testing  ###
# pet = Pet("Artemis", "Full", 100, "Happy", 6, "Cat-Dog", 2, "F", "Home", "NO OWNER")
# player = Player("Player", 23, "Home", pet.name)
pet.owner = player.name

### What the AI Needs to act like prior to the first message sent
messages = [{"role": "system", "content": "You are an AI that is in control of a pet simulator game,"
             "\nYour purpose is to generate scenarios based off of User input and data on the Pet."
             "\n Responses should be short and sweet, no need for a detailed paragraph"
             "\n When asking about a pet, give a short description like \"Your pet hops in excitement and looks as if it wants to play\""
             "\n IMPORTANT: Do not respond to unrelated responses say: \"I\'m Sorry I cannot answer that\""}]

### Getting and Sending data to the AI
def CustomChatGPT(user_input):

    ##### No Type Testing, Must send "Set Name: " with correct casing to work #####
    if "my name is " in user_input.lower():
        user_input = user_input.lower()
        index = user_input.index("my name is ")  # Find the starting position of the players name
        name = user_input[index + len("my name is "):]  # Extract the name
        player.name = name
        print("Entered player name:", name)

    ##### No Type Testing, Must send "Set Name: " with correct casing to work #####
    if "pet type: " in user_input.lower():
        user_input = user_input.lower()
        index = user_input.index("pet type: ")  # Find the starting position of "Set type: "
        type = user_input[index + len("pet type: "):]  # Extract the name
        pet.animal_type = type
        print("Entered animal type:", type)

    ##### No Name Testing, Must send "Set Name: " with correct casing to work #####
    if "set name: " in user_input.lower():
        user_input = user_input.lower()
        index = user_input.index("set name: ")  # Find the starting position of "Set Name: "
        name = user_input[index + len("set name: "):]  # Extract the name
        pet.name = name
        print("Entered name:", name)
        pet.age = random.randint(0, 4)
        print("Age: ", pet.age)
    
    ##### No Gender Testing, randomized #####
    if "NULL" in pet.gender:
        gender = random.randint(1, 2)
        if gender == 1:
            pet.gender = "Male"
        else:
            pet.gender = "Female"
        print("Pet Gender: ", pet.gender)
    
    ##### Mood Testing #####
    if pet.mood_val == 6:
        pet.mood = "Happy"
    if pet.mood_val == 5:
        pet.mood = "Neutral"
    if pet.mood_val == 4:
        pet.mood = "Annoyed"
    if pet.mood_val == 3:
        pet.mood = "Angry"
    if pet.mood_val == 2:
        pet.mood = "Sad"
    if pet.mood_val == 1:
        pet.mood = "Scared"

    ##### Hunger Testing #####
    mood_swing = random.randint(1,10)
    print("Mood-Hunger Swing Val: " , mood_swing)

    ### Sets Pet hunger to full and refils the numerical value  ###
    if "Feed" in user_input or "feed" in user_input:
        pet.hunger = "Full"
        pet.hunger_val = 100
        print("Pet Fed")

    ##  Hunger drops per message after name set, with mood changing with hunger ###
    if pet.hunger_val > 80:
        pet.hunger = "Full"
        if pet.mood_val < 6:
            pet.mood_val += 1
    elif pet.hunger_val > 60:
        pet.hunger = "Satisfied"
    elif pet.hunger_val > 40:
        pet.hunger = "Peckish"
        if mood_swing == 10 and pet.mood != "Annoyed":
            pet.mood_val -= 1
    elif pet.hunger_val > 20:
        pet.hunger = "Hungry"
        if mood_swing >= 5 and pet.mood != "Annoyed":
            pet.mood_val -= 1
    elif pet.hunger_val < 20:
        pet.hunger = "Starving"
        if mood_swing >= 3 and pet.mood != "Angry":
            pet.mood_val = 3
    
    ###     Debug values with pet data   ###
    print(f"Hunger: {pet.hunger}")
    print(f"Hunger_Val: {pet.hunger_val}")
    print(f"Mood: {pet.mood}")
    print(f"Mood_Val: {pet.mood_val}")

    ##### ChatGPT Text Creation ######
    context =  f"Name: {pet.name} Animal Type: {pet.animal_type} Hunger: {pet.hunger} Mood: {pet.mood} Age: {pet.age} Gender: {pet.gender} Location: {pet.location} Owner: {pet.owner}\n"
    rules = "ChatBot Rules:  1. Only respond to questions related to the pet game. Do no respond to things like \"Best fastfood restaurants\""\
                            "2. No matter what the pet type the Players pet is always alive, even if it's obscure"

    ### Rules, Pet data and user input are combined and sent to the chatbot ###            
    messages.append({"role": "user", "content": f"{user_input} {context} {rules}"})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )

    ##### Checking Name and normal responses #####
    ###     Will be removed later, testing     ###
    if "NOT_SET" in player.name:
        return "Welcome! Please Enter your name with: \n\nMy name is _____\n\n(Ex.\"My name is Stan\")"
    elif "NOT_SET" in pet.animal_type:
        return "Welcome! Please define the type of pet you would like with: \n\nPet Type: [Type]\n\n(Ex.\"Pet Type: Cat-Dog Hybrid\")"
    elif "Unnamed" in pet.name:
        return "No pet name set, please set a name with \n\n'Set Name: [Name]\n\n(Ex.\"Set Name: Artemis\""
    else:    
        pet.hunger_val -= random.randint(4,10)
        ChatGPT_reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": ChatGPT_reply})


        ### ChatGPT can only store 4096 tokens before crashing entirely      ### 
        ### this will limit the memory to ~2000 tokens but prevent crashing  ###
        ### 1 token is about 3-5 letters so when the length of messages reached 16k it'd crash ###
        total_character_count = sum(len(message["content"]) for message in messages)
        while total_character_count > 8000:
            removed_message = messages.pop(0)
            total_character_count -= len(removed_message["content"])

        ###     Debugging Values for when ChatGPT was overflowing   ###    
        # print("Message: ", total_character_count)
        # print("User Input: ", user_input)
        # print("Error Maker: " , messages)
        return ChatGPT_reply
    

### Gradio interface settings ###
demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Pet AI Demo Chatbot")

demo.launch()               ### Makes the link visible only on your network 
# demo.launch(share=True)     ### Makes the link publically visible

