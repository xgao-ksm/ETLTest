resources:
  jobs:
    dev_jenny_run_notebook:
      name: "[dev jenny] run-notebook"
      max_concurrent_runs: 4
      tasks:
        - task_key: my-notebook-task
          notebook_task:
            notebook_path: /Workspace/Users/jenny@xgao198902gmail.onmicrosoft.com/ETLTest/bundle1/helloworld
            source: WORKSPACE
      tags:
        dev: jenny
      queue:
        enabled: true
      run_as:
        user_name: jenny@xgao198902gmail.onmicrosoft.com