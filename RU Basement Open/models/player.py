
class Player:
    def __init__(self, playerid, name, mobile, home_phone, email, address, team_id, is_captain):
        self.playerid = playerid
        self.name = name
        self.mobile = mobile
        self.home_phone = home_phone
        self.email = email
        self.address = address
        self.team_id = team_id
        self.is_captain = is_captain


    def listify(self):
        return [self.playerid, self.name, self.mobile, self.home_phone, self.email, self.address, self.team_id, self.is_captain]

    def model(self):
        return "players"
