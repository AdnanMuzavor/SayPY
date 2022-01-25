"""An event consist of users logged in into different machines on some dates and thn logout, display list of users based on data of events who are currently logged into machine,avoid displaying machines where users are not logged in or have 0 users"""

# for passin g to sort function to sort as per dates


def get_event_date(event):
    return event.date

# for preparin dict of machines and logged in users corresponding


def current_users(events):
    events.sort(key=get_event_date)
    machines = {}
    for event in events:
        # If event not in dict,initialise it
        if event.machine not in machines:
            machines[event.machine] = set()
            # if user is logged in add it into set corresponding to machne where he has logged in
        if event.type == "login":
            # rmove user logged out but first ensure if he was in logged in
            machines[event.machine].add(event.user)
        elif event.type == "logout" and event.user in machines[event.machine]:
            machines[event.machine].remove(event.user)
    return machines


def generate_report(machines):
    for machine, users in machines.items():
        # If set is empty i.e no user logged in in the machine, dont't display
        if len(users) > 0:
            user_list = ", ".join(users)
            print("{}: {}".format(machine, user_list))

# Defining event class as each will have multiple attributes


class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user


# Making the list of objects where each object is an event
events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),
]

# Making a dictionary
users = current_users(events)
print(users)

# Getting report printed
generate_report(users)
