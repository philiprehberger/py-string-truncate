"""Truncate strings intelligently without cutting words."""

from __future__ import annotations


__all__ = [
    "truncate",
    "truncate_middle",
    "truncate_path",
]


def truncate(
    text: str,
    max_length: int,
    *,
    suffix: str = "\u2026",
    break_words: bool = False,
) -> str:
    """Truncate a string to a maximum length, respecting word boundaries.

    Args:
        text: The string to truncate.
        max_length: Maximum length including suffix.
        suffix: String to append when truncated. Defaults to ``"\\u2026"`` (ellipsis).
        break_words: If True, cut at exact max_length regardless of word boundaries.

    Returns:
        Truncated string.
    """
    if len(text) <= max_length:
        return text

    if max_length <= len(suffix):
        return suffix[:max_length]

    available = max_length - len(suffix)

    if break_words:
        return text[:available] + suffix

    # Find last space before the limit
    cut = text[:available + 1].rfind(" ")
    if cut <= 0:
        # No space found — force break
        return text[:available] + suffix

    return text[:cut].rstrip() + suffix


def truncate_middle(
    text: str,
    max_length: int,
    *,
    separator: str = "\u2026",
) -> str:
    """Truncate by removing the middle portion, keeping start and end.

    Args:
        text: The string to truncate.
        max_length: Maximum total length including separator.
        separator: String placed in the middle. Defaults to ``"\\u2026"``.

    Returns:
        Truncated string with middle removed.
    """
    if len(text) <= max_length:
        return text

    if max_length <= len(separator):
        return separator[:max_length]

    available = max_length - len(separator)
    start_len = (available + 1) // 2
    end_len = available - start_len

    start = text[:start_len]
    end = text[-end_len:] if end_len > 0 else ""

    return start + separator + end


def truncate_path(
    path: str,
    max_length: int,
    *,
    separator: str = "/",
    placeholder: str = "...",
) -> str:
    """Truncate a file path, preserving the first and last segments.

    Args:
        path: The path to truncate.
        max_length: Maximum total length.
        separator: Path separator.
        placeholder: String replacing removed middle segments.

    Returns:
        Truncated path.
    """
    if len(path) <= max_length:
        return path

    parts = path.split(separator)
    if len(parts) <= 2:
        return truncate_middle(path, max_length, separator=placeholder)

    first = parts[0] or separator  # handle leading separator
    last = parts[-1]

    # Minimum: first/…/last
    skeleton = f"{first}{separator}{placeholder}{separator}{last}"
    if len(skeleton) >= max_length:
        return truncate_middle(path, max_length, separator=placeholder)

    # Try to include more segments from the start
    budget = max_length - len(placeholder) - len(separator) * 2 - len(last)
    included: list[str] = []
    used = 0

    for part in parts[:-1]:
        candidate = part + separator
        if used + len(candidate) > budget:
            break
        included.append(part)
        used += len(candidate)

    if not included:
        included.append(first)

    return separator.join(included) + separator + placeholder + separator + last
