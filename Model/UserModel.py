class User():

    _id = 0

    def __init__(self):
        User._id = User._id + 1
        self.id = User._id
        self.name = ''
        self.email = ''
        self.password = ''



