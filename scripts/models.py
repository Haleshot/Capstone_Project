# # Use a pipeline as a high-level helper
# from transformers import pipeline

# messages = [
#     {"role": "user", "content": "Who are you?"},
# ]
# pipe = pipeline("text-generation", model="E:\Models\models--AI-MO--NuminaMath-7B-TIR\snapshots\8a0609f3f98167d3663b961befbd2e7a6168c34e")
# pipe(messages)

# from transformers import AutoTokenizer, LlamaForCausalLM

# model = LlamaForCausalLM.from_pretrained("E:\Models\models--AI-MO--NuminaMath-7B-TIR\snapshots\8a0609f3f98167d3663b961befbd2e7a6168c34e", use_safetensors=True)
# tokenizer = AutoTokenizer.from_pretrained("E:\Models\models--AI-MO--NuminaMath-7B-TIR\snapshots\8a0609f3f98167d3663b961befbd2e7a6168c34e", use_safetensors=True)

# prompt = "Hey, are you conscious? Can you talk to me?"
# inputs = tokenizer(prompt, return_tensors="pt")

# # Generate
# generate_ids = model.generate(inputs.input_ids, max_length=30) # type:ignore
# tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]

# from llama_cpp import Llama

# llm = Llama.from_pretrained(
#     repo_id="Qwen/Qwen2-0.5B-Instruct-GGUF",
#     filename="mathmate.gguf",
#     verbose=False
# )

import re
import torch
from transformers import pipeline

pipe = pipeline("text-generation", model="AI-MO/NuminaMath-7B-TIR", torch_dtype=torch.bfloat16, device_map="auto")

messages = [
    {"role": "user", "content": "For how many values of the constant $k$ will the polynomial $x^{2}+kx+36$ have two distinct integer roots?"},
]
prompt = pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

gen_config = {
    "max_new_tokens": 1024,
    "do_sample": False,
    "stop_strings": ["```output"], # Generate until Python code block is complete
    "tokenizer": pipe.tokenizer,
}

outputs = pipe(prompt, **gen_config)
text = outputs[0]["generated_text"]
print(text)

# WARNING: This code will execute the python code in the string. We show this for eductional purposes only.
# Please refer to our full pipeline for a safer way to execute code.
python_code = re.findall(r"```python(.*?)```", text, re.DOTALL)[0]
exec(python_code)
