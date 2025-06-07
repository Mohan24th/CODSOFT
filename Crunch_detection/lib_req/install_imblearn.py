# Run this script to install the imbalanced-learn package
import sys
import subprocess

def install_package():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "imbalanced-learn"])
        print("imbalanced-learn package installed successfully.")
    except subprocess.CalledProcessError as e:
        print("Failed to install imbalanced-learn package.")
        print(e)

if __name__ == "__main__":
    install_package()
