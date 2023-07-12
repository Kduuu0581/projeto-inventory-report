from inventory_report.product import Product


def test_create_product() -> None:
    product = Product(
        "1",
        "Arroz",
        "Marca",
        "10/10/2020",
        "10/10/2021",
        "123456",
        "Manter em local seco e arejado",
    )
    assert product.id == "1"
    assert product.product_name == "Arroz"
    assert product.company_name == "Marca"
    assert product.manufacturing_date == "10/10/2020"
    assert product.expiration_date == "10/10/2021"
    assert product.serial_number == "123456"
    assert product.storage_instructions == "Manter em local seco e arejado"
