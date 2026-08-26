from datetime import datetime
from importlib.metadata import PackageNotFoundError, version
 
packages = ["numpy", "pandas", "scikit-learn", "matplotlib"]
 
print("Uitgevoerd op:", datetime.now().isoformat(timespec="seconds"))
for package in packages:
    try:
        print(f"{package}: {version(package)}")
    except PackageNotFoundError:
        print(f"{package}: niet geïnstalleerd")
