from kubernetes import client, config
from prometheus_client import start_http_server, Gauge
import numpy as np
import time
import logging

class MLMetricsAdapter:
    def __init__(self):
        config.load_kube_config()
        self.k8s_client = client.CustomObjectsApi()
        self.prediction_gauge = Gauge('ml_prediction', 'ML-based workload prediction')
        
    def collect_metrics(self):
        """Collect current system metrics"""
        metrics = {
            'cpu_usage': self.get_cpu_metrics(),
            'request_rate': self.get_request_rate(),
            'error_rate': self.get_error_rate()
        }
        return metrics
        
    def predict_workload(self, metrics):
        """Use ML model to predict workload"""
        from ml.training.train_pipeline import MLTrainingPipeline
        pipeline = MLTrainingPipeline()
        prediction = pipeline.model.predict(np.array([list(metrics.values())]))
        return prediction[0]
        
    def update_hpa_metrics(self, prediction):
        """Update HPA with prediction metrics"""
        self.prediction_gauge.set(prediction)
        
    def run(self):
        """Main loop"""
        start_http_server(8000)
        while True:
            try:
                metrics = self.collect_metrics()
                prediction = self.predict_workload(metrics)
                self.update_hpa_metrics(prediction)
                logging.info(f"Updated metrics with prediction: {prediction}")
                time.sleep(15)  # Update every 15 seconds
            except Exception as e:
                logging.error(f"Error in metrics adapter: {e}")
                time.sleep(5)

if __name__ == "__main__":
    adapter = MLMetricsAdapter()
    adapter.run() 