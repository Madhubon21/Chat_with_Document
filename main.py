import streamlit as st
from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import numpy as np
import os
import faiss
import pickle
import google.generativeai as genai

genai.configure(api_key="Google AI Studio Gemini Api")  

def process_pdf(file):
    loader = PyPDFLoader(file_path=file)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = text_splitter.split_documents(documents)

    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = [model.encode(chunk.page_content) for chunk in chunks]

    embedded_data = [{"chunk": chunk.page_content, "embedding": embedding} for chunk, embedding in zip(chunks, embeddings)]
    embeddings_array = np.array(embeddings, dtype='float32')

    np.save("embeddings.npy", embedded_data)
    metadata = [{"id": f"chunk-{i}", "text": chunk.page_content} for i, chunk in enumerate(chunks)]
    faiss_index = faiss.IndexFlatL2(embeddings_array.shape[1])
    faiss_index.add(embeddings_array)

    faiss.write_index(faiss_index, "faiss_index.bin")
    with open("faiss_metadata.pkl", "wb") as f:
        pickle.dump(metadata, f)

    return len(chunks)

def get_relevant_chunks(query, top_k=2):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    query_embedding = model.encode(query).astype('float32')

    index = faiss.read_index("faiss_index.bin")
    D, I = index.search(np.array([query_embedding]), top_k)

    with open("faiss_metadata.pkl", "rb") as f:
        metadata = pickle.load(f)

    relevant_chunks = [metadata[i]["text"] for i in I[0]]
    return relevant_chunks

def answer_question(query):
    chunks = get_relevant_chunks(query)
    context = "\n".join(chunks)

    model = genai.GenerativeModel(model_name='gemini-1.5-pro')
    response = model.generate_content(f"Answer the following question using the provided context:\n\nQuestion: {query}\n\nContext: {context}")
    return response.text


def main():
    st.title("Doxpert.ai")

    uploaded_file = st.file_uploader("Upload your PDF file", type=["pdf"])

    if uploaded_file is not None:
        st.write("Processing PDF...")

        upload_dir = "uploads"
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)

        pdf_path = os.path.join(upload_dir, uploaded_file.name)
        with open(pdf_path, "wb") as f:
            f.write(uploaded_file.read())

        num_chunks = process_pdf(pdf_path)
        st.success(f"PDF processed successfully! {num_chunks} chunks created.")

    query = st.text_input("Enter your query:")

    if st.button("Go"):
        if query:
            with st.spinner("Fetching..."):
                answer = answer_question(query)
            st.subheader("Answer:")
            st.write(answer)
        else:
            st.warning("Please enter a query.")

if __name__ == "__main__":
    main()
