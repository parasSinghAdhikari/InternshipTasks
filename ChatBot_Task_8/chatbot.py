import speech_recognition as sr
import pyttsx3
import os
import platform
import datetime
import webbrowser


import random
import re

class RuleBasedChatbot:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()


        self.name = "RuleBot"
        self.greeting_responses = [
            "Hello! How can I help you today?",
            "Hi there! What's on your mind?",
            "Hey! Nice to meet you!",
            "Hello! I'm here to chat with you."
        ]
        
        self.goodbye_responses = [
            "Goodbye! Have a great day!",
            "See you later!",
            "Take care!",
            "Until next time!"
        ]
        
        self.default_responses = [
            "That's interesting! Tell me more.",
            "I'm not sure I understand. Can you rephrase that?",
            "Hmm, I don't have information about that.",
            "Could you be more specific?",
            "I'm still learning. What else would you like to know?"
        ]
    
    def speak(self,text):
        print("Assistant:", text)
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
            try:
                query = self.recognizer.recognize_google(audio)
                print("You:", query)
                return query.lower()
            except Exception:
                self.speak("Sorry, I didn't catch that.")
                return ""


    def clean_input(self, user_input):
        """Clean and normalize user input"""
        return re.sub(r'[^\w\s]', '', user_input.lower().strip())
    
    def respond(self, user_input):
        """Generate response based on user input using if-else logic"""
        cleaned_input = self.clean_input(user_input)
        
        # Greeting patterns
        if any(word in cleaned_input for word in ['hello', 'hi', 'hey', 'greetings']):
            return random.choice(self.greeting_responses)
        
        # Goodbye patterns
        elif any(word in cleaned_input for word in ['bye', 'goodbye', 'see you', 'quit', 'exit']):
            return random.choice(self.goodbye_responses)
        
        # How are you patterns
        elif 'how are you' in cleaned_input or 'how do you do' in cleaned_input:
            return "I'm doing well, thank you for asking! I'm just a simple chatbot, but I enjoy our conversation."
        
        # Name-related queries
        elif any(phrase in cleaned_input for phrase in ['your name', 'who are you', 'what are you']):
            return f"I'm {self.name}, a rule-based chatbot created with Python using if-else statements!"
        
        # Age-related queries
        elif 'how old' in cleaned_input or 'your age' in cleaned_input:
            return "I don't have an age like humans do. I was just created today!"
        
        # Weather queries
        elif 'weather' in cleaned_input:
            return "I don't have access to weather data, but I hope it's beautiful wherever you are!"
        
        # Time queries
        elif 'time' in cleaned_input or 'what time' in cleaned_input:
            return "I don't have access to real-time data, but you can check your device's clock!"
        
        # Help requests
        elif 'help' in cleaned_input:
            return """I can chat about various topics! Try asking me about:
- My name or what I am
- How I'm doing
- The weather
- Tell me a joke
- Or just say hello!"""
        
        # Joke requests
        elif 'joke' in cleaned_input or 'funny' in cleaned_input:
            jokes = [
                "Why don't scientists trust atoms? Because they make up everything!",
                "Why did the chatbot go to therapy? It had too many if-else issues!",
                "What do you call a chatbot that sings? A Dell!",
                "Why don't chatbots ever get tired? They run on endless loops!"
            ]
            return random.choice(jokes)
        
        # Thank you responses
        elif any(word in cleaned_input for word in ['thank', 'thanks']):
            return "You're welcome! I'm happy to help."
        
        # Yes/No responses
        elif cleaned_input in ['yes', 'yeah', 'yep', 'y']:
            return "Great! What would you like to talk about?"
        elif cleaned_input in ['no', 'nope', 'n']:
            return "No problem! Is there something else I can help you with?"
        
        # Compliments
        elif any(word in cleaned_input for word in ['good', 'great', 'awesome', 'nice', 'cool']):
            return "Thank you! I appreciate the kind words. What else can we chat about?"
        
        # Python or programming related
        elif any(word in cleaned_input for word in ['python', 'programming', 'code', 'coding']):
            return "I love Python! It's the language I was created with. Are you a programmer too?"
        
        elif "open notepad" in cleaned_input:
            os.system("notepad.exe")
            self.speak("Notepad opened.")
        elif "open calculator" in cleaned_input:
            if platform.system() == "Windows":
                os.system("calc.exe")
            elif platform.system() == "Darwin":
                os.system("open -a Calculator")
            else:
                os.system("gnome-calculator &")
                self.speak("Calculator opened.")
        elif "what time" in cleaned_input:
            now = datetime.datetime.now().strftime("%H:%M")
            self.speak(f"The time is {now}")
        elif "search file" in cleaned_input:
            filename = cleaned_input.replace("search file", "").strip()
            root_dir = "C:\\" if platform.system() == "Windows" else "/"
            for root, dirs, files in os.walk(root_dir):
                if filename in files:
                    self.speak(f"File found at {root}")
                    break
                else:
                    self.speak("File not found.")
        elif "web" in cleaned_input:
            self.speak("Opening your browser")
            webbrowser.open("https://www.google.com")
        
        elif "exit" in cleaned_input or "bye" in cleaned_input:
            self.speak("Goodbye! Have a nice day.")

        # Default response for unmatched inputs
        else:
            return random.choice(self.default_responses)

    def start_chat(self):
        """Main chat loop"""
        self.speak(f"🤖 {self.name}: Hello! I'm a rule-based chatbot. Type or say 'quit' or 'bye' to exit.")
        print("=" * 50)
        
        while True:
            self.speak("How can I help you? You can also type your question:")
            try:
                user_input = input("Type here or say something (press Enter to use voice):").strip()
                
                if not user_input:
                    user_input = self.listen()  
                if not user_input:
                    print("Please say or write something")
                    continue
                
                response = self.respond(user_input)
                print(f"🤖 {self.name}: {response}")
                
                # Check if user wants to quit
                if any(word in user_input.lower() for word in ['quit', 'exit', 'bye', 'goodbye']):
                    break
                    
            except KeyboardInterrupt:
                print(f"\n🤖 {self.name}: Goodbye! Thanks for chatting!")
                break
            except Exception as e:
                print(f"🤖 {self.name}: Sorry, I encountered an error. Let's keep chatting!")

# Create and run the chatbot
if __name__ == "__main__":
    chatbot = RuleBasedChatbot()
    chatbot.start_chat()
    