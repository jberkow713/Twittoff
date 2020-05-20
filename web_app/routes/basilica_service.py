import basilica
import os
from dotenv import load_dotenv 
 

API_KEY = os.getenv("BASILICA_API_KEY")

def basilica_api_client():
    connection = basilica.Connection(API_KEY)
    print(type(connection)) #> <class 'basilica.Connection'>
    return connection

#sentences = [
#    "This is a sentence",
#    "This is a similar sentence!",
#]

with basilica.Connection(API_KEY) as c:
    embeddings = c.embed_sentences(["Hello world!", "How are you?"])
    print(list(embeddings))

if __name__ == "__main__":

    print("---------")
    connection = basilica_api_client()

    print("---------")
    sentence = "Hello again"
    sent_embeddings = connection.embed_sentence(sentence)
    print(list(sent_embeddings))

    print("---------")
    sentences = ["Hello world!", "How are you?"]
    print(sentences)
    # it is more efficient to make a single request for all sentences...
    embeddings = connection.embed_sentences(sentences)
    print("EMBEDDINGS...")
    print(type(embeddings))
    print(list(embeddings))