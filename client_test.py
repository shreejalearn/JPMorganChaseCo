import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):

  def assertDataPointEqual(self, quote, expected_stock, expected_bid_price, expected_ask_price):
    expected_data_point = (
        expected_stock,
        float(quote['top_bid']['price']),
        float(quote['top_ask']['price']),
        (float(quote['top_bid']['price']) + float(quote['top_ask']['price'])) / 2
    )
    self.assertEqual(getDataPoint(quote), expected_data_point)


  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    self.assertDataPointEqual(quotes[0], 'ABC', 120.48, 121.2)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    self.assertDataPointEqual(quotes[0], 'ABC', 120.48, 119.2)


  """ ------------ Add more unit tests ------------ """
if __name__ == '__main__':
    unittest.main()