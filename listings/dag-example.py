(
  [
    ail(),
    reset_for_shodan() >> shodan(),
    reset_for_hibp() >> hibp(),
    misc(),
  ]
  >> set_score_calculation_flag()
  >> bump_priority_task(100)
)
