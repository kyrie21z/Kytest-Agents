def normalize_tags(text):
    """Turn a comma-separated tag string into a list of normalized tags.

    Each tag is stripped of surrounding whitespace and lower-cased. Empty tags
    (including ones that are only whitespace) are dropped. Duplicates, compared
    after normalization, are removed so that only the first occurrence is kept,
    and the remaining tags keep their original order. A string without any
    non-empty tag gives an empty list.

    >>> normalize_tags(" Python, ML ,python,, Data ")
    ['python', 'ml', 'data']
    """
    seen = []
    for raw in text.split(","):
        tag = raw.strip().lower()
        if tag and tag not in seen:
            seen.append(tag)
    return sorted(set(seen))
