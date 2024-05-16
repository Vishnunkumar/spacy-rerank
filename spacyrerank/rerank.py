import torch
import spacy
from .spacy_pipeline import get_embeddings, load_model
from functools import lru_cache
from spacy.language import Language


nlp = spacy.blank("en")

@Language.component("hf-embedder")
def spacy_embedder(doc):
    doc.vector = get_embeddings(doc.text)
    return doc


class Reranker:

    def __init__(self, query, texts):
        self.query = query
        self.texts = texts
        load_model()
        
    @lru_cache(maxsize=128)
    def __call__(self):
    
        if "hf-embedder" not in nlp.pipe_names:
            nlp.add_pipe("hf-embedder")
    
        scores = []
        query_embed = nlp(self.query).vector
        scores = [torch.nn.functional.cosine_similarity(doc.vector, query_embed) for doc in nlp.pipe(self.texts)]

        final_list = []
        for idx in torch.argsort(torch.Tensor(scores), descending=True):
            return_dict = {}
            return_dict["rank"] = idx.item()
            return_dict["text"] = self.texts[idx]
            return_dict["similarity-score"] = round(scores[idx][0].item(), 3)
            final_list.append(return_dict)
        
        return final_list
