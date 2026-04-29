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
* **Error Handlin:** Usin `try/except` blocks in order to directly and easily handle network errors or empty search results in very gracefully and easily way.


---

## Step 2 (Submitted: April 30)

**1. Updated description of the system based on implementation progress:**
The "AI Study Assistant" is currently in the active implementation phase dear sir and the core project folder structure has been already fully set up. The system successfully takes a user's topic input and initiates the research process. I have already started buildin the core logic where the assistant interacts with the external Wikipedia API to gather initial facts before formattin them.

**2. Refined list of programming concepts actually used:**
* **Object-Oriented Programmin (OOP):** Applied through modular class creation.
* **HTTP Requests & API Integration:** Usin the `requests` library in Python section.
* **JSON Parsin & Data Extraction:** Manipulatin dictionary data structures.
* **Exception Handlin:** Usin `try/except` blocks for network stability and consistency.

**3. Explanation of how these concepts are applied in your project:**
* **OOP:** Sir,firstly i just created a `WikipediaTool` class which encapsulates the search logic  and also an `Agent` class that manages the overall flow because it helps so much to keep the code very clean and modular way
* **API Integration:** The `requests.get()` function is used to send HTTP requests directly to  Wikipedia API endpoints in a very secure way.
* **JSON Parsin:** The external API returns data in JSON format and code parses this into Python dictionaries to extract just the relevant summary text, ignorin unnecessary metadata.
* **Exception Handlin:** `try/except` blocks are placed around the API calls in order to successfully prevent the program from crashin if there is no internet connection or if the search topic returns no results erro.

**4. Description of how tools are integrated into the system:**
The Wikipedia search tool is fully integrated as an independent module and when the user provides a topic, then  main agent script instantiates the `WikipediaTool` class and calls its `search(topic)` method becase this method builds the correct URL parameters, makes the API request, extracts the plain text summary from the JSON response, and returns it to the main agent to process into the further steps.
