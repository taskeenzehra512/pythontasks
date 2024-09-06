import subprocess

# Function to run a shell command and get the output
def run_command(command):
    return subprocess.check_output(command, shell=True).decode('utf-8').strip()


if __name__ == "__main__":
    
# Retrieve hardware details using lscpu and grep
byte_order = run_command("lscpu | grep 'Byte Order' | awk '{print $3, $4}'")
cores_per_socket = run_command("lscpu | grep 'Core(s) per socket' | awk '{print $4}'")
sockets = run_command("lscpu | grep 'Socket(s)' | awk '{print $2}'")
model_name = run_command("lscpu | grep 'Model name' | awk -F ': ' '{print $2}'")
cpu_mhz = run_command("lscpu | grep 'CPU MHz' | awk '{print $3}'")
cpu_max_mhz = run_command("lscpu | grep 'CPU max MHz' | awk '{print $4}'")
cpu_min_mhz = run_command("lscpu | grep 'CPU min MHz' | awk '{print $4}'")
virtualization = run_command("lscpu | grep 'Virtualization' | awk '{print $2}'")
l1_cache = run_command("lscpu | grep 'L1d cache' | awk '{print $3}'")
l2_cache = run_command("lscpu | grep 'L2 cache' | awk '{print $3}'")
l3_cache = run_command("lscpu | grep 'L3 cache' | awk '{print $3}'")

# RAM Memory (in MB) using free command
ram_memory = run_command("free -m | grep 'Mem:' | awk '{print $2}'")



# Path to the output file
output_file = 'hardware_info.txt'

# Write the results to the file
with open(output_file, 'w') as file:
    file.write(f"Byte Order:          {byte_order}\n")
    file.write(f"Core(s) per socket:  {cores_per_socket}\n")
    file.write(f"Socket(s):           {sockets}\n")
    file.write(f"Model name:          {model_name}\n")
    file.write(f"CPU MHz:             {cpu_mhz}\n")
    file.write(f"CPU max MHz:         {cpu_max_mhz}\n")
    file.write(f"CPU min MHz:         {cpu_min_mhz}\n")
    file.write(f"Virtualization Support:      {virtualization}\n")
    file.write(f"L1 Cache:            {l1_cache}\n")
    file.write(f"L2 cache:            {l2_cache}\n")
    file.write(f"L3 cache:            {l3_cache}\n")
    file.write(f"RAM Memory:          {ram_memory}MB\n")

print(f"Hardware details have been written to {output_file}")
