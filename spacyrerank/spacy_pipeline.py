import torch
import spacy
from transformers import AutoTokenizer, AutoModel
from functools import lru_cache


@lru_cache(maxsize=128)
def load_model():
    model_path = "models/tinygte/"
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModel.from_pretrained(model_path)
    return model, tokenizer


@lru_cache(maxsize=128)
def get_embeddings(text):
    
    encoded_input = load_model()[1]([text], padding=True, truncation=True, return_tensors='pt')
    with torch.no_grad():
        model_output = load_model()[0](**encoded_input)
    token_embeddings = model_output[0]
    input_mask_expanded = encoded_input['attention_mask'].unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)
