import tensorflow as tf
import numpy as np

class AIConsensus:
    def __init__(self, model_path):
        self.model = tf.keras.models.load_model(model_path)

    def predict(self, transactions):
        transactions = np.array(transactions)
        predictions = self.model.predict(transactions)
        return predictions

    def train(self, transactions, labels):
        transactions = np.array(transactions)
        labels = np.array(labels)
        self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        self.model.fit(transactions, labels, epochs=10, batch_size=32)
        self.model.save('model.h5')
