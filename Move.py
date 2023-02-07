class Move:
    def __init__(self, name, movetype, spephysup, accuracy, damage, pp, statsaffected=None, accuracystatsaffected=100, affectopponent=[], pivot=False):
        self._name = name 
        self._movetype = movetype #fire, water, etc
        self._spephysup = spephysup #special, physical, support
        self._accuracy = accuracy # 1-100
        self._damage = damage # 1-200
        self._pp = pp #PP Power Points, 5-50
        self._pivot = pivot # boolean, will make the poke return to trainer