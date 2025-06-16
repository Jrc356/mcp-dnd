"""D&D 5e API client module."""

import logging
from typing import Any

import requests

import config as config

logger = logging.getLogger(__name__)


def fetch_categories() -> dict[str, Any]:
    """Fetch all available D&D 5e API categories from the official API."""
    response = requests.get(f"{config.API_BASE_URL}/", timeout=config.REQUEST_TIMEOUT_SECONDS)
    if response.status_code != 200:
        logger.error(f"Failed to fetch categories: {response.status_code}")
        return {"error": f"API request failed with status {response.status_code}"}

    data = response.json()
    categories = []
    for key in data.keys():
        description = config.CATEGORY_DESCRIPTIONS.get(key, f"Collection of D&D 5e {key}")
        categories.append(
            {
                "name": key,
                "description": description,
                "uri": f"resource://dnd/items/{key}",
            }
        )

    return {"categories": categories, "count": len(categories)}


def fetch_items(category: str) -> dict[str, Any]:
    """Fetch all items in a specific D&D 5e API category."""
    response = requests.get(
        f"{config.API_BASE_URL}/{category}", timeout=config.REQUEST_TIMEOUT_SECONDS
    )
    if response.status_code != 200:
        logger.error(f"Failed to fetch items for {category}: {response.status_code}")
        return {"error": f"Category '{category}' not found or API request failed"}

    data = response.json()

    # Transform to resource format
    items = []
    for item in data.get("results", []):
        item_uri = f"resource://dnd/item/{category}/{item['index']}"
        items.append(
            {
                "name": item["name"],
                "index": item["index"],
                "uri": item_uri,
            }
        )

    return {
        "category": category,
        "count": len(items),
        "items": items,
        "source": "D&D 5e API (www.dnd5eapi.co)",
    }


def fetch_item(category: str, index: str) -> dict[str, Any]:
    """Fetch detailed information about a specific D&D 5e item by category and index."""
    response = requests.get(
        f"{config.API_BASE_URL}/{category}/{index}",
        timeout=config.REQUEST_TIMEOUT_SECONDS,
        allow_redirects=True,
    )

    if response.status_code != 200:
        logger.error(f"Failed to fetch item {category}/{index}: {response.status_code}")
        return {"error": f"Item '{index}' not found in category '{category}' or API request failed"}

    data = response.json()
    if not isinstance(data, dict):
        logger.error(f"Expected dict from API, got {type(data).__name__}")
        return {"error": "Invalid response format from API"}
    return data
