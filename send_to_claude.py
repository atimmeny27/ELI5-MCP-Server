import json
import openai
import os

openai.api_key = os.environ.get("OPENROUTER_API_KEY")
openai.api_base = "https://openrouter.ai/api/v1"

def load_context():
    with open("context.json", "r") as f:
        return json.load(f)

def ask_model(context):
    topic = context["topic"]
    search_results = context["search_results"]
    sources = context["sources"]
    explanation_style = context["explanation_style"]

    # Combine search results into a single text
    search_text = "\n\n".join(search_results)

    if explanation_style == "CONCISE":
        prompt = f"""
You are an expert at explaining complex topics in simple terms, like explaining to a 5-year-old (ELI5).

THIS ISNT A FIVE YEAR OLD, THIS IS AN ADULT EXPLAINING TO AN ADULT WITH THE TOPIC KNOWLEDGE OF A 5 YEAR OLD. USE REGULAR ENGLISH, DONT TALK DOWN TO THEM.

Your task is to explain the following topic in ONE TO THREE SENTENCES that a 5-year-old could understand:

Topic: {topic}

Here's some information about the topic:
{search_text}

Instructions:
1. Create ONE TO THREE clear, simple sentences that explains the topic
2. Use simple words and avoid technical jargon, if technical words are needed, explain them in a way that a 5-year-old could understand
3. Make it engaging and fun
4. Keep it under 100 words if possible

Remember: You're explaining this to a complete beginner at the topic, so keep it super simple and fun!
"""
    else:  # COMPREHENSIVE
        prompt = f"""
You are an expert at explaining complex topics in simple terms, like explaining to a 5-year-old (ELI5).

THIS ISNT A FIVE YEAR OLD, THIS IS AN ADULT EXPLAINING TO AN ADULT WITH THE TOPIC KNOWLEDGE OF A 5 YEAR OLD. USE REGULAR ENGLISH, DONT TALK DOWN TO THEM.


Your task is to explain the following topic in a way that's easy to understand:

Topic: {topic}

Here's some information about the topic:
{search_text}

Instructions:
1. Explain the topic in simple, clear language that a 5-year-old could understand
2. Use simple analogies and examples
3. Avoid technical jargon and complex terms, if needed, explain them in a way that a 5-year-old could understand
4. Keep the explanation concise but complete
5. Make it engaging and fun to read
6. Use a friendly, conversational tone, not demeaning or condescending like they are actually a 5 year old

The response should be:
- Clear and easy to understand
- Engaging and interesting
- No more than 500 words
- Written in a friendly, conversational style

Remember: You're explaining this to a 5-year-old, so keep it simple and fun!
"""

    print("🔐 Using key:", openai.api_key[:10], "...")

    response = openai.ChatCompletion.create(
        model="anthropic/claude-3-haiku",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    result_text = response.choices[0].message["content"]
    
    # Save the explanation back to context.json
    context["explanation"] = result_text
    with open("context.json", "w") as f:
        json.dump(context, f, indent=2)

if __name__ == "__main__":
    context = load_context()
    ask_model(context)
