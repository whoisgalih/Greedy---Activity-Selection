class Activity:
    name: str
    start: int
    end: int

    def __init__(self, name: str, start: int, end: int):
        self.name = name
        self.start = start
        self.end = end

    def __repr__(self):
        return f"{self.name}: {self.start} - {self.end}"
