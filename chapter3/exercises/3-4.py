invitees = ['ancy', 'kiara', 'sujay']
def invite():
    for person in invitees:
        #invite(person.title())
        print(f" Hi {person}, I would like to cordially invite you to dinner")


invite()
# sujay cant make it
guest_cant_make_it = 'sujay'
alt_guest = 'joe'
print(f'{guest_cant_make_it} cant make it for dinner so replace him with joe')
invitees.remove(guest_cant_make_it)
invitees.append(alt_guest)
invite()
print('----------------------------')
print('I have found a bigger table')
invitees.insert(0, 'shobha')
invitees.insert(2, 'sudhakar')
invitees.append('sujay')
print(invitees)
invite()

print('-----OOPS New Table wont arrive in time')
loop_until = len(invitees) - 2
for person in range(loop_until):
    removed_guests = invitees.pop()
    print(f'Hey {removed_guests}, sorry for the last min cancellation')

print(invitees)

print('deleting all')

for i in range(len(invitees)):
    del invitees[0]

print(f"final list null {invitees}")