# Doxpert.ai

Doxpert.ai is an AI-powered document exploration tool that allows users to interact with PDF documents through natural language queries. It processes large documents, breaks them into manageable chunks, performs semantic search, and provides intelligent, context-aware answers using Google Generative AI.

---

## Overview

Doxpert.ai simplifies working with large PDF documents by offering an intuitive interface for content analysis and exploration. With its ability to split documents, generate embeddings, and retrieve precise answers from complex queries, it is perfect for professionals, researchers, and students who frequently work with extensive documents.

---

## Features

- Upload and process PDF files into smaller, manageable text chunks.
- Generate embeddings for text using `SentenceTransformer`.
- Perform semantic searches on the document using FAISS.
- Get intelligent, context-aware answers to natural language queries powered by Google Generative AI.
- User-friendly interface built using Streamlit.

---

## Prerequisites

Ensure the following are installed on your system:

- Python 3.7 or later
- pip (Python package manager)
- A valid Google Generative AI API key

---

## Quick Start

### 1. Clone the Repository
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
2. Set Up a Virtual Environment
Create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate       # For macOS/Linux
venv\Scripts\activate          # For Windows
3. Install Dependencies
Install the required Python libraries:

bash
Copy
Edit
pip install -r requirements.txt
4. Configure the API Key
Replace "Gemini Google AI studio Api" in the code with your Google Generative AI API key.
To set it as an environment variable (optional):
bash
Copy
Edit
export GENERATIVE_AI_API_KEY="your-api-key"  # macOS/Linux
set GENERATIVE_AI_API_KEY="your-api-key"    # Windows
5. Run the Application
Launch the Streamlit app:

bash
Copy
Edit
streamlit run app.py
Open your browser and navigate to the URL provided by Streamlit (default: http://localhost:8501).

Project Structure
bash
Copy
Edit
.
├── app.py                # Main application code
├── requirements.txt      # Required dependencies
├── uploads/              # Directory for storing uploaded files
├── README.md             # Project documentation
├── .gitignore            # Git ignore file
└── venv/                 # Virtual environment (not tracked by Git)
Dependencies
Streamlit: For building the interactive user interface.
LangChain: For loading and processing PDF documents.
FAISS: For efficient similarity searches.
Sentence-Transformers: For generating text embeddings.
Google Generative AI: For intelligent natural language processing.
Install all dependencies using:

bash
Copy
Edit
pip install -r requirements.txt
Environment Variables
Variable Name	Description
GENERATIVE_AI_API_KEY	Your Google Generative AI API key
You can set this key in your terminal or directly in the code.

Development Setup
1. Set Up the Development Environment
Create and activate the virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate       # macOS/Linux
venv\Scripts\activate          # Windows
2. Install Development Tools
Install tools like black, flake8, and isort for code formatting and linting:

bash
Copy
Edit
pip install black flake8 isort
3. Lint and Format Code
Format code:
bash
Copy
Edit
black .
Lint code:
bash
Copy
Edit
flake8 .
Development Tools
Black: Python code formatter.
Flake8: Python linting tool.
Isort: Python import sorter.
Install all development tools:

bash
Copy
Edit
pip install black flake8 isort
Contributing
Contributions are welcome! Follow these steps to contribute:

Fork the repository.
Create a feature branch:
bash
Copy
Edit
git checkout -b feature-name
Commit your changes:
bash
Copy
Edit
git commit -m "Add feature-name"
Push your branch:
bash
Copy
Edit
git push origin feature-name
Open a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
Google Generative AI
Streamlit
LangChain
FAISS
Sentence-Transformers
