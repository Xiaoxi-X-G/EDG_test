import mlflow

def find_or_create_experiment_id(experiment_name):
    """
    experiment_name is string
    
    create experiemnt id and output id if not exists, else output id
    
    output is string
    """
    experiment = mlflow.get_experiment_by_name(experiment_name)
    if experiment is None:
        experiment_id = mlflow.create_experiment(experiment_name)
    else:
        experiment_id = dict(experiment)["experiment_id"]
    return experiment_id