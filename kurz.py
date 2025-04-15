class Kurz:
    """Třída pro reprezentaci plaveckého kurzu."""
    def __init__(self, nazev, kapacita, instruktor):
        self.nazev = nazev
        self.kapacita = kapacita
        self.instruktor = instruktor
        self.ucastnici = []  # seznam instancí Ucastnik

    def registrovat(self, ucastnik):
        if len(self.ucastnici) < self.kapacita:
            self.ucastnici.append(ucastnik)
            return f"{ucastnik.jmeno} byl(a) přidán(a) do kurzu {self.nazev}."
        else:
            return f"Nelze přidat: Kurz {self.nazev} je plný."

    def zobraz_info(self):
        return (f"Kurz: {self.nazev}, instruktor: {self.instruktor}, "
                f"kapacita: {len(self.ucastnici)}/{self.kapacita}")



