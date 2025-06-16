"""Configuration settings for the D&D MCP Server application."""

API_BASE_URL = "https://www.dnd5eapi.co/api"
REQUEST_TIMEOUT_SECONDS = 10


class Categories:
    """Enumeration of D&D API categories for better type safety."""

    ABILITY_SCORES = "ability-scores"
    ALIGNMENTS = "alignments"
    BACKGROUNDS = "backgrounds"
    CLASSES = "classes"
    CONDITIONS = "conditions"
    DAMAGE_TYPES = "damage-types"
    EQUIPMENT = "equipment"
    EQUIPMENT_CATEGORIES = "equipment-categories"
    FEATS = "feats"
    FEATURES = "features"
    LANGUAGES = "languages"
    MAGIC_ITEMS = "magic-items"
    MAGIC_SCHOOLS = "magic-schools"
    MONSTERS = "monsters"
    PROFICIENCIES = "proficiencies"
    RACES = "races"
    RULE_SECTIONS = "rule-sections"
    RULES = "rules"
    SKILLS = "skills"
    SPELLS = "spells"
    SUBCLASSES = "subclasses"
    SUBRACES = "subraces"
    TRAITS = "traits"
    WEAPON_PROPERTIES = "weapon-properties"


CATEGORY_DESCRIPTIONS = {
    Categories.ABILITY_SCORES: "The six abilities that describe a character's physical and mental characteristics",  # noqa: E501
    Categories.ALIGNMENTS: "The moral and ethical attitudes and behaviors of creatures",
    Categories.BACKGROUNDS: "Character backgrounds and their features",
    Categories.CLASSES: "Character classes with features, proficiencies, and subclasses",
    Categories.CONDITIONS: "Status conditions that affect creatures",
    Categories.DAMAGE_TYPES: "Types of damage that can be dealt",
    Categories.EQUIPMENT: "Items, weapons, armor, and gear for adventuring",
    Categories.EQUIPMENT_CATEGORIES: "Categories of equipment",
    Categories.FEATS: "Special abilities and features",
    Categories.FEATURES: "Class and racial features",
    Categories.LANGUAGES: "Languages spoken throughout the multiverse",
    Categories.MAGIC_ITEMS: "Magical equipment with special properties",
    Categories.MAGIC_SCHOOLS: "Schools of magic specialization",
    Categories.MONSTERS: "Creatures and foes",
    Categories.PROFICIENCIES: "Skills and tools characters can be proficient with",
    Categories.RACES: "Character races and their traits",
    Categories.RULE_SECTIONS: "Sections of the game rules",
    Categories.RULES: "Game rules",
    Categories.SKILLS: "Character skills tied to ability scores",
    Categories.SPELLS: "Magic spells with effects, components, and descriptions",
    Categories.SUBCLASSES: "Specializations within character classes",
    Categories.SUBRACES: "Variants of character races",
    Categories.TRAITS: "Racial traits",
    Categories.WEAPON_PROPERTIES: "Special properties of weapons",
}
