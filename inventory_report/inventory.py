from inventory_report.product import Product
from typing import List, Optional


class Inventory:
    def __init__(self, data: Optional[List[Product]] = None):
        if data is None:
            data = []
        self._data = data.copy()

    @property
    def data(self) -> List[Product]:
        return self._data.copy()

    def add_product(self, product: List[Product]) -> None:
        self._data.extend(product)
