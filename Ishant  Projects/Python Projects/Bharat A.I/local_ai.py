from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "facebook/opt-1.3b"  # Or any free model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def local_ai(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(inputs.input_ids, max_length=256)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

print(local_ai("What is AI?"))
