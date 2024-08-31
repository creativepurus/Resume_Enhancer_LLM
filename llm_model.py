import PyPDF2
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from langchain_huggingface import HuggingFaceEndpoint
import os
from api_key import api_token  # Ensure this module correctly provides your API token

# Set up the Streamlit app
st.title("AI-Powered Resume Improver")

# Upload the PDF file
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

# Get job description input from the user
job_description = st.text_area("Enter the Job Description")

# Set the API token environment variable
os.environ['HUGGINGFACEHUB_API_TOKEN'] = api_token

# Extract resume text and analyze it if the file is uploaded
resume_text = ""
if uploaded_file is not None:
    try:
        # Creating a PDF reader object
        reader = PyPDF2.PdfReader(uploaded_file)

        # Extracting text from all pages of the PDF
        for page in reader.pages:
            resume_text += page.extract_text() or ""

        # Check if resume text is empty (common with scanned PDFs)
        if not resume_text.strip():
            st.error("The uploaded PDF seems to be empty or contains scanned images that cannot be processed.")
        else:
            # Displaying the extracted text
            st.write("Here is the content of your resume:")
            st.text_area("Resume Content", resume_text, height=250)

            # Check if job description is provided
            if job_description:
                # Perform basic NLP to compare resume and job description
                documents = [resume_text, job_description]

                # Convert text to vector
                vectorizer = CountVectorizer().fit_transform(documents)
                vectors = vectorizer.toarray()

                # Calculate cosine similarity
                similarity_matrix = cosine_similarity(vectors)
                match_score = similarity_matrix[0][1] * 100  # Similarity between resume and job description

                st.write(f"Your resume matches the job description by {match_score:.2f}%")

                if match_score < 50:
                    st.write("Consider tailoring your resume to better match the job description.")
                else:
                    st.write("Your resume is a good match for the job description!")

    except Exception as e:
        st.error(f"An error occurred while processing the PDF: {e}")

# Check if both resume text and job description are provided and the user clicks the 'Improve Resume' button
if resume_text and job_description:
    if st.button("Improve Resume"):
        # Display a loading spinner while the LLM is processing the input
        with st.spinner("Improving your resume... Please wait."):
            try:
                # Set up the HuggingFace LLM endpoint
                llm = HuggingFaceEndpoint(
                    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
                    temperature=0.7,
                    model_kwargs={
                        "max_length": 128,
                    },
                    huggingfacehub_api_token=api_token
                )

                # Define the input text for the model
                text = (
                    f"Here is my resume: {resume_text}\n"
                    f"And this is the job description: {job_description}\n"
                    "Please help me modify my resume to increase the chances of landing this job."
                )

                # Invoke the model to get suggestions
                response = llm.invoke(text)

                # Display the AI-suggested improvements
                st.write("AI-Suggested Resume Improvements:")
                st.text_area("Improvements", response, height=200)

            except Exception as e:
                # Handle and display any errors that occur during processing
                st.error(f"An error occurred while processing the resume: {e}")
else:
    st.write("Please provide both a resume and a job description.")
