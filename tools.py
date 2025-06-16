import logging
from typing import Any

from fastmcp import FastMCP

import api
import config

logger = logging.getLogger(__name__)


def register_tools(app: FastMCP) -> None:
    """Register all resources with the FastMCP app."""

    @app.tool
    def get_categories() -> dict[str, Any]:
        """List all available D&D 5e API categories for browsing the official content.

        This resource provides a comprehensive list of all categories available in the D&D 5e API,
        such as spells, monsters, equipment, classes, races, and more. Each category entry includes
        a name, description, and endpoint URL.

        This is typically the first resource to access when exploring the D&D 5e API, as it provides
        an overview of all available content categories and their endpoints.

        The data is cached to improve performance on subsequent requests.

        Returns:
            A dictionary containing all available D&D 5e API categories with descriptions
            and endpoints, with source attribution to the D&D 5e API.

        """
        logger.info("Fetching D&D API categories")
        try:
            return api.fetch_categories()
        except Exception as e:
            logger.exception(f"Error fetching categories: {e}")
            return {"error": f"Failed to fetch categories: {e!s}"}

    @app.tool
    def get_items(category: str) -> dict[str, Any]:
        """Retrieve a list of all items available in a specific D&D 5e API category.

        This resource provides access to all items within a specified category, such as all spells,
        all monsters, all equipment, etc. The response includes basic information about each item
        (name and index) that can be used to retrieve detailed information via the item details resource.

        Common categories include:
        - spells: All spells in the D&D 5e ruleset
        - monsters: All monsters and creatures
        - equipment: All standard equipment items
        - magic-items: All magical items and artifacts
        - classes: All character classes
        - races: All playable races

        The data is cached to improve performance on subsequent requests.

        Args:
            category: The D&D API category to retrieve items from (e.g., 'spells', 'monsters', 'equipment')

        Returns:
            A dictionary containing all items in the specified category with basic information,
            with source attribution to the D&D 5e API.

        """  # noqa: E501
        logger.debug(f"Fetching items for category: {category}")

        # Validate category
        if category not in config.CATEGORY_DESCRIPTIONS:
            logger.error(f"Invalid category requested: {category}")
            return {
                "error": f"Category '{category}' not found. Available categories: {', '.join(config.CATEGORY_DESCRIPTIONS.keys())}"  # noqa: E501
            }

        try:
            return api.fetch_items(category)
        except Exception as e:
            logger.exception(e)
            return {"error": f"Failed to fetch items for {category}: {e!s}"}

    @app.tool
    def get_item(category: str, index: str) -> dict[str, Any]:
        """Retrieve detailed information about a specific D&D 5e item by its category and index.

        This resource provides comprehensive details about a specific D&D item, including all of its
        properties, descriptions, mechanics, and related information. The response structure varies
        based on the category, as different types of items have different properties:

        - Spells: Includes level, casting time, range, components, duration, description, etc.
        - Monsters: Includes challenge rating, hit points, armor class, abilities, actions, etc.
        - Equipment: Includes cost, weight, properties, damage (for weapons), etc.
        - Classes: Includes proficiencies, spellcasting abilities, class features, etc.
        - Races: Includes ability bonuses, traits, languages, etc.

        The data is cached to improve performance on subsequent requests.

        Args:
            category: The D&D API category the item belongs to (e.g., 'spells', 'monsters', 'equipment')
            index: The unique identifier for the specific item (e.g., 'fireball', 'adult-red-dragon')

        Returns:
            A dictionary containing detailed information about the requested item,
            with source attribution to the D&D 5e API.

        """
        logger.debug(f"Fetching item details: {category}/{index}")
        try:
            return api.fetch_item(category, index)
        except Exception as e:
            logger.exception(f"Error fetching item {category}/{index}: {e}")
            return {"error": f"Failed to fetch item {category}/{index}: {e!s}"}
