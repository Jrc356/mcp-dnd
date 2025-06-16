"""Tests for dnd_mcp.api module."""

import requests

import api


class DummyResponse:
    """Dummy response for mocking requests."""

    def __init__(self, json_data, status_code):
        """Initialize with JSON data and status code."""
        self._json = json_data
        self.status_code = status_code

    def json(self):
        """Return the stored JSON data."""
        return self._json


def test_fetch_categories_success(monkeypatch):
    """Test successful fetch_categories call."""
    dummy_json = {"monsters": {}, "spells": {}}

    def mock_get(*args, **kwargs):
        return DummyResponse(dummy_json, 200)

    monkeypatch.setattr(requests, "get", mock_get)
    result = api.fetch_categories()
    assert "categories" in result
    assert result["count"] == 2


def test_fetch_categories_failure(monkeypatch):
    """Test fetch_categories with failed request."""

    def mock_get(*args, **kwargs):
        return DummyResponse({}, 404)

    monkeypatch.setattr(requests, "get", mock_get)
    result = api.fetch_categories()
    assert "error" in result


def test_fetch_items_success(monkeypatch):
    """Test successful fetch_items call."""
    dummy_json = {"results": [{"name": "Goblin", "index": "goblin"}]}

    def mock_get(*args, **kwargs):
        return DummyResponse(dummy_json, 200)

    monkeypatch.setattr(requests, "get", mock_get)
    result = api.fetch_items("monsters")
    assert result["count"] == 1
    assert result["items"][0]["name"] == "Goblin"


def test_fetch_items_failure(monkeypatch):
    """Test fetch_items with failed request."""

    def mock_get(*args, **kwargs):
        return DummyResponse({}, 404)

    monkeypatch.setattr(requests, "get", mock_get)
    result = api.fetch_items("monsters")
    assert "error" in result


def test_fetch_item_success(monkeypatch):
    """Test successful fetch_item call."""
    dummy_json = {"name": "Goblin", "index": "goblin"}

    def mock_get(*args, **kwargs):
        return DummyResponse(dummy_json, 200)

    monkeypatch.setattr(requests, "get", mock_get)
    result = api.fetch_item("monsters", "goblin")
    assert result["name"] == "Goblin"


def test_fetch_item_failure(monkeypatch):
    """Test fetch_item with failed request."""

    def mock_get(*args, **kwargs):
        return DummyResponse({}, 404)

    monkeypatch.setattr(requests, "get", mock_get)
    result = api.fetch_item("monsters", "goblin")
    assert "error" in result


def test_fetch_item_invalid_format(monkeypatch):
    """Test fetch_item with invalid response format."""

    class WeirdResponse:
        status_code = 200

        def json(self):
            return [1, 2, 3]

    def mock_get(*args, **kwargs):
        return WeirdResponse()

    monkeypatch.setattr(requests, "get", mock_get)
    result = api.fetch_item("monsters", "goblin")
    assert "error" in result
