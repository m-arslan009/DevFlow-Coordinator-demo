def require_title(title: str) -> str:
    cleaned = title.strip()
    if not cleaned:
        raise ValueError('title required')
    return cleaned
