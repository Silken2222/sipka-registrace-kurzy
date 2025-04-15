class Ucastnik:
    """Základní třída pro účastníka kurzu."""
    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek

    def zobraz_info(self):
        return f"{self.jmeno}, {self.vek} let"


class DiteUcastnik(Ucastnik):
    """Třída pro dítě přihlášené rodičem."""
    def __init__(self, jmeno, vek, jmeno_rodice, telefon, email):
        super().__init__(jmeno, vek)
        self.jmeno_rodice = jmeno_rodice
        self.telefon = telefon
        self.email = email

    def zobraz_info(self):
        return (f"Dítě: {self.jmeno}, {self.vek} let\n"
                f"Rodič: {self.jmeno_rodice}, Tel: {self.telefon}, Email: {self.email}")


class DospelyUcastnik(Ucastnik):
    """Třída pro dospělého účastníka (plavání nebo aqua aerobik)."""
    def __init__(self, jmeno, vek, telefon, email, typ_kurzu):
        super().__init__(jmeno, vek)
        self.telefon = telefon
        self.email = email
        self.typ_kurzu = typ_kurzu

    def zobraz_info(self):
        return (f"{self.typ_kurzu.title()}: {self.jmeno}, {self.vek} let, "
                f"Tel: {self.telefon}, Email: {self.email}")
