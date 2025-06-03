import sys
import os
import json
from duckduckgo_search import DDGS
import subprocess
from pathlib import Path

def search_web(topic):
    """Search the web for information about the topic."""
    print(f"🔍 Searching for information about {topic}...")
    
    with DDGS() as ddgs:
        # Get relevant search results
        results = list(ddgs.text(topic, max_results=5))
        
        # Combine the snippets into a context
        context = {
            "topic": topic,
            "search_results": [result["body"] for result in results],
            "sources": [result["href"] for result in results]
        }
        
        return context

def save_to_markdown(topic, explanation):
    """Save the explanation to a markdown file."""
    # Create results directory if it doesn't exist
    results_dir = Path("results")
    results_dir.mkdir(exist_ok=True)
    
    # Create the markdown file
    filename = f"{topic.lower().replace(' ', '_')}.md"
    filepath = results_dir / filename
    
    with open(filepath, "w") as f:
        f.write(f"# {topic}\n\n")
        f.write(explanation)
    
    return filepath.absolute()

def main():
    if len(sys.argv) < 4:
        print("Usage: python eli5_assistant.py \"your topic\" \"CLI\" or \"MD\" \"CONCISE\" or \"COMPREHENSIVE\"")
        return

    topic = sys.argv[1]
    output_format = sys.argv[2].upper()
    explanation_style = sys.argv[3].upper()

    if explanation_style not in ["CONCISE", "COMPREHENSIVE"]:
        print("Invalid explanation style. Please use 'CONCISE' or 'COMPREHENSIVE'.")
        return

    # Search the web for information
    context = search_web(topic)
    
    # Add explanation style to context
    context["explanation_style"] = explanation_style
    
    # Save context to file for the AI to process
    with open("context.json", "w") as f:
        json.dump(context, f, indent=2)

    # Call the AI processing script
    try:
        subprocess.run(["python", "send_to_claude.py"], check=True)
        
        # Read the processed explanation
        with open("context.json", "r") as f:
            result = json.load(f)
            explanation = result.get("explanation", "No explanation generated.")
        
        if output_format == "CLI":
            print("\n📝 Here's your explanation:\n")
            print(explanation)
        elif output_format == "MD":
            filepath = save_to_markdown(topic, explanation)
            print(f"\n✅ The {topic}.md file has been created inside {filepath}")
        else:
            print("Invalid output format. Please use 'CLI' or 'MD'.")
            
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return

if __name__ == "__main__":
    main() 