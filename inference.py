from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("t5-base")
model = T5ForConditionalGeneration.from_pretrained("t5-base")

def simplify(text):
    input_text = "simplify: " + text

    input_ids = tokenizer.encode(
        input_text,
        return_tensors="pt",
        max_length=512,
        truncation=True
    )

    outputs = model.generate(
        input_ids,
        max_length=50,
        num_beams=5,
        early_stopping=True
    )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)

sentence = "Perform cervical rotation to the right and left."

print("Original:", sentence)
print("Simplified:", simplify(sentence))
