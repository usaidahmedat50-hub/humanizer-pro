import math
import re
from collections import Counter

def calculate_stats(text: str):
    \"\"\"
    Calculate simple perplexity (based on word frequency) and burstiness 
    (standard deviation of sentence lengths) to give a 'Human Score'.
    \"\"\"
    if not text or len(text.strip()) == 0:
        return {"perplexity": 0, "burstiness": 0, "human_score": 0}

    # Tokenize words
    words = re.findall(r'\w+', text.lower())
    if not words:
        return {"perplexity": 0, "burstiness": 0, "human_score": 0}

    # Simple Perplexity (Shannon Entropy)
    word_counts = Counter(words)
    total_words = len(words)
    entropy = -sum((count / total_words) * math.log2(count / total_words) for count in word_counts.values())
    perplexity = 2 ** entropy

    # Burstiness (Variance in sentence lengths)
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if len(s.strip()) > 0]
    
    if len(sentences) > 1:
        lengths = [len(s.split()) for s in sentences]
        mean_len = sum(lengths) / len(lengths)
        variance = sum((l - mean_len) ** 2 for l in lengths) / len(lengths)
        burstiness = math.sqrt(variance)
    else:
        burstiness = 0

    # Human Score (Heuristic: High burstiness and moderate perplexity is human)
    # Burstiness > 5 is good. Perplexity > 20 is good for varied vocabulary.
    score = (min(burstiness, 15) / 15 * 50) + (min(perplexity, 100) / 100 * 50)
    
    return {
        "perplexity": round(perplexity, 2),
        "burstiness": round(burstiness, 2),
        "human_score": round(min(score, 100), 1)
    }
