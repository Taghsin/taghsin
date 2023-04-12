from typing import List, NamedTuple


class TagModel(NamedTuple):
    key: str
    value: str


class TagList(NamedTuple):
    tags: List[TagModel]
