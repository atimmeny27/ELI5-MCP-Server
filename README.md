# ELI5-Tool

This tool prompts Claude to explain any topic like you are 5, concept taken from the popular subreddit. It fetches content throguh an API key for the browser DuckDuckGo, and allows Claude to use the browser to search any sources it finds relevant. This is primarily a CLI program, but you can also make the explanations into a .md file.

---

## 🚀 Installation

To get started on macOS:

You will need a free API key from OpenRouter or another source, scroll to bottom after step 2 if you don't have a dedicated one for this project. 

1. Open **Terminal** (`⌘ + Space`, type `Terminal`, hit Enter).
2. Run the following commands:

```bash
git clone https://github.com/atimmeny27/ELI5-MCP-Server
cd ELI5-MCP-Server
chmod +x start.sh
```

4. Then
```bash
python3 -m ensurepip --upgrade
python3 -m pip install -r requirements.txt
clear
```

3. The tool is now verified, if you still need to setup an API go below. Anytime you wish to launch the program, enter

```bash
./start.sh
```

### 🔑 How to Get Your Free OpenAI API Key

To use this tool, you’ll need a free API key from OpenRouter (or OpenAI / Anothropic but this one is free). Follow these steps:

1. Sign Up or Log In

[Go to https://platform.openai.com/signup](https://openrouter.ai/)
➡️ Create an account or log in with Google/GitHub.

2. Generate an API Key
	•	After logging in, click your profile icon → “Keys”
	•	Click “Create Key” and copy the resulting string (starts with sk-or-...)
	•	Save it somewhere safe

3. Set Up Your Key Locally

4. To permanently keep this key active
```bash
touch ~/.zshrc 
open -e ~/.zshrc 
```
5. Then paste ```export OPENROUTER_API_KEY="your-key-here-starting-with-sk-"``` at the end of the file, and save it
6. Now paste ```source ~/.zshrc``` in your terminal or refresh the session. You can now start the tool with ```./start.sh```
