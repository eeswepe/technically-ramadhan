def make_readable(seconds):
    hrs = seconds // 3600
    mnts = (seconds % 3600) // 60
    scnds = (seconds % 3600) % 60

    return f"{hrs:02d}:{mnts:02d}:{scnds:02d}"
