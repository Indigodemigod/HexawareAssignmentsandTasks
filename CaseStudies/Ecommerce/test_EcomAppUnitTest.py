import unittest
from unittest.mock import patch
from dao.OrderProcessorRepositoryImpl import OrderProcessorRepositoryImpl
from entity.Customers import Customer
from entity.Products import Product
from myexceptions.CustomerNotFound import CustomerNotFoundException


class TestProductCreation(unittest.TestCase):
    def setUp(self):
        self.service = OrderProcessorRepositoryImpl()

    @patch('dao.OrderProcessorRepositoryImpl.OrderProcessorRepositoryImpl.createProduct')
    def test_for_create_product(self, mock_create_product):
        test_cases = [
            (Product("Product to test", 2000.0, "Testing", 20), True)
        ]
        for product, expected_result in test_cases:
            mock_create_product.return_value = expected_result
            result = self.service.createProduct(product)
            self.assertEqual(result, expected_result)
            mock_create_product.assert_called_with(product)

    @patch('dao.OrderProcessorRepositoryImpl.OrderProcessorRepositoryImpl.createCustomer')
    def test_for_create_customer(self, mock_create_customer):
        test_cases = [
            (Customer("Customer to test", "testemailcom", "Testing@1"), False),
            (Customer("Customer2 to test", "test.email@gmail.com", "Testin1@"), True)
        ]
        for customer, expected_result in test_cases:
            mock_create_customer.return_value = expected_result
            result = self.service.createCustomer(customer)
            self.assertEqual(result, mock_create_customer.return_value)
            mock_create_customer.assert_called_with(customer)

    @patch('dao.OrderProcessorRepositoryImpl.OrderProcessorRepositoryImpl.placeOrder')
    @patch('dao.OrderProcessorRepositoryImpl.OrderProcessorRepositoryImpl.get_customer_by_id')
    @patch('dao.OrderProcessorRepositoryImpl.OrderProcessorRepositoryImpl.get_product_by_id')
    def test_for_place_order(self, mock_get_product_by_id, mock_get_customer_by_id, mock_place_order):
        customer_id = 1
        mock_get_customer_by_id.return_value = Customer("Test Customer", "test@example.com", "password")
        product_id = 1
        mock_get_product_by_id.return_value = Product("Test Product", 100.0, "Description", 10)
        products_quantities = [(mock_get_product_by_id.return_value, 2)]
        shipping_address = "Test Address"
        test_cases = [
            (mock_get_customer_by_id.return_value, products_quantities, shipping_address, True)
        ]
        for customer, product, shipping_address, expected in test_cases:
            mock_place_order.return_value = expected
            result = self.service.placeOrder(customer, product, shipping_address)
            self.assertEqual(result, mock_place_order.return_value)
            mock_place_order.assert_called_with(customer, product, shipping_address)

    @patch('dao.OrderProcessorRepositoryImpl.OrderProcessorRepositoryImpl.get_customer_by_id')
    def test_for_exception_handling(self, mock_get_customer_by_id):
        mock_get_customer_by_id.side_effect = CustomerNotFoundException("Customer not found.")
        customer_id = 111
        with self.assertRaises(CustomerNotFoundException):
            self.service.get_customer_by_id(customer_id)


if __name__ == '__main__':
    unittest.main()
