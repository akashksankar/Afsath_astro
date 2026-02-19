
data = [
    {'username': 'ashik', 'password': '1234', 'mark': 272},
    {'username': 'adhina', 'password': '2311', 'mark': 256},
    {'username': 'reshma', 'password': '5111', 'mark': 261}
]

# user input
u = input("Enter username: ")
p = input("Enter password: ")

found = False

for user in data:
    if user['username'] == u and user['password'] == p:
        print("✅ Login successful")
        print("Your mark is:", user['mark'])
        found = True
        break

if not found:
    print("❌ Invalid username or password")
