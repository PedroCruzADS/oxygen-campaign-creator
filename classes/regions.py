class Region:
    def __init__(self) -> None:

        self.sudeste = [
            {"key": "454"},
            {"key": "460"},
            {"key": "449"}]

        self.sul = [{"key": "456"},
                    {"key": "452"},
                    {"key": "459"}]

        self.norte = [{"key": "458"},
                      {"key": "457"},
                      {"key": "441"},
                      {"key": "440"},
                      {"key": "464"}]

        self.nordeste = [{"key": "451"},
                         {"key": "461"},
                         {"key": "439"},
                         {"key": "447"},
                         {"key": "443"},
                         {"key": "442"},
                         {"key": "455"}]

        self.centro_oeste = [{"key": "444"},
                             {"key": "462"},
                             {"key": "446"},
                             {"key": "448"}]

        self.region_keys = {"sul": self.sul,
                            "sudeste": self.sudeste,
                            "norte": self.norte,
                            "centro_oeste": self.centro_oeste,
                            "nordeste": self.nordeste}
