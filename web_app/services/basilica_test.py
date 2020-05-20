import basilica
sentences = [
    "This is a sentence!",
    "This is a similar sentence!",
    "I don't think this sentence is very similar at all...",
]
with basilica.Connection('73afeca4-b8fd-28d0-1771-75318c6889f1') as c:
    embeddings = list(c.embed_sentences(sentences))
print(embeddings)

from scipy import spatial
print(spatial.distance.cosine(embeddings[0], embeddings[1]))
print(spatial.distance.cosine(embeddings[0], embeddings[2]))