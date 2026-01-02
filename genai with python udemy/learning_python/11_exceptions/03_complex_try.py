def serve_chai(flavour):
    flavour_copy = flavour
    chai_menu = ["masala", "ginger", "elaichi"]
    if flavour not in chai_menu:
        flavour = "unknown"
    try:
        if flavour == "unknown":
            raise ValueError(f"we don't have {flavour_copy} flavour")
    except ValueError as e:
        print("Error:", e)
    else:
        print(f"Preparing {flavour} chai ....")
        print(f"{flavour} chai is served")
    finally:
        print("Next Customer Please")


serve_chai("masala")
serve_chai("motacha")