from collections import defaultdict
import lxml.etree as ET


class Parser:
    def __init__(self, path):
        self._path = path
        self._items = []

    @property
    def all_items(self) -> list[dict]:
        """
        get all items
        """
        if self._items:
            return [list(i.keys())[0] for i in self._items]

        self._parse_file()
        return [list(i.keys())[0] for i in self._items]

    @property
    def items_with_spare_parts(self) -> list[dict]:
        """
        get only the items with spare parts
        """
        if self._items:
            return [i for i in self._items if all(bool(value) for value in i.values())]

        self._parse_file()
        return [i for i in self._items if all(bool(value) for value in i.values())]

    @property
    def count(self) -> int:
        """
        get count
        """
        if self._items:
            return len(self._items)

        self._parse_file()
        return len(self._items)

    def _parse_file(self):
        """
        parse the file to list of dicts where each key is the root item name
        and value is the list of nested (nahradni dily) items,
        if root item does not have nested, value is empty list

        example: [{a: ["Arrma diferenciál kompletní 37T 1.35M", "Arrma hřídel posuvná kompozit"]},
                {b: []},
                {c: []}]
        """
        nested = []
        for event, element in ET.iterparse(self._path, events=("start", "end")):
            parent = element.getparent()
            is_valid = parent is not None

            if is_valid and event == "start" and parent.tag == "items":
                nested = []

            if is_valid and event == "start" and parent.tag == "part" and parent.get("name") == "Náhradní díly":
                nested.append(element.get("name"))

            if is_valid and event == "end" and parent.tag == "items":
                item = defaultdict(list)
                item[element.get("name")].extend(nested)
                self._items.append(item)
