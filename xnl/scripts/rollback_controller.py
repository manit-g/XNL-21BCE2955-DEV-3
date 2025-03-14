from kubernetes import client, config
import time
import logging

class RollbackController:
    def __init__(self):
        config.load_kube_config()
        self.k8s_apps = client.AppsV1Api()
        
    def check_deployment_health(self, name, namespace):
        deployment = self.k8s_apps.read_namespaced_deployment(name, namespace)
        if deployment.status.available_replicas < deployment.spec.replicas:
            return False
        return True
        
    def rollback_deployment(self, name, namespace):
        logging.info(f"Rolling back deployment {name} in namespace {namespace}")
        self.k8s_apps.patch_namespaced_deployment(
            name=name,
            namespace=namespace,
            body={"spec": {"template": {"metadata": {"annotations": {"rollback": "true"}}}}}
        ) 