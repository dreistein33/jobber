import g4f
import requests
from bs4 import BeautifulSoup
import time
import tiktoken

TOKEN_LIMIT = 4096

PROVIDER = g4f.Provider.DeepAi


def count_tokens(text: str) -> int:
    encoding = tiktoken.get_encoding("cl100k_base")

    return len(encoding.encode(text))


def get_company_details(url: str) -> str:
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')
        
    text_elements = soup.find_all(string=True)

    visible_texts = filter(lambda text: not text.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]'], text_elements)
    extracted_text = ' '.join(visible_texts)

    content = f"Wyekstraktuj dane o firmie z tego tekstu: {extracted_text}"

    response = g4f.ChatCompletion.create(model='gpt-3.5-turbo', provider=PROVIDER, messages=[
                                        {"role": "user", "content": content}], stream=False)

    return response


def get_moti_letter(
    language: str,
    job_url: str,
    job_title: str,
    person_name: str,
    person_surname: str,
    person_age: str,
    person_interests: str,
    person_about: str
) -> str:
    details = get_company_details(job_url)
    time.sleep(5)

    about_you = f"You are {person_name} {person_surname}, {person_age} y.o. You are interested in {person_interests}. About you: {person_about}"

    cover_letter_prompt = f"You are applying for a job as a {job_title}, and you want to create a compelling cover letter that showcases your skills, experiences, and enthusiasm for the position. Write a cover letter in {language} that introduces yourself, highlights your relevant achievements and qualifications, and explains why you are the perfect fit for the job. Please make it engaging, persuasive, and tailored to the specific company and job description. Feel free to include any additional information that you think would make you stand out as a top candidate. The company you are applying to is detailed here: {details}."

    complete_prompt = about_you + cover_letter_prompt

    print(f"Tokens in prompt: {count_tokens(complete_prompt)}")

    # Is there a handier way to deal with the error here, so my backend will
    # automatically detect if its an exception?
    try:
        response = g4f.ChatCompletion.create(model='gpt-3.5-turbo', provider=PROVIDER, messages=[
                                        {"role": "user", "content": complete_prompt}], stream=False)
    except Exception as e:
        response = f"{e}"

    return response


# pdf_path = "/home/dzony/Downloads/Jakub-Juchnowski.pdf"
# with open(pdf_path) as f:
#     pdf = PdfReader(pdf_path)

#     page = pdf.pages[0]

#     print(page.extract_text()) 

