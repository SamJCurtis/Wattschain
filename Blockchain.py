import hashlib
import json
from time import time


class Blockchain(object):

    def __init__(self):
        self.chain = []
        self.currentTransactions = []

        #Create the genesis block
        self.newBlock(previousHash=1, proof=100)


    def newBlock(self, proof, previousHash=None):
        '''
        Create a new Block in the Blockchain

        :param proof: <int> The proof given by the Proof of Work algorithm
        :param previousHash: (Optional) <str> Hash of previous Block
        :return: <dict> New Block
        '''
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.currentTransactions,
            'proof': proof,
            'previousHash': previous_hash or self.hash(self.chain[-1])

        }
        self.currentTransactions = []
        self.chain.append(block)
        return block



    def newTransaction(self,sender, recipient, amount):
        #adds a new transaction to the list of transactions
        '''
        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the Block that will hold this transaction
        '''
        self.currentTransactions.append({
                'sender': sender,
                'recipient': recipient,
                'amount': amount
            })
        return self.lastBlock['index'] + 1


    @staticmethod
    def hash(block)
        '''
        Creates a SHA-256 hash of a Block

        :param block: <dict> Block
        :return: <str>
        '''

        blockString = json.dumps(block,sortKeys=True.encode()
        return hashlib.sha256(blockString).hexdigest()


    @property
    def lastBlock(self)
        #returns the last Block in the chain
        pass

