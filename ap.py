import streamlit as st
from srcn.cf import classify_persona
from srcn.rag_pipline import load_documents, retrieve
from srcn.gen import generate_response
from srcn.escalator import should_escalate

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