'''
@Author: Senkita
'''

from interface import Interface
from processing import Processing
import sys

def main():
    try:
        ui = Interface()

        file_path, config_file = ui.file_selector()
        p = Processing(file_path, config_file)
        result = p.analysis()
        name = p.output(result)
        
        ui.finish(name)
    except:
        sys.exit(0)

if __name__ == "__main__":
    main()