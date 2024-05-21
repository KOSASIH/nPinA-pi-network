import unittest

from .test_ai_consensus import TestAIConsensus
from .test_cryptography import TestCryptography
from .test_distributed_ledger import TestDistributedLedger

def main():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestAIConsensus))
    test_suite.addTest(unittest.makeSuite(TestCryptography))
    test_suite.addTest(unittest.makeSuite(TestDistributedLedger))
    unittest.TextTestRunner(verbosity=2).run(test_suite)

if __name__ == '__main__':
    main()
