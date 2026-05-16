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
* **Exception Handlin:** `try/except` blocks are placed around the API calls in order to successfully prevent the program from crashin if there is no internet connection or if the search topic returns no results error.


---

## Step 3 (Submitted: May 15)

**1. Description of the testin process:**
Testin is performed using Python's built-in `unittest` framework and thetesting process focuses fully on verifying core functionality of the `WikipediaTool` in order to ensure it correctly interacts with the external API and also can handle successful responses, and aditionally safely manages errors without crashin the main application at all.

**2. List and explanation of test scenarios:**
* **Test Scenario 1: Valid Topic Search (Functional Testin):** Tests if the tool correctly fetches and returns a summary when a valid topic (e.g., "Python_(programming_language)") is provided and then xpected result: A string containing the summary text.
* **Test Scenario 2: Invalid/Non-existent Topic (Error Handlin):** Tests how system behaves when the user inputs gibberish or a non-existent Wikipedia page and also expected result: The system catches the HTTP error and returns a safe error message string rather than crashin.

**3. Short explanation of deployment preparation (how the system can be run):**
The system is designed as a command-line tool and in order to operate and run it,  user needs Python installed at first and user also nneds to have required external dependencies such as the `requests` library will be listed in a `requirements.txt` file and so user will simply install the dependencies using `pip install -r requirements.txt` and then launch the program just y typin `python agent.py` in their own specific terminal

**4. Short explanation of data conversion or porting:**
Data conversion happens when interacting with the Wikipedia API. The API returns back data in very structured JSON format, which includs a lot of unnecessary metadata after that `WikipediaTool` receives this JSON, parses it into a Python dictionary, isolates the specific `"extract"` key which holds the plain text and after that converts/ports it into a clean, raw string format. This ensures the main Agent only receives the exact text it needs to display to the user, maintaining data consistency

---

## Final Submission (Submitted: May 16)

**1. Final version of this system description and its actual cleargoal:**
Firstly this AI Study Assistant is now a ully functional command-line Python application and its actual and main goal is to automate the initial phase of academic research and to be honest it successfully takes a user-defined complex topic, autonomously queries an external knowledge base, and returns a concise, factual summary directly to the terminal very extremely fas. 

**2. Final explanation of programming concepts and their usage:**
* **Object-Oriented Programming (OOP):** I just directly used it to structure the code logically. Additionally `WikipediaTool` handles external communication, while the `Agent` manages the application lifecycle and user interaction all at the same timing.
* **API Integration & HTTP Requests:** The `requests` library is used to perform GET requests to the Wikipedia REST API
* **JSON Parsing:** Used to extract the `"extract"` text field from API's JSON response payload
* **Error Handling:** `try/except` blocks ensure that network failures or missin pages do not crash the application, providin user friendly type of error messages instead
* **Unit Testing:** Python's `unittest` framework is used in order to clearly validate the tool's behavior under both normal and edgecase type of conditions

**3. Final description of tools and their role in the system:**
primary tool integrated into this system is  **Wikipedia API Search Tool** and clearly its role is extremely quite critical since it acts as the agent's bridge to the outside world, allowing it to retrieve real-time, factual data based on dynamic user input. 

**4. Final testing results and conclusions:**
The testing phase was completed successfully usin the `test_agent.py` script and then the functional test (`test_valid_search`) passed, proved that the tool correctly fetches and parses valid JSON data and also  error handling test (`test_invalid_search`) also passed, confirmin that invalid inputs return a safe error string instead of a system crash. 
Conclusion: The system is quite stable consistent, error-resistant, and ready for actual real world usage.

**5. Final deployment preparation description:**
The system is prepared for local deployment ans then i have just added  `requirements.txt` file to the repository because of the rrason that a  new user simply needs to clone the repository, run `pip install -r requirements.txt` in order to install dependencies, and then start the assistant by runnin `python agent.py` in their own specific terminal

**6. Short explanation of the chosen deployment strategy:**
The most suitable deployment strategy for this solution is a **Command-Line Tool** by far because it is very lightweight and exactly designed for quick research tasks, deploying it as a local CLI application is highly efficient so users can so easily run it in their terminal without needing a heavy web server or interface.

**4. Description of how tools are integrated into the system:**
The Wikipedia search tool is fully integrated as an independent module and when the user provides a topic, then  main agent script instantiates the `WikipediaTool` class and calls its `search(topic)` method becase this method builds the correct URL parameters, makes the API request, extracts the plain text summary from the JSON response, and returns it to the main agent to process into the further steps.
