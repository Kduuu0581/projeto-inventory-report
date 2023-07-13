from inventory_report.reports.simple_report import SimpleReport
from inventory_report.product import Product
from typing import Dict, List


class CompleteReport(SimpleReport):
    def generate(self) -> str:
        data = self.inventory.data
        oldest_date = self.oldest_manufacturing_date(data)
        closest_date = self.closest_expiration_date(data)
        largest_inventory = self.largest_inventory(data)
        companies = self.get_all_companies(data)

        return (
            f"Oldest manufacturing date: {oldest_date}\n"
            f"Closest expiration date: {closest_date}\n"
            f"Company with the largest inventory: {largest_inventory}\n"
            f"Stocked products by company:\n"
            f"{companies}"
        )

    def get_all_companies(self, data: List[Product]) -> str:
        companies: Dict[str, int] = {}
        for item in data:
            if not companies.get(item.company_name):
                companies[item.company_name] = 1
            else:
                companies[item.company_name] += 1

        string_to_return = ""

        for key, value in companies.items():
            company = f"- {key}: {value}\n"
            string_to_return += company

        return string_to_return
