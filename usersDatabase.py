'''
    As a senior backend engineer at Amazon, you are tasked with developing a fast in-memory data structure to manage profile information (username, name and email) for 100 million users. It should allow the following operations to be performed efficiently:
        1.  INSERT the profile information for a new user
        2.  FIND the profile info of user given their username
        3.  UPDATE the profile info of user given their username
        4.  LIST all the users of the platform sorted by username

    We can assume usernames are unique.

    INSERT test cases
        a.  inserting into empty database
        b.  inserting a user when username already exists
        c.  inserting a user with username that does not exist

    
    SOLUTION
        INSERT  Loop through list and add new user at position that keeps list sorted
        FIND    Loop through list and find user that matches query
        UPDATE  Loop through list and find user that matches query and update details
        LIST    return the list of objects

'''

class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
        #print('User created!')

    def __repr__(self):
        return "User(username='{}', name='{}', email='{}')".format(self.username, self.name, self.email)

    def __str__(self):
        return self.__repr__()

    def introduce_yourself(self, guestname):
        print("Hi {}, I'm {}! Contact me at {} ".format(guestname, self.name, self.email))

user = User('john', 'John Doe', 'john@email.com')
#user.introduce_yourself('David')
#User.introduce_yourself(user, 'David')

#   example inputs
abu = User('abu', 'Abu Sam', 'abu@email.com')
ben = User('ben', 'Ben Davies', 'ben@example.com')
henry = User('henry', 'Henry Jacobs', 'henry@email.com')
jason = User('jay', 'Jason Philips', 'jason@email.com')
sid = User('sid', 'Sidney Potier', 'sid@email.com')
sonny = User('sonny', 'Sonny James', 'sonny@email.com')
valerie = User('val', 'Valerie Thomas', 'val@email.com')

users = [abu, ben, henry, jason, sid, sonny, valerie]
#print(abu)

class UserDatabase:
    def __init__(self):
        self.users = []

    def insert(self, user):
        i = 0
        while i < len(self.users):
            #   find first username greater than new user's username
            if self.users[i].username > user.username:
                break
            i = i + 1
        self.users.insert(i, user)

    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user

    def update(self, user):
        target = self.find(user.username)
        target.name = user.name
        target.email = user.email

    def list_all(self):
        return self.users


database = UserDatabase()
database.insert(henry)
database.insert(abu)
database.insert(sonny)
#print(database.list_all())
print(database.find('sonny'))

database.insert(ben)
print(database.list_all())