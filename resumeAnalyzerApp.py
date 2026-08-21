import streamlit as st
from utils import extract_pdf, create_vector_store
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


# Page configuration
st.set_page_config(page_title="Help4Code Placement RAG")

st.title("Help4Code Resume Analyzer AI")


# Upload resume
resume_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

# Enter Job Description
jd_text = st.text_area(
    "Paste Job Description"
)


# Analyze button
if st.button("Analyze"):

    if resume_file and jd_text:

        # Extract Resume
        resume_text = extract_pdf(resume_file)

        # Combine Resume + Job Description
        combine_text = resume_text + "\n\n" + jd_text

        # Create Vector Store
        vectorstore = create_vector_store(combine_text)

        # Create Retriever
        retriever = vectorstore.as_retriever()

        # Load Ollama LLM
        llm = Ollama(model="gemma2:2b")

        # Prompt Template
        prompt = ChatPromptTemplate.from_template(
            """
            You are an AI placement coach for Help4Code.

            Context:
            {context}

            Question:
            {question}

            Analyze the resume against the job description.

            Provide:

            1. Skills Gap Analysis
            2. Missing Technologies
            3. ATS Score (0-100)
            4. 10 Technical Interview Questions
            5. Resume Improvement Suggestions

            Give the answer in a clear and structured format.
            """
        )

        # RAG Chain
        chain = (
            {
                "context": retriever,
                "question": RunnablePassthrough()
            }
            | prompt
            | llm
            | StrOutputParser()
        )

        # Run Chain
        response = chain.invoke(
            "Analyze my resume against the provided job description."
        )

        # Display Result
        st.subheader("Analysis Result")

        st.write(response)

    else:

        st.warning(
            "Please upload your resume and paste the job description."
        )