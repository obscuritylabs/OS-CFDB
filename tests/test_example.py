from example.main import greet


def test_greet() -> None:
    """Test that greeting properly greets."""
    assert greet("Tory") == "Hello, Tory"
