import os.path

from examples.simple_pipeline import THIS_DIR
from examples.utils import get_client, create_experiment_and_upload_pipeline

USER_NAMESPACE = "admin"
EXPERIMENT_NAME = 'test experiment'
EXPERIMENT_DESCRIPTION = "Experiment for examples"
JOB_NAME = 'simple pipeline job example'
PIPELINE_NAME = "simple pipeline"
PIPELINE_DESCRIPTION = "simple pipeline example"
COMPILED_PIPELINE_NAME = 'simple_pipeline.py.tar.gz'


if __name__ == '__main__':
    client = get_client()

    pipeline, experiment = create_experiment_and_upload_pipeline(
        client,
        PIPELINE_NAME,
        os.path.join(THIS_DIR, COMPILED_PIPELINE_NAME),
        pipeline_description=PIPELINE_DESCRIPTION,
        experiment_name=EXPERIMENT_NAME,
        experiment_description=EXPERIMENT_DESCRIPTION,
        user_namespace=USER_NAMESPACE
    )

    # Run a pipeline
    pipeline_run = client.run_pipeline(
        experiment_id=experiment.id,
        job_name=JOB_NAME,
        pipeline_id=pipeline.id,
        params={
            "learning_rate": 0.1,
            "num_layers": 2,
            "optimizer": 'ftrl'
        },
    )

    # Wait for the run to complete
    run_resp = client.wait_for_run_completion(pipeline_run.id, timeout=300)
    print(run_resp)
