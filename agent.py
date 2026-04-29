import requests

# 1. OOP Concept: Creatin  modular Tool class
class WikipediaTool:
    def search(self, topic):
        # 2. API Integration: Wikipedia endpoint
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic}"
        
        # 3. Exception Handling: try/except block for network stability
        try:
            response = requests.get(url)
            response.raise_for_status() 
            
            # 4. JSON Parsin and Data Extraction
            data = response.json()
            if "extract" in data:
                return data["extract"]
            else:
                return "Error: No detailed summary found for this topic."
                
        except requests.exceptions.RequestException as e:
            return f"Network Error or Page Not Found: {e}"

# OOP Concept: Main Agent class in ordder to control the flow
class Agent:
    def __init__(self):
        self.wiki_tool = WikipediaTool()

    def run(self):
        print("=== AI Study Assistant ===")
        # Input handling
        topic = input("Enter a topic to research (e.g., Python_(programming_language)): ")
        print(f"\n[Agent] Fetching information about '{topic}'...\n")
        
        # Tool usage durin the execution step
        result = self.wiki_tool.search(topic)
        
        print("=== Results ===")
        print(result)
        print("===============")

if __name__ == "__main__":
    # Instantiatin the agent and then startin the workflow
    study_agent = Agent()
    study_agent.run()
