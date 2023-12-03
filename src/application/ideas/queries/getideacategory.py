
from ....persistence.ideacategories import getideacategories

def fetch_idea_category_list() -> dict:
    return getideacategories.get_idea_categories()
