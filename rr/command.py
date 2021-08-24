from .measure import RR

def main():
    rr = RR()
    while True:
        input("Press when you exhale...")
        rr.breath()
        print(rr)