import tensorflow as tf
import numpy as np
from prometheus_client import start_http_server, Counter, Gauge

class TrafficAnalyzer:
    def __init__(self):
        self.model = self.build_model()
        self.traffic_gauge = Gauge('traffic_prediction', 'Predicted traffic level')
        
    def build_model(self):
        model = tf.keras.Sequential([
            tf.keras.layers.LSTM(64, input_shape=(24, 10)),
            tf.keras.layers.Dense(32, activation='relu'),
            tf.keras.layers.Dense(1)
        ])
        model.compile(optimizer='adam', loss='mse')
        return model
        
    def analyze_traffic(self, metrics):
        prediction = self.model.predict(metrics)
        self.traffic_gauge.set(prediction[0][0])
        return prediction 