def add_time(*args):
  hrs = to_24(args[0])[0]
  mins = to_24(args[0])[1]

  hrs_to_add = int((mins + int(args[1].split(" ")[0].split(":")[1])) / 60)
  minutes = (mins + int(args[1].split(" ")[0].split(":")[1])) % 60

  days_to_add = int((hrs + hrs_to_add + int(args[1].split(" ")[0].split(":")[0])) / 24)
  hours = (hrs + hrs_to_add + int(args[1].split(" ")[0].split(":")[0])) % 24

  if minutes < 10:
    minutes_str = "0" + str(minutes)
  else:
    minutes_str = str(minutes)

  time24 = str(hours) + ":" + minutes_str

  time = to_am_pm(time24)

  days = ["monday", "tuesday", "wednesday", 
          "thursday", "friday", "saturday", "sunday"]

  if len(args) == 3:
    initial_day = (args[2]).lower()
    initial_day_index = days.index(initial_day)
    final_day_index = (initial_day_index + days_to_add) % 7
    final_day = ", " + days[final_day_index].title()
  else:
    final_day = ""

  if days_to_add == 1:
    time = time + final_day + " (next day)"
  elif days_to_add > 1:
    time = time + final_day + " (" + str(days_to_add) + " days later)"
  else:
    time = time + final_day

  return time


def to_24(time):
  am_pm = time.split(" ")[1]
  minutes = int(time.split(" ")[0].split(":")[1])
  if am_pm == "AM":
    hours = int(time.split(" ")[0].split(":")[0]) % 12
  else:
    hours = (int(time.split(" ")[0].split(":")[0]) % 12) + 12
  # print(str(hours) + ":" + str(minutes))
  return [hours, minutes]


def to_am_pm(time):
  hours = int(time.split(":")[0])
  minutes = time.split(":")[1]

  if hours < 12 or hours == 24:
    am_pm = " AM"
    if hours == 24:
      hrs = "12"
    elif hours == 0:
      hrs = "12"
    else:
      hrs = str(hours)
  else:
    am_pm = " PM"
    if hours == 12:
      hrs = "12"
    else:
      hrs = str(hours - 12)

  return hrs + ":" + minutes + am_pm