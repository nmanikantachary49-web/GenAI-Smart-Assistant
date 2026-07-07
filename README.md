# Generative-AI-Web-Application-using-Ollama-and-LangChain
<h1 align="center">🤖 Generative AI Web Application using Ollama and LangChain</h1>

<p align="center">
  <b>A modern AI chatbot web application built with Flask, LangChain, and Ollama using the Gemma 2B local LLM.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Flask-Web_App-black?style=for-the-badge&logo=flask">
  <img src="https://img.shields.io/badge/LangChain-Framework-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Ollama-Local_LLM-orange?style=for-the-badge">
</p>

<hr>

<h2>📌 Project Overview</h2>

<p>
This project is a <b>Generative AI Web Application</b> that allows users to ask questions and receive intelligent AI-generated responses through a clean and modern web interface.
</p>

<p>
The application uses <b>Flask</b> for the backend, <b>LangChain</b> for prompt management and LLM pipeline creation, and <b>Ollama</b> to run the <b>Gemma 2B</b> model locally.
</p>

<p>
Unlike cloud-based AI applications, this project runs the language model on the local system using Ollama, making it useful for learning how local LLM applications work.
</p>

<hr>

<h2>🚀 Key Features</h2>

<ul>
  <li>Interactive AI chatbot web interface</li>
  <li>Uses local LLM through Ollama</li>
  <li>Integrated with LangChain prompt templates</li>
  <li>Built using Flask backend</li>
  <li>Modern and responsive frontend UI</li>
  <li>No external API key required</li>
  <li>Beginner-friendly GenAI project</li>
</ul>

<hr>

<h2>🧠 Technologies Used</h2>

<table>
  <tr>
    <th>Technology</th>
    <th>Purpose</th>
  </tr>
  <tr>
    <td><b>Python</b></td>
    <td>Main programming language</td>
  </tr>
  <tr>
    <td><b>Flask</b></td>
    <td>Backend web framework</td>
  </tr>
  <tr>
    <td><b>HTML & CSS</b></td>
    <td>Frontend design and layout</td>
  </tr>
  <tr>
    <td><b>LangChain</b></td>
    <td>LLM orchestration and prompt pipeline</td>
  </tr>
  <tr>
    <td><b>Ollama</b></td>
    <td>Runs the local language model</td>
  </tr>
  <tr>
    <td><b>Gemma 2B</b></td>
    <td>Local large language model used for responses</td>
  </tr>
</table>

<hr>

<h2>🏗️ Project Architecture</h2>

<pre>
User
 │
 │ Enters a question
 ▼
Frontend HTML Form
 │
 │ Sends POST request
 ▼
Flask Backend
 │
 │ Passes question to LangChain prompt
 ▼
LangChain Chain
 │
 │ Sends prompt to Ollama
 ▼
Gemma 2B Model
 │
 │ Generates response
 ▼
Flask renders response on webpage
</pre>

<hr>

<h2>📂 Project Structure</h2>

<pre>
Generative-AI-Web-Application-using-Ollama-and-LangChain/
│
├── index.py
├── requirements.txt
├── templates/
│   └── new.html
└── README.md
</pre>

<hr>

<h2>⚙️ How the Project Works</h2>

<ol>
  <li>The user opens the Flask web application in the browser.</li>
  <li>The user types a question in the input box.</li>
  <li>The question is sent to the Flask backend using a POST request.</li>
  <li>Flask passes the user question into the LangChain prompt template.</li>
  <li>LangChain sends the formatted prompt to the Ollama local model.</li>
  <li>The Gemma 2B model generates an AI response.</li>
  <li>The response is displayed back on the frontend page.</li>
</ol>

<hr>

<h2>� Installation</h2>

<pre>
python -m pip install -r requirements.txt
</pre>

<p>
The Flask application is launched from <code>index.py</code> and renders the frontend HTML template located at <code>templates/new.html</code>.
</p>

<hr>

<h2>�💻 Backend Code Explanation</h2>

<h3>1. Flask Application Setup</h3>

<pre>
app = Flask(__name__)
</pre>

<p>
This creates the Flask web application.
</p>

<h3>2. Ollama Model Initialization</h3>

<pre>
llm = ChatOllama(model="gemma:2b")
</pre>

<p>
This connects the application with the locally installed Ollama model named <b>gemma:2b</b>.
</p>

<h3>3. Prompt Template</h3>

<pre>
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("user", "Question: {question}")
    ]
)
</pre>

<p>
This defines how the user input should be sent to the AI model.
The system message tells the model to behave like a helpful assistant.
</p>

<h3>4. LangChain Pipeline</h3>

<pre>
chain = prompt | llm | output_parser
</pre>

<p>
This creates the complete LangChain pipeline:
</p>

