# import re
# import torch
# from transformers import pipeline

# pipe = pipeline("text-generation", model=r"E:\Models\models--AI-MO--NuminaMath-7B-TIR", torch_dtype=torch.bfloat16, device_map="auto")

# messages = [
#     {"role": "user", "content": "For how many values of the constant $k$ will the polynomial $x^{2}+kx+36$ have two distinct integer roots?"},
# ]
# prompt = pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

# gen_config = {
#     "max_new_tokens": 1024,
#     "do_sample": False,
#     "stop_strings": ["```output"], # Generate until Python code block is complete
#     "tokenizer": pipe.tokenizer,
# }

# outputs = pipe(prompt, **gen_config)
# text = outputs[0]["generated_text"]
# print(text)

# # WARNING: This code will execute the python code in the string. We show this for eductional purposes only.
# # Please refer to our full pipeline for a safer way to execute code.
# python_code = re.findall(r"```python(.*?)```", text, re.DOTALL)[0]
# exec(python_code)
