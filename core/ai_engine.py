import torch
import easyocr
from transformers import pipeline
import aiohttp

class DualAIEngine:
    def __init__(self):
        dev = 0 if torch.cuda.is_available() else -1
        self.ocr = easyocr.Reader(['ar', 'en'], gpu=torch.cuda.is_available())
        self.clf = pipeline("text-classification", model="facebook/roberta-hate-speech-dynabench-r4-target", device=dev)

    async def analyze(self, content_batch):
        scores = {"Hate Speech": 0, "Violence": 0, "Fake Account": 0.1}
        for item in content_batch:
            text = item['text']
            for img_bytes in item.get('img_files', []):
                ocr_text = " ".join(self.ocr.readtext(img_bytes, detail=0))
                text += " " + ocr_text
            
            res = self.clf(text[:512])[0]
            if res['label'] == 'hate': scores["Hate Speech"] += res['score']
        return max(scores, key=scores.get)
      