<ul>
  <li>Prompt formatting</li>
  <li>LLM response generation</li>
  <li>String output parsing</li>
</ul>

<h3>5. Flask Route</h3>

<pre>
@app.route("/", methods=["GET", "POST"])
def home():
    response = ""
    if request.method == "POST":
        user_input = request.form["question"]
        response = chain.invoke({"question": user_input})
    return render_template("index.html", response=response)
</pre>

<p>
This route handles both page loading and form submission.
When the user submits a question, the AI response is generated and displayed on the webpage.
</p>

<hr>

<h2>📦 Installation Steps</h2>

<h3>1. Clone the Repository</h3>

<pre>
git clone https://github.com/GanjiNagendhraPrasad/Generative-AI-Web-Application-using-Ollama-and-LangChain.git
</pre>

<h3>2. Navigate to the Project Folder</h3>

<pre>
cd Generative-AI-Web-Application-using-Ollama-and-LangChain
</pre>

<h3>3. Create Virtual Environment</h3>

<pre>
python -m venv .venv
</pre>

<h3>4. Activate Virtual Environment</h3>

<p><b>For Windows:</b></p>

<pre>
.venv\Scripts\activate
</pre>

<p><b>For Mac/Linux:</b></p>

<pre>
source .venv/bin/activate
</pre>

<h3>5. Install Required Libraries</h3>

<pre>
pip install -r requirements.txt
</pre>

<h3>6. Install Ollama</h3>

<p>
Download and install Ollama from the official website:
</p>

<pre>
https://ollama.com/
</pre>

<h3>7. Pull Gemma 2B Model</h3>

<pre>
ollama pull gemma:2b
</pre>

<h3>8. Run Ollama</h3>

<pre>
ollama serve
</pre>

<h3>9. Run Flask Application</h3>

<pre>
python app.py
</pre>

<h3>10. Open in Browser</h3>

<pre>
http://127.0.0.1:5000
</pre>

<hr>

<h2>📌 Requirements</h2>

<pre>
flask
langchain
langchain-core
langchain-ollama
ollama
</pre>

<hr>

<h2>🎯 Use Cases</h2>

<ul>
  <li>AI chatbot application</li>
  <li>Local LLM learning project</li>
  <li>Generative AI web application</li>
  <li>LangChain beginner project</li>
  <li>Flask-based AI assistant</li>
  <li>Offline AI assistant prototype</li>
</ul>

<hr>

<h2>✅ Advantages of This Project</h2>

<ul>
  <li>No OpenAI API key required</li>
  <li>Runs locally using Ollama</li>
  <li>Simple and easy to understand</li>
  <li>Good project for AI/ML and GenAI portfolio</li>
  <li>Demonstrates backend and frontend integration</li>
  <li>Shows practical knowledge of LangChain and LLMs</li>
</ul>

<hr>

<h2>⚠️ Important Note</h2>

<p>
This project is designed to run locally because it depends on Ollama.
For cloud deployment platforms like Render, the code must be modified to use a cloud-based LLM API such as OpenAI, Gemini, Groq, or Hugging Face.
</p>

<hr>

<h2>📸 Demo UI</h2>

<p>
The application provides a modern chatbot-style interface where users can enter questions and view AI-generated responses instantly.
</p>

<hr>

<h2>🔮 Future Enhancements</h2>

<ul>
  <li>Add chat history</li>
  <li>Add streaming response output</li>
  <li>Add voice input support</li>
  <li>Add document upload and RAG-based question answering</li>
  <li>Add user authentication</li>
  <li>Deploy cloud version using OpenAI or Gemini API</li>
  <li>Improve UI with dark/light mode toggle</li>
</ul>

<hr>

<h2>👨‍💻 Author</h2>

<p>
<b>Ganji Nagendhra Prasad</b>
</p>

<p>
AI & ML Graduate | Data Science Intern | Aspiring Data Analyst / Data Scientist / AI Engineer
</p>

<p>
GitHub: 
<a href="https://github.com/GanjiNagendhraPrasad">
GanjiNagendhraPrasad
</a>
</p>

<hr>

<h2>⭐ Conclusion</h2>

<p>
This project demonstrates how to build a simple but powerful Generative AI web application using Flask, LangChain, and Ollama.
It is a practical beginner-friendly project for understanding how local LLMs can be integrated with web applications.
</p>

<p align="center">
  <b>⭐ If you like this project, please star the repository!</b>
</p>#   G e n A I - S m a r t - A s s i s t a n t  
 #   G e n A I - S m a r t - A s s i s t a n t  
 #   G e n A I - S m a r t - A s s i s t a n t  
 #   G e n A I - S m a r t - A s s i s t a n t  
 