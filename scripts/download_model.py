import re
import torch
from transformers import pipeline

cache_directory = r"<insert-path-to-download-model>"

pipe = pipeline(
    "text-generation", 
    model="AI-MO/NuminaMath-7B-TIR", 
    torch_dtype=torch.bfloat16, 
    device_map="auto",
    model_kwargs={"cache_dir": cache_directory},
    tokenizer_kwargs={"cache_dir": cache_directory}
)