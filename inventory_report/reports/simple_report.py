import typing
from inventory_report.reports.report import Report
from inventory_report.inventory import Inventory
from inventory_report.product import Product
from typing import List
from datetime import datetime, date


class SimpleReport(Report):
    def add_inventory(self, inventory: Inventory) -> None:
        self.inventory = inventory

    def generate(self) -> str:
        data = self.inventory.data
        oldest_date = self.oldest_manufacturing_date(data)
        closest_date = self.closest_expiration_date(data)
        largest_inventory = self.largest_inventory(data)

        return (
            f"Oldest manufacturing date: {oldest_date}\n"
            f"Closest expiration date: {closest_date}\n"
            f"Company with the largest inventory: {largest_inventory}\n"
        )

    def oldest_manufacturing_date(self, data: List[Product]) -> str:
        oldest_date = min(item.manufacturing_date for item in data)
        return oldest_date

    def closest_expiration_date(self, data: List[Product]) -> str:
        today = date.today()
        closest_date = min(
            item.expiration_date
            for item in data
            if datetime.strptime(item.expiration_date, "%Y-%m-%d").date()
            >= today
        )
        return closest_date

    def largest_inventory(self, data: List[Product]) -> str:
        companies: typing.Dict[str, int] = {}
        for item in data:
            if not companies.get(item.company_name):
                companies[item.company_name] = 1
            else:
                companies[item.company_name] += 1
        return max(companies, key=lambda item: companies[item])
