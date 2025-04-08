# datetime.strptime

# dt = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")

# # Set minutes and seconds to 0
# rounded = dt.replace(minute=0, second=0, microsecond=0)
from datetime import datetime

def hourly_uniqueusers(events):
    a = {}

    for user,ts in events:
        dt = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
        dt_rounded = dt.replace(minute=0, second=0, microsecond=0)

        if dt_rounded not in a:
            a[dt_rounded] = set()
        
        a[dt_rounded].add(user)

    result = {}

    for hour, users in a.items():
        result[hour.strftime("%Y-%m-%d %H:%M:%S")] = len(users)
    
    return result

# test cases

if __name__ == "__main__":
    events = [
        ("u1", "2023-07-01 09:15:00"),
        ("u2", "2023-07-01 09:45:00"),
        ("u1", "2023-07-01 10:00:00"),
        ("u3", "2023-07-01 10:10:00"),
        ("u1", "2023-07-01 10:59:59"),
        ("u4", "2023-07-01 11:00:00")
    ]

    print(hourly_uniqueusers(events))

