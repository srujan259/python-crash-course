poll_active = True
gym_details = {}
while poll_active:
    name = input('whats your name:')
    workout = input('whats your workout')
    gym_details[name]=workout

    repeat = input("Do you have another partner with you (yes/no):")
    if(repeat=='no'):
        poll_active = False

print(gym_details)
for name, workout in gym_details.items():
    print(f"{name} is working on {workout} today")