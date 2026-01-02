def brew_chai(flavour):
    if flavour not in ["masala", "ginger", "elaichi"]:
        raise ValueError(f"{flavour} flavour not available....")
    print(f"brewing {flavour} chai....")


brew_chai("mint")