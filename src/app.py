from flask import Flask, request, jsonify
from distributed_ledger import DistributedLedger

app = Flask(__name__)

node_id = 1
nodes = [1, 2, 3]
ledger = DistributedLedger(node_id, nodes)

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    transaction = request.get_json()
    ledger.add_transaction(**transaction)
    return jsonify({'message': 'Transaction added'})

@app.route('/mine_block', methods=['POST'])
def mine_block():
    ledger.mine_block()
    return jsonify({'message': 'Block mined'})

@app.route('/receive_block', methods=['POST'])
def receive_block():
    block = request.get_json()
    if ledger.receive_block(block):
        return jsonify({'message': 'Block received'})
    return jsonify({'message': 'Invalid block'})

if __name__ == '__main__':
    app.run(port=5000)
