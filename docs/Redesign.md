# Echodataflow Redesign

## Control Flow 

1. In the new design, Echodataflow will require only two configuration YAML files: one for the data source and an optional one for logging.

2. Refer to a sample deployment YAML for [reference](../echodataflow/deployment/deployment_demo.yaml).

3. The deployment and logging YAML files are passed to the `deploy_echodataflow` function in the `echodataflow.deployment.deployment_engine` module.

4. The `deploy_echodataflow` parses the YAML files to create a `Deployment` object.

5. The `Deployment` object contains a list of `Service` objects, each representing a single service in the deployment.

6. The `deploy_echodataflow` function then calls `_deploy_service` function for each `Service` in the `Deployment` object.

7. The `_deploy_service` takes a `Service` object and a logging dictionary as input, deploying the service using the `Service.deploy` method.

8. The `_deploy_service` also handles workpool and workqueue creation.

9. Once all services are deployed, `deploy_echodataflow` returns the `Deployment` object and lists all successfully deployed services.

10. Worker nodes are spun up to point to the appropriate workpool and workqueue for task processing.

11. Worker nodes start processing tasks from the workqueue according to the configured schedule or manual triggers.

12. Each run triggers the `edf_service` function from the `echodataflow.deployment.service` module.

13. The `edf_service` takes a `Service` object, a logging dictionary, and Dask cluster information as input, executing the service by running stages sequentially.

14. The `edf_service` handles cluster creation and teardown required for any or all stages.

15. It dynamically extracts the function and module name from the `stage` attribute of the `Service` to execute each stage.

16. The stage function defaults to `Sv_flow` from the `echodataflow.deployment.flow` module.

17. For each stage, the data source is extracted:

    a. The extract_source function from the `echodataflow.deployment.source` module calls the `glob_all_files` utility function to gather all files from the source path, returning a list of file paths.

    b. The list of file paths is grouped using the `parse_raw_paths` function based on grouping information provided in the group attribute of the Service.

    c. `parse_raw_paths` returns a dictionary where keys are group names and values are lists of file paths.

    d. The `club_raw_files` function processes this dictionary, returning another dictionary where keys are group names and values are dictionaries containing files and their related information.

18. Each group and file are iterated through, and a series of tasks defined in the tasks attribute of the `Service.Stages` object are executed for each file.

19. After all tasks are executed for a file, the output is stored at the destination path specified in the `Service.destination` object.