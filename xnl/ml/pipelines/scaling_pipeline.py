from kfp import dsl, components
from kfp.components import func_to_container_op

@func_to_container_op
def prepare_data():
    import pandas as pd
    import numpy as np
    
    # Generate training data
    n_samples = 10000
    data = {
        'cpu_usage': np.random.uniform(0, 100, n_samples),
        'memory_usage': np.random.uniform(0, 100, n_samples),
        'request_count': np.random.poisson(100, n_samples)
    }
    df = pd.DataFrame(data)
    df.to_csv('/data/training_data.csv', index=False)
    return '/data/training_data.csv'

@func_to_container_op
def train_model(data_path: str):
    from ml.training.train_pipeline import MLTrainingPipeline
    
    pipeline = MLTrainingPipeline()
    pipeline.train()
    return '/ml/models/best_model.h5'

@dsl.pipeline(
    name='Scaling Model Pipeline',
    description='Pipeline to train and deploy scaling model'
)
def scaling_pipeline():
    data_op = prepare_data()
    train_op = train_model(data_op.output) 