def parse_natural_query(query: str):
    query = query.lower().strip()
    filters = {}

    if "palindromic" in query or "palindrome" in query:
        filters["is_palindrome"] = True
    if "single word" in query:
        filters["word_count"] = 1
    if "longer than" in query:
        try:
            num = int(query.split("longer than")[1].split()[0])
            filters["min_length"] = num + 1
        except Exception:
            pass
    if "containing the letter" in query or "containing" in query:
        parts = query.split("containing")
        if len(parts) > 1:
            char = parts[1].strip().split()[1][0]
            filters["contains_character"] = char

    if not filters:
        raise ValueError("Could not parse query")

    return filters
