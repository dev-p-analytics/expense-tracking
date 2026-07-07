import os
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("Project Root: ", ROOT_DIR)
sys.path.insert(0, ROOT_DIR)
print(sys.path)