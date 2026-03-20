import json
import os

def transform(input_json, output_path):
    with open(input_json, 'r') as f:
        raw = json.load(f)
    formatted = {
        "cookies": [{
            "name": c['name'], "value": c['value'], "domain": ".facebook.com", "path": "/",
            "expires": c.get('expirationDate', -1), "httpOnly": c.get('httpOnly', False),
            "secure": True, "sameSite": "Lax"
        } for c in raw],
        "origins": []
    }
    with open(output_path, 'w') as f:
        json.dump(formatted, f, indent=2)
      
