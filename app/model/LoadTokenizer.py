from transformers import AutoTokenizer

def loadUp(name: str, cdir: str):
    return AutoTokenizer.from_pretrained(name, cache_dir=cdir)
