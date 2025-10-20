from fastapi import APIRouter, HTTPException, Query
from api.v1.schemas import string_schema
from api.v1.services import string_service
from api.utils import nlp_parser

router = APIRouter(prefix="/strings", tags=["String Analysis"])


@router.post("", response_model=string_schema.StringResponse, status_code=201)
def create_string(data: string_schema.StringCreate):
    if not isinstance(data.value, str):
        raise HTTPException(status_code=422, detail="value must be a string")

    record = string_service.create_string(data.value)
    if not record:
        raise HTTPException(status_code=409, detail="String already exists")

    return record


@router.get("/filter-by-natural-language")
def filter_by_natural_language(query: str):
    try:
        filters = nlp_parser.parse_natural_query(query)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    results = string_service.get_all_strings(**filters)

    return {
        "data": results,
        "count": len(results),
        "interpreted_query": {
            "original": query,
            "parsed_filters": filters
        }
    }


@router.get("", response_model=string_schema.StringListResponse)
def get_all_strings(
    is_palindrome: bool | None = Query(None),
    min_length: int | None = Query(None),
    max_length: int | None = Query(None),
    word_count: int | None = Query(None),
    contains_character: str | None = Query(None)
):
    results = string_service.get_all_strings(
        is_palindrome=is_palindrome,
        min_length=min_length,
        max_length=max_length,
        word_count=word_count,
        contains_character=contains_character
    )

    return {
        "data": results,
        "count": len(results),
        "filters_applied": {
            "is_palindrome": is_palindrome,
            "min_length": min_length,
            "max_length": max_length,
            "word_count": word_count,
            "contains_character": contains_character
        }
    }


@router.get("/{string_value}", response_model=string_schema.StringResponse)
def get_string(string_value: str):
    record = string_service.get_string_by_value(string_value)
    if not record:
        raise HTTPException(status_code=404, detail="String not found")
    return record


@router.delete("/{string_value}", status_code=204)
def delete_string(string_value: str):
    success = string_service.delete_string(string_value)
    if not success:
        raise HTTPException(status_code=404, detail="String not found")
