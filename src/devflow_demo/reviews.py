def latest_review(states: list[str]) -> str | None:
    return states[-1] if states else None
