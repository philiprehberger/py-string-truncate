import pytest

from philiprehberger_string_truncate import (
    truncate,
    truncate_middle,
    truncate_path,
    truncate_words,
    wrap,
)


def test_no_truncation_needed():
    assert truncate("short", max_length=20) == "short"


def test_truncate_at_word_boundary():
    result = truncate("Hello beautiful world", max_length=15)
    assert len(result) <= 15
    assert result.endswith("\u2026")


def test_truncate_custom_suffix():
    result = truncate("Hello beautiful world", max_length=15, suffix="...")
    assert result.endswith("...")


def test_truncate_break_words():
    result = truncate("Hello beautiful world", max_length=10, break_words=True)
    assert len(result) == 10


def test_truncate_very_short():
    result = truncate("Hello world", max_length=1)
    assert len(result) <= 1


def test_truncate_middle_no_truncation():
    assert truncate_middle("short", max_length=20) == "short"


def test_truncate_middle():
    result = truncate_middle("Hello beautiful world", max_length=15)
    assert len(result) <= 15
    assert "\u2026" in result
    assert result.startswith("Hello")


def test_truncate_path_no_truncation():
    path = "/a/b/c"
    assert truncate_path(path, max_length=50) == path


def test_truncate_path():
    path = "/very/long/path/to/some/file.txt"
    result = truncate_path(path, max_length=25)
    assert len(result) <= 25
    assert "file.txt" in result
    assert "..." in result


def test_empty_string():
    assert truncate("", max_length=10) == ""


def test_exact_length():
    text = "exactly10!"
    assert truncate(text, max_length=10) == text


def test_single_long_word():
    result = truncate("superlongword", max_length=8)
    assert len(result) <= 8


def test_truncate_words_truncates_with_suffix():
    assert truncate_words("one two three four five", 3) == "one two three..."


def test_truncate_words_no_suffix_when_not_truncated():
    assert truncate_words("one two", 5) == "one two"


def test_truncate_words_empty_string():
    assert truncate_words("", 5) == ""


def test_truncate_words_zero_max_words():
    # max_words=0 yields just the suffix when text has any words.
    assert truncate_words("a b c", 0) == "..."


def test_truncate_words_negative_max_words():
    with pytest.raises(ValueError):
        truncate_words("a b", -1)


def test_wrap_respects_width():
    result = wrap("the quick brown fox jumps over", width=10)
    for line in result.split("\n"):
        assert len(line) <= 10


def test_wrap_preserves_paragraph_breaks():
    result = wrap("para one\n\npara two", width=80)
    assert "\n\n" in result


def test_wrap_invalid_width():
    with pytest.raises(ValueError):
        wrap("hello", width=0)
