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
   cd <Chat_With_Document>
```
### Set Up a Virtual Environment
Follow these steps to set up a virtual environment for the project:
1. **Create the Virtual Environment**  
   Run the following command in your terminal:
   ```bash
   python -m venv venv
   
### Install Dependencies
Install the required dependencies using the following command:
```bash
pip install -r requirements.txt
```
### Configure the API Key
Replace "Gemini Google AI studio Api" in the code with your Google Generative AI API key.
Alternatively, set the key as an environment variable:

```bash
export GENERATIVE_AI_API_KEY="your-api-key"  # macOS/Linux
set GENERATIVE_AI_API_KEY="your-api-key"    # Windows
```
### Run the Application
Start the application using Streamlit:
```bash
streamlit run app.py
```
Open your browser and navigate to the URL provided by Streamlit (default: http://localhost:8501).
### Project Structure
The repository is organized as follows:

```bash
├── app.py                # Main application code
├── requirements.txt      # Required dependencies
├── uploads/              # Directory for storing uploaded files
├── README.md             # Project documentation
├── .gitignore            # Git ignore file
└── venv/                 # Virtual environment (not tracked by Git)
```
## Dependencies
This project relies on the following libraries and frameworks:

- `Streamlit: For building the interactive user interface.`
- `LangChain: For loading and processing PDF documents.`
- `FAISS: For efficient similarity searches.`
- `Sentence-Transformers: For generating text embeddings.`
- `Google Generative AI: For intelligent natural language processing.`
- `You can install all dependencies using:`

```bash
pip install -r requirements.txt
```
## Development Setup
Set Up the Development Environment
Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate       # macOS/Linux
venv\Scripts\activate          # Windows
```
### Install Development Tools
Install additional tools for development, such as black, flake8, and isort:

```bash
pip install black flake8 isort
```
### Lint and Format Code
Use these tools to maintain code quality:
Format code:
```bash
black
```
Lint code:
```bash
flake8 
```
##Development Tools
This project utilizes the following development tools:

- `Black: A code formatter to ensure consistent style.`
-`Flake8: A linting tool to catch potential code issues.`
-`Isort: A tool to sort imports in Python scripts.`
-`Install these tools using:`

``` bash
pip install black flake8 isort
```

