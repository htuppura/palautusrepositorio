from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        p = toml.loads(
                request.urlopen(self._url).read().decode("utf-8")
                        )["tool"]["poetry"]

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta
        # Project-olio sen tietojen perusteella
        return Project(p["name"], p["description"], p["license"],
                p["authors"], p["dependencies"], 
                p["group"]["dev"]["dependencies"])
