import numpy as np
from sklearn.model_selection import train_test_split
from predictor import WorkloadPredictor
import joblib

class MLTrainer:
    def __init__(self):
        self.predictor = WorkloadPredictor()
        
    def generate_sample_data(self):
        # Generate synthetic training data
        n_samples = 1000
        X = np.random.rand(n_samples, 10)  # 10 features
        y = np.sum(X, axis=1) * 0.3 + np.random.normal(0, 0.1, n_samples)
        return X, y
        
    def train_model(self):
        X, y = self.generate_sample_data()
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        
        self.predictor.build_model()
        self.predictor.train(X_train, y_train)
        
        # Save the model
        joblib.dump(self.predictor.model, 'ml/models/scaling_model.joblib')
        
if __name__ == "__main__":
    trainer = MLTrainer()
    trainer.train_model() 