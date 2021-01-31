import requests as req


class DataManager:
    def __init__(self, question_count):
        self.ENDPOINT = "https://opentdb.com/api.php"
        self.params = {"amount": question_count, "type": "boolean"}

    # PUBLIC METHODS
    def get_trivia(self):
        res = req.get(self.ENDPOINT, params=self.params)
        res.raise_for_status()

        return res.json()["results"]
