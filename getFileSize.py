import os

#This is used directly from https://stackoverflow.com/questions/1392413/calculating-a-directorys-size-using-python
#START to used code (not Mine)
def get_size(start_path = '.', useMB = False):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                if useMB:
                    total_size += os.path.getsize(fp)/1000000.0
                else:
                    total_size += os.path.getsize(fp)
    return total_size
#END to used code
