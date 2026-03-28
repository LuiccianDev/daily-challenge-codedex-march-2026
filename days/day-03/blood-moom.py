def blood_moon(time):
  # Write code below 💖

  #convert inputs to taotal minutes
  hours , minutes = map(int, time.split(':'))
  total_minutes = hours * 60 + minutes

  num_veces = 3
  #  Blood Moon occurs every 2 hours and 48 minutes. 
  interval = 2 * 60 + 48  # 168 min
  results =[]
  for _ in range(num_veces):
    total_minutes = (total_minutes + interval) % (24 * 60)
    new_hours = total_minutes // 60
    new_minutes = total_minutes % 60
    results.append(f"{new_hours:02d}:{new_minutes:02d}")

  return results