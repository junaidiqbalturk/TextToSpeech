class Joke:

    def __init__(self,setup, punchline) -> None:
        self.setup = setup
        self.punchline = punchline

    def __str__(self) -> str:
        return f"setup: {self.setup} punchline: {self.punchline}"