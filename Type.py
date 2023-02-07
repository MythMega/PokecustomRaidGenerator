class Type:
    def __init__(self, name):
        self._name = name
        self._immune = []
        self._resists = []
        self._powerfull = []
    

    def add_immunities(self, newImmuneType):
        self._immune.append(newImmuneType)    

    def add_resist(self, newResistedType):
        self._resists.append(newResistedType)

    def add_powerfull(self, newPowerfullType):
        self._powerfull.append(newPowerfullType)