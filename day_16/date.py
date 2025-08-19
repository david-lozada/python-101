from datetime import datetime

now = datetime.now()
# day = now.day
# month = now.month
# year = now.year
# hour = now.hour
# minutes = now.minute
# ordered_date = now.strftime("%d/%m/%Y, %H:%M:%p")
# detailed_date = now.strftime("Today is %d %B, %Y")

def time_remain(start, end):            
    time_diff = end - start
    
    # Extract days, hours, minutes, and seconds
    days = time_diff.days
    hours, remainder = divmod(time_diff.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    return days, hours, minutes, seconds

# Get the time difference
start = now
end = datetime(now.year + 1, 1, 1)
days, hours, minutes, seconds = time_remain(start, end)

print(f"Time difference: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")

# print(detailed_date)