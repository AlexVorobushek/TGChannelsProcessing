class Channel:
    def __init__(self, username:str, title:str, members_count:int):
        self.username = username
        self.title = title
        self.members_count = members_count

    def __str__(self):
        return f"(name: @{self.username}\ttitle: {self.title}\tmembers count: {self.members_count})"