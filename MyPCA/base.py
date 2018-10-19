import pandas as pd
import sys
from abc import abstractmethod

class Base:
    def __init__(self, intensity_file, meta_file):
        self.intensity_file = intensity_file
        self.meta_file = meta_file

        if ".csv" not in self.intensity_file or ".csv" not in self.meta_file:
            print("Please enter valid file format")
        else:
            try:
                self.mdf = pd.read_csv(self.meta_file, low_memory=False)
                self.gdf = pd.read_csv(self.intensity_file, low_memory=False)
            except Exception as e:
                print(e)
                sys.exit()

    @abstractmethod
    def fit():
        """Placeholder for fit. Subclasses should implement this method!"""
