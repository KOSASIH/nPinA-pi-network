import json
import time
import hashlib
import requests

class DistributedLedger:
    def __init__(self, node_id, nodes):
        self.node_id = node_id
        self.nodes = nodes
        self.chain = [self.create_genesis_block()]
        self.pending_transactions = []

    def create_genesis_block(self):
        return {
            'index': 0,
            'timestamp': int(time.time()),
            'transactions': [],
            'previous_hash': '0' * 64,
            'nonce': 0
        }

    def add_transaction(self, sender, receiver, amount):
        transaction = {
            'sender': sender,
            'receiver': receiver,
            'amount': amount,
            'timestamp': int(time.time())
        }
        self.pending_transactions.append(transaction)

    def mine_block(self):
        block = {
            'index': len(self.chain),
            'timestamp': int(time.time()),
            'transactions': self.pending_transactions,
            'previous_hash': self.get_previous_hash(),
            'nonce': 0
        }
        block['hash'] = self.calculate_hash(block)
        self.chain.append(block)
        self.pending_transactions = []
        self.propagate_block(block)

    def get_previous_hash(self):
        return self.chain[-1]['hash']

    def calculate_hash(self, block):
        block_string = json.dumps(block, sort_keys=True).encode()
        block_hash = hashlib.sha256(block_string).hexdigest()
        return block_hash

    def propagate_block(self, block):
        for node in self.nodes:
            if node != self.node_id:
                requests.post(f'http://localhost:{node}/receive_block', json=block)

    def is_chain_valid(self, chain):
        for i in range(1, len(chain)):
            current_block = chain[i]
            previous_block = chain[i - 1]
            if current_block['previous_hash'] != self.calculate_hash(previous_block):
                return False
            if not self.validate_transactions(current_block['transactions']):
                return False
        return True

    def validate_transactions(self, transactions):
        aic = AIConsensus('model.h5')
        for transaction in transactions:
            if not aic.predict([transaction]):
                return False
        return True

    def receive_block(self, block):
        if self.is_chain_valid([block]):
            self.chain.append(block)
            return True
        return False
