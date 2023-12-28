import warnings
warnings.filterwarnings('ignore')

import re

import LoadModel
import LoadTokenizer

CACHE_DIR_MODEL = '../tr_cache/models/'
CACHE_DIR_TOKENS = '../tr_cache/tokenizers/'
MODEL_NAME = 'tinkoff-ai/ruDialoGPT-medium'


class Model:
    def __init__(self) -> None:
        self.tokenizer = LoadTokenizer.loadUp(MODEL_NAME, CACHE_DIR_TOKENS)
        self.model = LoadModel.loadUp(MODEL_NAME, CACHE_DIR_MODEL)
        print('Model is ready')
        
    def preparePrompt(self, prompt: str):
        return self.tokenizer(prompt, return_tensors='pt')
    
    def prepareOutput(self, input, output):
        answer = self.tokenizer.decode(output, skip_special_tokens=True)
        return self.beautify(answer, input)
        
    def beautify(self, text: str, prompt: str):
        text = re.sub(r'@@[а-яА-Я]+@@', '', text)
        text = re.sub(r' +', ' ', text)
        text = re.sub(r'\s+(?=(?:[,.?!:;…]))', '', text)

        return text.replace(prompt, '').strip()
    
    def conv(self, prompt):
        inputs = self.preparePrompt(prompt)
        print('Generating...')
        generated_token_ids = self.model.generate(
            **inputs,
            top_k=10,
            top_p=0.95,
            num_beams=3,
            num_return_sequences=1,
            do_sample=True,
            no_repeat_ngram_size=2,
            temperature=1.2,
            repetition_penalty=1.2,
            length_penalty=1.0,
            eos_token_id=50257,
            pad_token_id=self.tokenizer.pad_token_id,
            max_new_tokens=40
        )
        print('Done generating')
        return self.prepareOutput(prompt, generated_token_ids[0])
