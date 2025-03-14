import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import tensorflow as tf
import joblib
import os

class MLTrainingPipeline:
    def __init__(self):
        self.model = None
        self.scaler = StandardScaler()
        self.model_path = 'ml/models'
        os.makedirs(self.model_path, exist_ok=True)
        
    def prepare_data(self):
        # Simulate historical workload data
        # In production, this would come from Prometheus metrics
        n_samples = 10000
        timestamps = pd.date_range(start='2024-01-01', periods=n_samples, freq='5min')
        
        # Features: CPU usage, memory usage, request count, error rate, latency
        data = {
            'cpu_usage': np.random.uniform(0, 100, n_samples),
            'memory_usage': np.random.uniform(0, 100, n_samples),
            'request_count': np.random.poisson(100, n_samples),
            'error_rate': np.random.beta(1, 30, n_samples),
            'latency': np.random.gamma(2, 0.1, n_samples)
        }
        
        df = pd.DataFrame(data, index=timestamps)
        return df
        
    def create_sequences(self, data, seq_length=24):
        X, y = [], []
        for i in range(len(data) - seq_length):
            X.append(data[i:(i + seq_length)])
            y.append(data[i + seq_length])
        return np.array(X), np.array(y)
        
    def build_model(self, input_shape):
        model = tf.keras.Sequential([
            tf.keras.layers.LSTM(64, input_shape=input_shape, return_sequences=True),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.LSTM(32),
            tf.keras.layers.Dense(16, activation='relu'),
            tf.keras.layers.Dense(5)  # Predict all metrics
        ])
        
        model.compile(
            optimizer='adam',
            loss='mse',
            metrics=['mae']
        )
        return model
        
    def train(self):
        # Prepare data
        df = self.prepare_data()
        
        # Scale the data
        scaled_data = self.scaler.fit_transform(df)
        
        # Create sequences
        X, y = self.create_sequences(scaled_data)
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Build and train model
        self.model = self.build_model(input_shape=(X.shape[1], X.shape[2]))
        
        self.model.fit(
            X_train, y_train,
            epochs=50,
            batch_size=32,
            validation_data=(X_test, y_test),
            callbacks=[
                tf.keras.callbacks.EarlyStopping(patience=5),
                tf.keras.callbacks.ModelCheckpoint(
                    f'{self.model_path}/best_model.h5',
                    save_best_only=True
                )
            ]
        )
        
        # Save scaler
        joblib.dump(self.scaler, f'{self.model_path}/scaler.joblib')
        
if __name__ == "__main__":
    pipeline = MLTrainingPipeline()
    pipeline.train() 