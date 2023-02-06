# Partition Manager

This is a Python script that allows users to create and delete partitions on a disk drive in Windows.

## Prerequisites

- The `subprocess` module must be imported.

## Functions

### get_disk_list()

This function returns a list of available disk drives in Windows. It uses the `subprocess.check_output` function to execute a `wmic` command to get the names of the logical disks, and then it decodes the output and splits it into a list.

### create_partition(disk, size, file_system)

This function creates a new partition on the specified disk with the specified size and file system. It writes a script file with the necessary `diskpart` commands and uses the `subprocess.call` function to execute it.

### delete_partition(disk, partition)

This function deletes the specified partition on the specified disk. It works similarly to the `create_partition` function, writing a script file with the necessary `diskpart` commands to delete the partition.

### main()

This is the main function that interacts with the user and performs the partition operations. It prints a menu with options to create or delete a partition, and allows the user to enter their choice. It uses the functions `get_disk_list`, `create_partition`, and `delete_partition` to perform the operations.

## Usage

To run the script, make sure you have the necessary dependencies installed and then execute the script. The script will show a menu with options to create or delete a partition, and prompt the user to enter the disk drive to use and any necessary parameters.
