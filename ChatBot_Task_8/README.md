# RuleBot - Advanced Voice & Text Chatbot

A Python-based rule-based chatbot with both text and voice interaction capabilities, plus basic operating system task automation.

## Features

### 🗣️ Voice & Text Interaction
- **Text Input**: Type messages directly in the terminal
- **Voice Input**: Press Enter without typing to use voice recognition
- **Voice Output**: The bot speaks all responses using text-to-speech
- **Hybrid Mode**: Switch between text and voice seamlessly

### 🤖 Conversational Abilities
- Greeting and farewell responses
- Basic conversation (how are you, name, age)
- Weather inquiries (general responses)
- Joke telling with built-in humor
- Help and guidance
- Programming-related discussions
- Thank you acknowledgments
- Yes/No response handling

### 💻 Operating System Tasks
- **Open Applications**: Launch Notepad, Calculator
- **Time Information**: Get current system time
- **File Search**: Search for files across the system
- **Web Browser**: Open default browser with Google
- **Cross-Platform**: Works on Windows, macOS, and Linux

## Prerequisites

Install the required Python packages:

```bash
pip install speechrecognition pyttsx3 pyaudio
```

**Note**: On some systems, you may need additional packages:
- Windows: Usually works out of the box
- macOS: May require `brew install portaudio`
- Linux: May require `sudo apt-get install python3-pyaudio`

## Installation

1. Clone or download the `chatbot.py` file
2. Install the dependencies listed above
3. Run the script:

```bash
python chatbot.py
```

## Usage

### Starting the Chatbot
Run the script and the bot will greet you. You have two interaction options:

1. **Type your message** and press Enter
2. **Press Enter without typing** to use voice input

### Example Commands

#### Basic Conversation
- "Hello" / "Hi" / "Hey"
- "How are you?"
- "What's your name?"
- "Tell me a joke"
- "Thank you"

#### Operating System Tasks
- "Open notepad"
- "Open calculator" 
- "What time is it?"
- "Search file [filename]"
- "Open web browser"

#### Exit Commands
- "Bye" / "Goodbye"
- "Quit" / "Exit"
- Press Ctrl+C

## Code Structure

### Main Class: `RuleBasedChatbot`

#### Key Methods:
- `__init__()`: Initialize TTS engine, speech recognizer, and response templates
- `speak(text)`: Convert text to speech and display in terminal
- `listen()`: Capture and process voice input using Google Speech Recognition
- `clean_input(user_input)`: Normalize and clean user input
- `respond(user_input)`: Main logic engine using if-else statements for intent detection
- `start_chat()`: Main conversation loop handling both text and voice input

#### Response Categories:
- **Greetings**: Random selection from greeting templates
- **Farewells**: Random selection from goodbye templates  
- **Information**: Name, age, capabilities
- **Utilities**: Time, weather, file search
- **Entertainment**: Jokes, compliments
- **System Tasks**: Application launching, web browsing
- **Fallback**: Default responses for unrecognized input

## Customization

### Adding New Responses
Add new elif conditions in the `respond()` method:

```python
elif 'your_keyword' in cleaned_input:
    return "Your custom response"
```

### Adding OS Tasks
Extend the OS task section with new commands:

```python
elif "your_command" in cleaned_input:
    os.system("your_system_command")
    self.speak("Task completed")
```

### Modifying Response Templates
Edit the response lists in `__init__()`:

```python
self.greeting_responses = [
    "Your custom greeting",
    "Another greeting option"
]
```

## Security Considerations

⚠️ **Important**: This chatbot executes system commands. Be cautious when:
- Adding new OS task commands
- Running on production systems
- Allowing untrusted users to interact with it

## Cross-Platform Compatibility

The chatbot includes platform detection for:
- **Windows**: Uses `notepad.exe`, `calc.exe`
- **macOS**: Uses `open -a Calculator`
- **Linux**: Uses `gnome-calculator`

## Troubleshooting

### Voice Recognition Issues
- Ensure microphone permissions are granted
- Check microphone functionality
- Verify internet connection (Google Speech Recognition requires internet)

### Audio Output Issues
- Verify system audio is working
- Check TTS engine installation
- Try adjusting system volume

### Module Installation Issues
- Use `pip3` instead of `pip` on some systems
- Try installing with `--user` flag
- Check Python version compatibility (3.6+)

## Future Enhancements

Potential improvements:
- Add more sophisticated natural language processing
- Implement offline speech recognition
- Add more OS automation capabilities
- Include API integrations (weather, news, etc.)
- Add conversation history and context awareness
- Implement user preference learning

## License

This project is provided as-is for educational and personal use.

---

**Note**: This is a rule-based chatbot using if-else logic. For more advanced conversational AI, consider implementing machine learning models or integrating with AI APIs.