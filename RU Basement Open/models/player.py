
class Player:
    def __init__(self, playerid, name, mobile, home_phone, email, address):
        self.playerid = playerid
        self.name = name
        self.mobile = mobile
        self.home_phone = home_phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.name}"

    def listify(self):
        return [self.playerid, self.name, self.mobile, self.home_phone, self.email, self.address]

    def model(self):
        return "players"
