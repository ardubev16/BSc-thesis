@satayo_task(tool_code="dnsrecon")
def dnsrecon(
  tool_code: str,
  output_path: str,
  id_research: int,
  id_domain: int,
  target_domain: str,
  id_tool_progress: int,
) -> None:
  logger.info("Start of DNSRecon")
  # Run DNSRecon
  ...
