import subprocess

def run_commands():
    command1 = "python3 create_config.py starlink_ablation_2.tle gs.txt '2024-04-09 12:00:00' '2024-04-09 12:00:01' '1' output_file_coordinates_2.json"
    command2 = "python3 imagesatellite.py output_file_coordinates_2.json > output_coordinates_2.txt"

    try:
        subprocess.run(command1, shell=True, check=True)
        subprocess.run(command2, shell=True, check=True)

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_commands()
