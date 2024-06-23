def pre_task(self, context: Context) -> None:
  if "output_path" in self.arg_list:
    self.tmp_dir = tempfile.mkdtemp(self.tool_code)

  AIRFLOW_HOST = "satayo-airflow01"
  host_id = fun.select_one(q.select_host, AIRFLOW_HOST)

  self.id_tool_progress = fun.ins_up(
    q.insert_tool_progress,
    context["params"]["id_research"],
    context["dag"].dag_id,
    context["dag_run"].run_id,
    context["task"].task_id,
    host_id,
    self.tool_code,
  )
  fun.ins_up(q.update_time_start, int(time()), self.id_tool_progress)


def post_task(self) -> None:
  if self.tmp_dir:
    shutil.rmtree(self.tmp_dir)
  fun.ins_up(q.update_tool_progress_success, self.id_tool_progress)
  fun.ins_up(q.update_time_stop, int(time()), self.id_tool_progress)
