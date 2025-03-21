from spravce_pojistniku import SpravcePojistniku
from aplikace import Aplikace

if __name__ == "__main__":
    spravce = SpravcePojistniku()
    app = Aplikace(spravce)
    app.spustit_aplikaci()