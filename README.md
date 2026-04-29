# 231ADB284-EgeBilgic-AI--and-Agent-Based-Python-System
231ADB284 Ege Bilgic, 24 April 2026, Applied System Software An AI-powered study assistant to research, summarize, and generate study guides for complex topics.
# AI Study Assistant - Project Journal for Applied System Software

## Step 1 (Submitted: April 24)

**1. Short description of the planned system and its goal:**
The planned system is a command-line "AI Study Assistant" built in using Python coding langauage and the actual main  goal of the system is to take a complex topic provided by the user just like History of Artificial Intelligence  and after that automatically generate a structured and factual study summary. It automates the initial research phase for students.

**2. Description of the AI or agentbased approach:**
The system will be implemented just like a single intelligent agent powered by Large Language Model (LLM) and also it will use a simple reasonin loop: it will receive the user's topic, decide what information it needs, use external tools to fetch that data, process the retrieved text, and finally synthesize the final study guide

**3. List of tools that will be used in the system:**
* **Wikipedia API / Web Search Tool:** Used by the agent to query and fetch realtime, factual information about the given topic.
* **File Writer Tool:**  utility that the agent uses to automatically save the final generated summary into a local text or Markdown (`.md`) file.

**4. Preliminary list of programmin concepts that will be required:**
* **Object-Oriented Programmin (OOP):** To define modular classes for the `Agent`, `Tool`, and `Task`.
* **API Integration:** Usin the `requests` library in Python in order to interact with  external search APIs and the LLM.
* **JSON Parsing:** To extract the necessary data from the API responses.
* **Error Handling:** Using `try/except` blocks to handle network errors or empty search results gracefully and easily.
