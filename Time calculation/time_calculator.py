def add_time(start, duration, day_week= False):
  
  arr_day_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  index_day_of_week = {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3, "friday": 4, "saturday": 5, "sunday": 6}
  
  duration_tup = duration.split(":")
  duration_hours = int(duration_tup[0])
  duration_minutes = int(duration_tup[1])

  start_tup = start.split(":")
  start_minutes_tup = start_tup[1].split(" ")
  start_hours = int(start_tup[0])
  start_minutes = int(start_minutes_tup[0])
  timeam_pm = start_minutes_tup[1]
  check_am_pm = {"AM": "PM", "PM": "AM"}

  number_days = int(duration_hours / 24)

  final_minutes = start_minutes + duration_minutes
  
  if (final_minutes >= 60):
    start_hours += 1
    final_minutes = final_minutes % 60

  final_check_am_pm = int((start_hours + duration_hours) /12)
  final_hours = (start_hours + duration_hours) % 12

  final_minutes = final_minutes if final_minutes > 9 else "0" + str(final_minutes)
  final_hours = final_hours = 12 if final_hours == 0 else final_hours

  if (timeam_pm == "PM" and start_hours+(duration_hours % 12) >= 12):
    number_days += 1

  timeam_pm = check_am_pm[timeam_pm] if final_check_am_pm %2 == 1 else timeam_pm

  new_time = str(final_hours) + ":" + str(final_minutes) + " " + timeam_pm

  if (day_week):
    day_week = day_week.lower()
    i = int((index_day_of_week[day_week]) + number_days) % 7
    new_day = arr_day_of_week[i]
    new_time += ", " + new_day

  if (number_days == 1):
    return new_time + " " + "(next day)"
  elif (number_days > 1):
    return new_time + " (" + str(number_days) + " days later)"
    
  return new_time