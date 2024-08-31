# AI-Powered Resume Enhancer

[Screencast from 09-01-2024 12:42:59 AM.webm](https://github.com/user-attachments/assets/12437972-bd7d-4b08-a382-832306afb6c9)

[![GitHub issues](https://img.shields.io/github/issues/AnshD2002/Resume_Enhancer_LLM)](https://github.com/AnshD2002/Resume_Enhancer_LLM/issues)
[![GitHub stars](https://img.shields.io/github/stars/AnshD2002/Resume_Enhancer_LLM)](https://github.com/AnshD2002/Resume_Enhancer_LLM/stargazers)
[![GitHub license](https://img.shields.io/github/license/AnshD2002/Resume_Enhancer_LLM)](https://github.com/AnshD2002/Resume_Enhancer_LLM/blob/main/LICENSE)

## Overview

The AI-Powered Resume Enhancer is a Streamlit-based application designed to help you improve your resume by analyzing it against job descriptions. Leveraging the Mistral-7B-Instruct-v0.3 model from Hugging Face, this app suggests tailored modifications to increase your chances of landing your dream job.

## Features

- **PDF Resume Upload**: Upload your resume in PDF format for analysis.
- **Job Description Matching**: Input the job description to compare how well your resume matches the required skills.
- **Cosine Similarity Calculation**: Calculate the similarity score between your resume and the job description to assess alignment.
- **LLM-Powered Improvements**: Get AI-suggested resume modifications using the Mistral-7B-Instruct-v0.3 model.
- **User-Friendly Interface**: Intuitive Streamlit interface for easy interaction.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AnshD2002/Resume_Enhancer_LLM.git
   cd Resume_Enhancer_LLM
2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
4. Set up your API token for Hugging Face by modifying api_key.py:
   ```bash
   api_token = "your_huggingface_api_token"
5. Usage
Run the Streamlit application:
   ```bash
   api_token = "your_huggingface_api_token"

## Upload your resume in PDF format.

Input the job description you are targeting.

Review the similarity score and get AI-powered suggestions to enhance your resume.

## Dependencies
PyPDF2
Streamlit
scikit-learn
Hugging Face Hub
Mistral-7B-Instruct-v0.3 Model
Contributing
Contributions are welcome! Please read the contribution guidelines before getting started.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
Thanks to Hugging Face for providing the LLM infrastructure.
The Mistral-7B-Instruct-v0.3 model is the core of this project's AI capabilities.

##Contact
For any inquiries or issues, please open an issue on GitHub or contact me at [anshdabral182@gmail.com].
