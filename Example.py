{
  "paragraphs": [
    {
      "text": "# -*- coding: utf-8 -*-\n#\n# Licensed under the Apache License, Version 2.0 (the \"License\");\n# you may not use this file except in compliance with the License.\n# You may obtain a copy of the License at\n#\n# http://www.apache.org/licenses/LICENSE-2.0\n#\n# Unless required by applicable law or agreed to in writing, software\n# distributed under the License is distributed on an \"AS IS\" BASIS,\n# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n# See the License for the specific language governing permissions and\n# limitations under the License.\n\n\"\"\"\n### Tutorial Documentation\nDocumentation that goes along with the Airflow tutorial located\n[here](http://pythonhosted.org/airflow/tutorial.html)\n\"\"\"\nimport airflow\nfrom airflow import DAG\nfrom airflow.operators.bash_operator import BashOperator\nfrom datetime import timedelta\n\n\n# these args will get passed on to each operator\n# you can override them on a per-task basis during operator initialization\ndefault_args \u003d {\n    \u0027owner\u0027: \u0027airflow\u0027,\n    \u0027depends_on_past\u0027: False,\n    \u0027start_date\u0027: airflow.utils.dates.days_ago(2),\n    \u0027email\u0027: [\u0027airflow@airflow.com\u0027],\n    \u0027email_on_failure\u0027: False,\n    \u0027email_on_retry\u0027: False,\n    \u0027retries\u0027: 1,\n    \u0027retry_delay\u0027: timedelta(minutes\u003d5),\n    # \u0027queue\u0027: \u0027bash_queue\u0027,\n    # \u0027pool\u0027: \u0027backfill\u0027,\n    # \u0027priority_weight\u0027: 10,\n    # \u0027end_date\u0027: datetime(2016, 1, 1),\n    # \u0027wait_for_downstream\u0027: False,\n    # \u0027dag\u0027: dag,\n    # \u0027adhoc\u0027:False,\n    # \u0027sla\u0027: timedelta(hours\u003d2),\n    # \u0027execution_timeout\u0027: timedelta(seconds\u003d300),\n    # \u0027on_failure_callback\u0027: some_function,\n    # \u0027on_success_callback\u0027: some_other_function,\n    # \u0027on_retry_callback\u0027: another_function,\n    # \u0027trigger_rule\u0027: u\u0027all_success\u0027\n}\n\ndag \u003d DAG(\n    \u0027tutorial\u0027,\n    default_args\u003ddefault_args,\n    description\u003d\u0027A simple tutorial DAG\u0027,\n    schedule_interval\u003dtimedelta(days\u003d1))\n\n# t1, t2 and t3 are examples of tasks created by instantiating operators\nt1 \u003d BashOperator(\n    task_id\u003d\u0027print_date\u0027,\n    bash_command\u003d\u0027date\u0027,\n    dag\u003ddag)\n\nt1.doc_md \u003d \"\"\"\\\n#### Task Documentation\nYou can document your task using the attributes `doc_md` (markdown),\n`doc` (plain text), `doc_rst`, `doc_json`, `doc_yaml` which gets\nrendered in the UI\u0027s Task Instance Details page.\n![img](http://montcs.bloomu.edu/~bobmon/Semesters/2012-01/491/import%20soul.png)\n\"\"\"\n\ndag.doc_md \u003d __doc__\n\nt2 \u003d BashOperator(\n    task_id\u003d\u0027sleep\u0027,\n    depends_on_past\u003dFalse,\n    bash_command\u003d\u0027sleep 5\u0027,\n    dag\u003ddag)\n\ntemplated_command \u003d \"\"\"\n{% for i in range(5) %}\n    echo \"{{ ds }}\"\n    echo \"{{ macros.ds_add(ds, 7)}}\"\n    echo \"{{ params.my_param }}\"\n{% endfor %}\n\"\"\"\n\nt3 \u003d BashOperator(\n    task_id\u003d\u0027templated\u0027,\n    depends_on_past\u003dFalse,\n    bash_command\u003dtemplated_command,\n    params\u003d{\u0027my_param\u0027: \u0027Parameter I passed in\u0027},\n    dag\u003ddag)\n\nt2.set_upstream(t1)\nt3.set_upstream(t1)\n\n",
      "user": "ptoole@qubole.com",
      "dateUpdated": "Aug 22, 2018 2:20:29 AM",
      "config": {
        "colWidth": 12.0,
        "graph": {
          "mode": "table",
          "height": 300.0,
          "optionOpen": false,
          "keys": [],
          "values": [],
          "groups": [],
          "scatter": {}
        },
        "enabled": true,
        "editorMode": "ace/mode/scala"
      },
      "settings": {
        "params": {},
        "forms": {}
      },
      "paragraphProgress": {
        "jobs": [],
        "numCompletedTasks": 0,
        "numTasks": 0,
        "truncated": false
      },
      "version": "v0",
      "jobName": "paragraph_1534894073199_-1706752487",
      "id": "20180821-232753_1144993508_q_PWB91R1ET31534893758",
      "result": {
        "code": "SUCCESS",
        "type": "TEXT",
        "msg": "This line will be printed."
      },
      "dateCreated": "Aug 21, 2018 11:27:53 PM",
      "dateSubmitted": "Aug 22, 2018 2:16:15 AM",
      "dateStarted": "Aug 22, 2018 2:16:17 AM",
      "dateFinished": "Aug 22, 2018 2:17:05 AM",
      "status": "FINISHED",
      "progressUpdateIntervalMs": 1000
    },
    {
      "text": "",
      "config": {},
      "settings": {
        "params": {},
        "forms": {}
      },
      "version": "v0",
      "jobName": "paragraph_1534895399224_-1314404964",
      "id": "20180821-234959_1380342676_q_PWB91R1ET31534893758",
      "dateCreated": "Aug 21, 2018 11:49:59 PM",
      "status": "READY",
      "progressUpdateIntervalMs": 1000
    }
  ],
  "name": "Example.py",
  "id": "PWB91R1ET31534893758",
  "angularObjects": {
    "2D6S4V6R633551517332493711:shared_process": [],
    "2D4NVQY3Z33551517332493696:shared_process": [],
    "2D5MTWVG233551517332493673:shared_process": [],
    "2D6UDAR6A33551517332493703:shared_process": []
  },
  "config": {
    "isDashboard": false,
    "defaultLang": ""
  },
  "info": {},
  "source": "FCN"
}