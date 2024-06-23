def execute(
  id_research,
  id_domain,
  target_domain,
  size_domain,
  python_id_host,
  output_path,
  parser_tool,
):
  tool_code = "dnsrecon"
  id_tool_progress = fun.select_one(
    q.count_tool, None, id_research, python_id_host, tool_code
  )
  # Check if DNSRecon is scheduled to run for this domain.
  if id_tool_progress:
    time_start = int(time.time())
    fun.ins_up(
      q.insert_log, id_tool_progress, time_start, "Start of DNSRecon", 1, id_tool_progress
    )
    dnsrecon_path = parser_tool.get("config", "dnsrecon_path")
    # Check if DNSRecon path is correctly written in conf/path_tools.txt
    if fun.check_program_installation(dnsrecon_path, id_tool_progress):
      # Run DNSRecon
      ...
