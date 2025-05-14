import boto3
import docx
from botocore.config import Config

kendra_client = boto3.client(
    'kendra',
    aws_access_key_id='AKIA6ODU5LO4LN3EX6F4',
    aws_secret_access_key='MG1JabRZFtaqq5AiS71UNcGWO9aiWHGGhsDZbPb5',
    region_name='ap-south-1'  # e.g., 'us-west-2'
)

comprehend_client = boto3.client(
    'comprehend',
    aws_access_key_id='AKIA6ODU5LO4LN3EX6F4',
    aws_secret_access_key='MG1JabRZFtaqq5AiS71UNcGWO9aiWHGGhsDZbPb5',
    region_name='ap-south-1'
)

def query_kendra(index_id, query_text):
    response = kendra_client.query(
        IndexId=index_id,
        QueryText=query_text,
    )
    return response

def analyze_document(text):
    # Extract key phrases
    key_phrases_response = comprehend_client.detect_key_phrases(
        Text=text,
        LanguageCode='en'  # Specify language code
    )
    
    # Extract entities (optional)
    entities_response = comprehend_client.detect_entities(
        Text=text,
        LanguageCode='en'
    )
    
    return key_phrases_response['KeyPhrases'], entities_response['Entities']

def read_docx(file_path):
    doc = docx.Document(file_path)
    full_text = []
    for paragraph in doc.paragraphs:
        full_text.append(paragraph.text)
    return '\n'.join(full_text)

def main():
    file_path = './ScrappedFiles/imtiy.az6969.docx'
    
    # Read document text from .docx
    document_text = read_docx(file_path)
    
    # Analyze the document text
    keywords, entities = analyze_document(document_text)
    
    print("Keywords Found:")
    for keyword in keywords:
        print(f"- {keyword['Text']} (Score: {keyword['Score']})")
    
    print("\nEntities Found:")
    for entity in entities:
        print(f"- {entity['Text']} (Type: {entity['Type']}, Score: {entity['Score']})")

if __name__ == "__main__":
    main()