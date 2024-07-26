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