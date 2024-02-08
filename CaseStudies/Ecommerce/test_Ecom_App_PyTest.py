import pytest
from dao.OrderProcessorRepositoryImpl import OrderProcessorRepositoryImpl
from entity.Customers import Customer
from entity.Products import Product


def test_for_create_product(mocker):
    creating_product = OrderProcessorRepositoryImpl()
    mock_create_product = mocker.patch('dao.OrderProcessorRepositoryImpl.OrderProcessorRepositoryImpl.createProduct')
    test_cases = [
        (Product("Product To Test", 400.5, "demo_category", 50), True)
    ]
    for product, expected_value in test_cases:
        mock_create_product.return_value = expected_value
        result = creating_product.createProduct(product)
        assert result == expected_value


def test_for_create_customer(mocker):
    registration_process = OrderProcessorRepositoryImpl()
    mock_create_customer = mocker.patch('dao.OrderProcessorRepositoryImpl.OrderProcessorRepositoryImpl.createCustomer')
    test_cases = [
        (Customer("Customer to test", "testemailcom", "Testing@1"), False),
        (Customer("Customer2 to test", "test.email@gmail.com", "Testin1@"), True)
    ]
    for customer, expected_value in test_cases:
        mock_create_customer.return_value = expected_value
        result = registration_process.createCustomer(customer)
        assert result == expected_value


def test_for_place_order(mocker):
    placing_order = OrderProcessorRepositoryImpl()
    mock_place_order = mocker.patch('dao.OrderProcessorRepositoryImpl.OrderProcessorRepositoryImpl.placeOrder')
    test_cases = [
        (Customer("TestCustomer", "test@email.test", "Test@1"),
         [Product("TestProduct", "test_category", "testing", 50), 2],
         "RDS Testing", True),
        (Customer("TestCustomer", "test@email.test", "Test@1"), [Product("TestProduct", 700.5, "testing", 50), 5],
         "RDS Testing", True),
    ]
    for customer, product, address, expected_value in test_cases:
        mock_place_order.return_value = expected_value
        result = placing_order.placeOrder(customer, product, address)
        assert result == expected_value


def test_for_exception_handling(mocker):
    creating_customer = OrderProcessorRepositoryImpl()
    mock_create_customer = mocker.patch("dao.OrderProcessorRepositoryImpl.OrderProcessorRepositoryImpl.get_customer_by_id")
    test_cases = [
        (9999, True),
        (9999, False)
    ]
    for c_id, expected_output in test_cases:
        mock_create_customer.return_value = expected_output
        result = creating_customer.get_customer_by_id(c_id)
        assert result == mock_create_customer.return_value
