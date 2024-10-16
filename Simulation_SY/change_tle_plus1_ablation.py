import sys

def pick_ith_satellite(source_file, target_file, i):
    with open(source_file, 'r') as file:
        lines = file.readlines()

    satellites = [lines[i:i+3] for i in range(0, len(lines), 3)]

    # Select the ith satellite
    selected_satellite = satellites[i]

    print("Selected satellite data:")
    for line in selected_satellite:
        print(line.strip())

    with open(target_file, 'a') as file:
        file.writelines(selected_satellite)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <source_file> <target_file> <index>")
    else:
        source_file = sys.argv[1]
        target_file = sys.argv[2]
        index = int(sys.argv[3])
        pick_ith_satellite(source_file, target_file, index)
