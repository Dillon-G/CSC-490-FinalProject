# User manual for Pet AI
This is the user manual for Team L[AI]on's PetAI, the program currently features OpenAI integration to allow for a chatbot AI to drive a text based game forward, an image generation AI to allow for the user to see the pet they want and a web application to bring everything together.<br>
When running the program please take note that a specific version of OpenAI must be pip installed, this can be done with the following pip command: `pip install openai==0.28`<br>
<br>
## Setup
Within `AI_Chatbot.py` as well as `Image_Generator.py` there exists a line that must be filled out with the users OpenAI API key. 
<br><ins>This key is required to allow the chatbot and image generation to run.</ins>
<br><ins>Currently there is a temporary key in place which will expire around December 10th, 2023.</ins>
<br>The key can be entered here in `AI_Chatbot.py`<br>
![image](https://github.com/Dillon-G/CSC-490-FinalProject/assets/111513711/11170fe3-7064-4b41-b89b-75ca85d2ca54)
<br>And then here in `Image_Generator.py`<br>
![image](https://github.com/Dillon-G/CSC-490-FinalProject/assets/111513711/b1401560-c08a-4010-af7f-1ce10dc88e75)

Next it should be noted that in the final version we were able to get out we managed to allow generated images to display after a web page refresh. However, the method used wasn't properly tested and when called it causes the AI Chatbot to never regain control, thus preventing the experience from moving forward.
<br>The feature is currently disabled. The feature can be tested by having the subprocess on line 210 enabled like follows:<br>![image](https://github.com/Dillon-G/CSC-490-FinalProject/assets/111513711/ca4cb318-bb51-4091-b16c-d8408036fe5e)
<br>It should be noted that the current build has it commented out, if the user wishes to have their pet displayed while playing with the chatbot then please move to [this section of the manual](#pet-setup).

## The Web Application
The web application can be opened through the "Mainpage.html" file, without the chatbot or image generator running it will only display a page that holds containers for each of the previously mentioned.<br>
When functional, the web application will display the Chatbot AI first, and after going through the initial user set up process from the chatbot will display the image generated after a page refresh.<br>

## The AI Image generator
The AI Image generator will run after the user is prompted for, and fills out, the "Pet Type: " prescripted message in the chatbox.
<br> Once filled out, the image generator accesses OpenAI's image database, with our given instructions and the users pet description to generate a pet to the best of it's abilities. The image generator will output a link directly to the console of the program which, when fully functional, should display directly to the page for the user.
## The AI Chatbot
The Chatbot is the driving force of the program and needs to be broken into a few chapters.
### Pre-Game
The user will be shown 3 prescripted messages before the game can begin. The first requesting their name, the program currently takes in the first name of the user to allow for children to easily access the game. The second requests the kind of pet they would like, this can be anything from a dog to a dragon or even a hybrid cat with wings. Finally the user will be asked to name their pet, which will act similar to how the player named themselves. 
<br>
### Playing normally
When playing the game normally, there are restrictions for the chatbot in place, such as avoiding talking about unrelated topics and any rule OpenAI has in place. However for the player their only restriction is their imagination as the driving force of the game is the users responses.<br>
The user should keep in mind that the pet does have a hunger level that the chatbot will subtly tell them if requested. However if the user neglects their pet it will become more and more angry if it's hunger drops too low. Specific states have differing chances for the happiness to drop.
<br> The Pet's happiness will move from **Happy->Neutral->Annoyed->Angry given lack of feeding**
<br>`Hunger: Peckish - 10% per message to lower the pet's happiness by 1 level`
<br>`Hunger: Hungry - 70% per message to lower the pet's happiness by 1 level`
<br>`Hunger: Starving - 100% per message to lower the pet's happiness to angry due to neglect`
<br>A Pet's hunger can be restored to full if the user types a message including the keyword "feed"(Ex. _I feed Artemis some steak_.) This will not make the pet happy immediately, a pet with a full belly will slowly regain happiness by 1 level per message sent and <ins>an angry pet will refuse to play.</ins>
### Behind the scenes
Playing with the pet can be super fun as the AI seems to allow you to play any game and visit nearly anywhere.
<br>Some things to be noted is that when the AI or User respond, a logic check is ran to scan for keywords to allow for data updates, such as location, feeding of the pet, naming and rules for the AI itself.
<br>If the terminal is open during play, the user will be able to see that multiple pieces of pet data are on display including updates when they happen.
<br>When the user sends a message a set of rules and chunk of tesxt containing pet data is appended to their message to send relevant data to the AI, this is not shown to the user and their message is still sent as is.
<br>The chatbot runs on a charge-per-token system and appending messages that continuously grow in size is hard on response generation as well as charges the owner of the key more and more. As such a failsafe is put in place to limit the appended chat history from exceeding 1000 tokens, which is about 4000 characters. If the chatbot reaches a token send/recieve limit of 4096 tokens (16k characters) it ultimately crashes due to a policy on OpenAI preventing the size of such messages.
<a id="pet-setup"></a>
## Seeing your pet through manual input
When running the program, one of the initial prescripted questions will ask the user to enter a "pet type." When this line is filled out with non-illegal terms the pet image generator is called and will generate an image. The image is hosted on a temporary url which will be displayed in the terminal.<br>
Taking this link, move to the mainpage.html file and replace the URL `http://127.0.0.1:5000/image_gen`.
![image](https://github.com/Dillon-G/CSC-490-FinalProject/assets/111513711/21c4ac0c-a518-41b7-ac93-b447c3f1f7d5)
<br> When the link is in place refresh the page, this should allow the user to see their pet while talking with the AI Chatbot. The visible message history with the chatbot will be gone, however it is saved internally so the bot will act the same regardless of page refreshes.
