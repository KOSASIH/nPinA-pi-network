import unittest

class TestDistributedLedger(unittest.TestCase):
    def setUp(self):
        # Set up
        self.node_id = 1
        self.nodes = [1, 2, 3]
        self.ledger = DistributedLedger(self.node_id, self.nodes)

    def test_create_genesis_block(self):
        # Test create_genesis_block function
        # ...

    def test_add_transaction(self):
        # Test add_transaction function
        # ...

    def test_mine_block(self):
        # Test mine_block function
        # ...

    def test_get_previous_hash(self):
        # Test get_previous_hash function
        # ...

    def test_calculate_hash(self):
        # Test calculate_hash function
        # ...

    def test_propagate_block(self):
        # Test propagate_block function
        # ...

    def test_is_chain_valid(self):
        # Test is_chain_valid function
        # ...

    def test_validate_transactions(self):
        # Test validate_transactions function
        # ...

    def test_receive_block(self):
        # Test receive_block function
        # ...

    def tearDown(self):
        # Clean up
        # ...

if __name__ == '__main__':
    unittest.main()
