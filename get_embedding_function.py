
from langchain.embeddings import HuggingFaceEmbeddings

def get_embedding_function():
    '''embeddings = BedrockEmbeddings(
        credentials_profile_name="default", region_name="us-east-1"
    )'''

    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

    
    return embeddings
