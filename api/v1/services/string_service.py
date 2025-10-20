from typing import Optional, List
from api.v1.models import string_model
from api.utils import analyzer

# In-memory store
STRING_STORE = {}  # key: sha256 hash, value: StringRecord instance


def create_string(value: str):
    props = analyzer.compute_properties(value)
    hash_value = props["sha256_hash"]

    if hash_value in STRING_STORE:
        return None  # Conflict

    record = string_model.StringRecord(value, props)
    STRING_STORE[hash_value] = record
    return record


def get_string_by_value(value: str):
    # Find by value, not hash
    for record in STRING_STORE.values():
        if record.value == value:
            return record
    return None


def get_all_strings(
    is_palindrome: Optional[bool] = None,
    min_length: Optional[int] = None,
    max_length: Optional[int] = None,
    word_count: Optional[int] = None,
    contains_character: Optional[str] = None
):
    results = list(STRING_STORE.values())

    if is_palindrome is not None:
        results = [r for r in results if r.properties["is_palindrome"] == is_palindrome]
    if min_length is not None:
        results = [r for r in results if r.properties["length"] >= min_length]
    if max_length is not None:
        results = [r for r in results if r.properties["length"] <= max_length]
    if word_count is not None:
        results = [r for r in results if r.properties["word_count"] == word_count]
    if contains_character:
        results = [r for r in results if contains_character in r.value]

    return results


def delete_string(value: str):
    to_delete = None
    for hash_value, record in STRING_STORE.items():
        if record.value == value:
            to_delete = hash_value
            break
    if to_delete:
        del STRING_STORE[to_delete]
        return True
    return False
