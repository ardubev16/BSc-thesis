def crontabs_from_domain(domain: str):
  DAILY_HOUR = 3
  WEEKLY_HOUR = 3
  random.seed(domain)

  # Choose a random day of the week
  weekly_day = random.randint(0, 6)

  # Choose two random days in a month offset by 14 days
  monthly_day = random.randint(1, 14)
  monthly_day2 = monthly_day + 14

  return {
    "daily": f"0 {DAILY_HOUR} * * *",
    "weekly": f"0 {WEEKLY_HOUR} * * {weekly_day}",
    "biweekly": f"0 {DAILY_HOUR} {monthly_day},{monthly_day2} * *",
  }
