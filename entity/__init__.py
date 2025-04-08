class Account:
    def __init__(self, id, fullName, username, password):
        self.id = id
        self.fullName = fullName
        self.username = username
        self.password = password
        
    def __str__(self):
        return f"{self.id} - {self.fullName} = {self.username}"