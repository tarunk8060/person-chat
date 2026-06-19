import streamlit as st
from cf import classify_persona
from rag_pipline import load_documents, retrieve
from gen import generate_response
from escalator import should_escalate

load_documents()

st.title("Persona Adaptive Support Agent")

query = st.text_input("Ask your question")

if query:
    if should_escalate(query):
        st.error("Escalating to human agent.")
    else:
        persona = classify_persona(query)
        context = retrieve(query)
        response = generate_response(persona, query, context)

        st.write("Persona:", persona)
        st.write(response)
