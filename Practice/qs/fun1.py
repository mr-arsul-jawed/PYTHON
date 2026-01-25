names = [
    'John', 'Emma', 'Michael', 'Sophia', 'James', 'Isabella', 'William', 'Mia', 
    'Ethan', 'Charlotte', 'Alexander', 'Amelia', 'Daniel', 'Harper', 'Matthew', 
    'Evelyn', 'Joseph', 'Abigail', 'Benjamin', 'Emily', 'David', 'Ella', 'Logan', 
    'Avery', 'Lucas', 'Scarlett', 'Henry', 'Grace', 'Jackson', 'Chloe', 'Sebastian', 
    'Lily', 'Jack', 'Aria', 'Aiden', 'Madison', 'Owen', 'Layla', 'Elijah', 'Luna', 
    'Gabriel', 'Zoe', 'Caleb', 'Riley', 'Isaac', 'Victoria', 'Ryan', 'Penelope', 
    'Nathan', 'Aubrey', 'Aaron', 'Hannah', 'Andrew', 'Mila', 'Samuel', 'Nora', 
    'Joshua', 'Ellie', 'Carter', 'Addison', 'Christopher', 'Brooklyn', 'Luke', 
    'Savannah', 'Dylan', 'Bella', 'Anthony', 'Stella', 'Isaiah', 'Skylar', 'Oliver', 
    'Paisley', 'Wyatt', 'Genesis', 'Julian', 'Claire', 'Eli', 'Ariana', 'Hunter', 
    'Violet', 'Landon', 'Aaliyah', 'Christian', 'Hazel', 'Levi', 'Aurora', 'Jonathan', 
    'Lucy', 'Charles', 'Caroline', 'Connor', 'Sarah', 'Thomas', 'Alice', 'Jeremiah', 
    'Kennedy', 'Jordan', 'Sadie', 'Nicholas', 'Maya', 'Evan', 'Lillian', 'Adrian', 
    'Peyton'
]


def find_name(rank):
    for val in range(len(names)):
        if val == rank:
            print("Find the name index:",val,"and name:",names[val])
            break
       

find_name(3)