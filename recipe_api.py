"""
Local recipe lookup — no external API required.

Returns recipes from a hardcoded dictionary, keyed by ingredient name
(lowercase). Add more ingredients/recipes to RECIPE_DB below to expand
coverage. Each recipe is a dict shaped the same way app.py expects, so
no changes are needed in app.py.
"""

# ---------------------------------------------------------------------
# Add / edit recipes here. Key = ingredient name (lowercase).
# Each recipe needs: title, image (optional URL, or leave "" ), and
# usedIngredientCount (optional, just for display).
# ---------------------------------------------------------------------
RECIPE_DB = {
    "tomato": [
        {
            "title": "Classic Tomato Soup",
            "image": "https://images.unsplash.com/photo-1547592166-23ac45744acd?w=400",
            "usedIngredientCount": 1,
        },
        {
            "title": "Tomato Basil Pasta",
            "image": "https://images.unsplash.com/photo-1621996346565-e3dbc353d2e5?w=400",
            "usedIngredientCount": 2,
        },
        {
            "title": "Fresh Tomato Salsa",
            "image": "https://images.unsplash.com/photo-1600335895229-6e75511892c8?w=400",
            "usedIngredientCount": 3,
        },
    ],
    "banana": [
        {
            "title": "Banana Smoothie",
            "image": "https://images.unsplash.com/photo-1553530666-ba11a7da3888?w=400",
            "usedIngredientCount": 1,
        },
        {
            "title": "Banana Bread",
            "image": "https://images.unsplash.com/photo-1605286658233-e34e64f56c8a?w=400",
            "usedIngredientCount": 4,
        },
    ],
    "apple": [
        {
            "title": "Apple Cinnamon Oatmeal",
            "image": "https://images.unsplash.com/photo-1568051243858-533a607809a5?w=400",
            "usedIngredientCount": 2,
        },
        {
            "title": "Classic Apple Pie",
            "image": "https://images.unsplash.com/photo-1568571780765-9276ac8b75a2?w=400",
            "usedIngredientCount": 5,
        },
    ],
    "potato": [
        {
            "title": "Crispy Roasted Potatoes",
            "image": "https://images.unsplash.com/photo-1518977676601-b53f82aba655?w=400",
            "usedIngredientCount": 1,
        },
        {
            "title": "Mashed Potatoes",
            "image": "https://images.unsplash.com/photo-1600891964092-4316c288032e?w=400",
            "usedIngredientCount": 3,
        },
    ],
    "carrot": [
        {
            "title": "Carrot Ginger Soup",
            "image": "https://images.unsplash.com/photo-1476718406336-bb5a9690ee2a?w=400",
            "usedIngredientCount": 2,
        },
    ],
    "egg": [
        {
            "title": "Simple Scrambled Eggs",
            "image": "https://images.unsplash.com/photo-1525351484163-7529414344d8?w=400",
            "usedIngredientCount": 1,
        },
        {
            "title": "Vegetable Omelette",
            "image": "https://images.unsplash.com/photo-1510693206972-df098062cb71?w=400",
            "usedIngredientCount": 4,
        },
    ],
    "chicken": [
        {
            "title": "Grilled Chicken Breast",
            "image": "https://images.unsplash.com/photo-1532550907401-a500c9a57435?w=400",
            "usedIngredientCount": 1,
        },
    ],
    "rice": [
        {
            "title": "Simple Fried Rice",
            "image": "https://images.unsplash.com/photo-1603133872878-684f208fb84b?w=400",
            "usedIngredientCount": 3,
        },
    ],
}


def getrecipe(foodname: str, number: int = 5) -> list[dict]:
    """
    Looks up recipes for `foodname` in the local RECIPE_DB.

    Args:
        foodname: Ingredient name typed by the user (case-insensitive).
        number: Max number of recipes to return.

    Returns:
        A list of recipe dicts, or [] if the ingredient isn't in the
        local database.
    """
    foodname = (foodname or "").strip().lower()

    if not foodname:
        return []

    recipes = RECIPE_DB.get(foodname, [])

    return recipes[:number]
