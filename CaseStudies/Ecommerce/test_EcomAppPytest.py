import unittest
from unittest.mock import patch
from dao.OrderProcessorRepositoryImpl import OrderProcessorRepositoryImpl
from entity.Customers import Customer
from entity.Products import Product
from myexceptions.CustomerNotFound import CustomerNotFoundException


class TestProductCreation(unittest.TestCase):
    def setUp(self):
        self.service = OrderProcessorRepositoryImpl()  # Assuming Service is the class where createProduct is called

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
    def test_for_place_order(self, mock_place_order):
        customer_id = 1
        customer = self.service.get_customer_by_id(customer_id)
        product_id = 1
        product = self.service.get_product_by_id(product_id)
        products_quantities = [(product, 2)]
        shipping_address = "Test Address"
        test_cases = [
            (customer, products_quantities, shipping_address, True)
        ]
        for customer, product, shipping_address, expected in test_cases:
            mock_place_order.return_value = expected
            result = self.service.placeOrder(customer, product, shipping_address)
            self.assertEqual(result, mock_place_order.return_value)
            mock_place_order.assert_called_with(customer, product, shipping_address)

    def test_for_exception_handling(self):
        pass
        # with self.assertRaises(CustomerNotFoundException):
        # mock_customer.return_value = CustomerNotFoundException("Customer not found.")
        # customer_id = 111
        # customer = self.service.get_customer_by_id(customer_id)
        # self.assertEquals(customer, mock_customer.return_value)


if __name__ == '__main__':
    unittest.main()
