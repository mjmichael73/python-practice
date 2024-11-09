# *** in Version 3.10: ***
with (open("file.out", "rb") as rf, open("file_copy.out", "wb") as wf):
    pass

# *** Before: ***
with open("file.out", "rb") as rf:
    with open("file_copy", "wb") as wf:
        pass