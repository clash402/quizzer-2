import requests as req


class DataManager:

    # PUBLIC METHODS
    def get_trivia(self, question_count):
        endpoint = "https://opentdb.com/api.php"
        params = {"amount": question_count, "type": "boolean"}

        res = req.get(endpoint, params=params)
        res.raise_for_status()

        return res.json()["results"]
