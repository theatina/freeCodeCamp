def add_time(start, duration, day=-1):
  days_dict=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  new_time=-9
  # if days_later: 0 -> '', 1 -> 'next day', n(n>1) -> 'n days later' 
  days_later=0
  time,am_pm=start.split(" ")
  time,am_pm=time.strip(), am_pm.strip()
  # print(f"{time}\n{am_pm}")
  
  start_h,start_mins=time.split(":")
  start_h=int(start_h)
  if am_pm=="PM":
    start_h=start_h+12
  start_mins=int(start_mins)
  
  dur_h,dur_mins=duration.split(":")
  dur_h=int(dur_h)
  dur_mins=int(dur_mins)
  if dur_h+dur_mins==0:
    return start
    
  if dur_h==0:
    fin_hour=start_h+int((start_mins+dur_mins)/60)%24
  else:
    fin_hour= (start_h+dur_h+int((start_mins+dur_mins)/60))%24

  if dur_mins==0:
    fin_mins=start_mins
  else:
    fin_mins= int((start_mins+dur_mins)%60)

  days_later = int((start_h+dur_h+int((start_mins+dur_mins)/60))/24)

  if fin_hour<12:
    am_pm="AM"
  else:
    fin_hour-=12
    am_pm="PM"
    
  if fin_hour==0:
    fin_hour=12
  
  new_time=f"{fin_hour}:{str(fin_mins).zfill(2)} {am_pm}"
  
  if day!=-1:
    day=day.capitalize()
    days_after_pos=days_later%7    
    fin_pos=(days_dict.index(day)+days_after_pos)
    if fin_pos>len(days_dict)-1:
      fin_pos=7-fin_pos

    new_time+=f", {days_dict[fin_pos]}"
  
  days_later_msg=""
  if days_later==1:
    days_later_msg=" (next day)"
  elif days_later>1:
    days_later_msg=f" ({days_later} days later)"
    
  new_time+=f"{days_later_msg}"
  
  return new_time


# new_time=add_time("11:59 PM", "24:05", "Wednesday")
# print(new_time)
