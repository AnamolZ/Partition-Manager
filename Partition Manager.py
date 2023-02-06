import subprocess

def get_disk_list():
    """Return a list of available disk drives in Windows."""
    output = subprocess.check_output("wmic logicaldisk get name", shell=True).decode("utf-8")
    disk_list = output.split("\n")[1:-1]
    return disk_list

def create_partition(disk, size, file_system):
    """Create a new partition on the specified disk with the specified size and file system."""
    command = f"diskpart /s script.txt"
    with open("script.txt", "w") as script:
        script.write(f"select disk {disk}\n")
        script.write(f"create partition primary size={size}\n")
        script.write(f"format fs={file_system} quick\n")
    subprocess.call(command, shell=True)

def delete_partition(disk, partition):
    """Delete the specified partition on the specified disk."""
    command = f"diskpart /s script.txt"
    with open("script.txt", "w") as script:
        script.write(f"select disk {disk}\n")
        script.write(f"select partition {partition}\n")
        script.write("delete partition\n")
    subprocess.call(command, shell=True)

def main():
    """Main function to interact with the user and perform partition operations."""
    print("Welcome to the Partition Manager")
    print("Available disk drives:", get_disk_list())
    disk = input("Enter the disk drive to use (e.g. C):")
    while True:
        print("1. Create Partition")
        print("2. Delete Partition")
        print("3. Quit")
        choice = input("Enter your choice:")
        if choice == "1":
            size = input("Enter the size of the partition (e.g. 100MB):")
            file_system = input("Enter the file system to use (e.g. NTFS):")
            create_partition(disk, size, file_system)
        elif choice == "2":
            partition = input("Enter the partition to delete (e.g. 1):")
            delete_partition(disk, partition)
        elif choice == "3":
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
