import copy
from stats import DEFAULT_STATS


class Character:
    def __init__(self, name: str, character_class: str, race: str,  level: int, stats: dict = None):
        self.name = name
        self.level = level
        self.stats = stats if stats is not None else copy.deepcopy(DEFAULT_STATS) #default stats if not provided

    def __repr__(self):
        return f"Character(name={self.name}, level={self.level}, stats={self.stats.hit_points})"
