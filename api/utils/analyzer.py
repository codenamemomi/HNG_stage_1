import hashlib
from collections import Counter

def compute_properties(value: str):
    cleaned = value.strip()
    hash_value = hashlib.sha256(cleaned.encode()).hexdigest()

    return {
        "length": len(cleaned),
        "is_palindrome": cleaned.lower() == cleaned[::-1].lower(),
        "unique_characters": len(set(cleaned)),
        "word_count": len(cleaned.split()),
        "sha256_hash": hash_value,
        "character_frequency_map": dict(Counter(cleaned))
    }
