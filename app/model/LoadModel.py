from transformers import AutoModelWithLMHead

def loadUp(name: str, cdir: str):
    return AutoModelWithLMHead.from_pretrained(name, cache_dir=cdir)
