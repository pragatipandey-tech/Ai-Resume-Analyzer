import spacy

nlp = spacy.load("en_core_web_sm")

def extract_skills(text, skills_list):
    doc = nlp(text.lower())
    found_skills = []

    for token in doc:
        if token.text in skills_list:
            found_skills.append(token.text)

    return list(set(found_skills))