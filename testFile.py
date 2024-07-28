from sentence_transformers import SentenceTransformer

import requests
from sentence_transformers import SentenceTransformer, util

# Bypass SSL verification
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
model = SentenceTransformer('all-MiniLM-L6-v2', cache_folder="/Users/mahassaf004/.cache/torch/sentence_transformers")
print("Model loaded successfully.")
