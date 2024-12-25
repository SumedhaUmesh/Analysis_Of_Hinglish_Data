import torch


def translate(text):
    torch_model = torch.load('model.pt')
    tokenizer = torch.load('model2.pt')
    translated = ""
    text = text.split('\n')
    for i in text:
        if i:
            model_inputs = tokenizer(i, return_tensors="pt")
            generated_tokens = torch_model.generate(**model_inputs, forced_bos_token_id=tokenizer.lang_code_to_id["en_XX"])
            translation = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
            translated += translation[0] + "\n"

    return translated
