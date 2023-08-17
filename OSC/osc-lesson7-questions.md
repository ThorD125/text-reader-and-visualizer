# Course Questions - Lecture 7
## Ownership
* Which command statements could you use to determine the ownership of a file/directory in linux?
ls -l {file}
stat {file}
getfacl {file}
* There are two levels of ownership in linux. Explain
The user level and the group level. The user level refers to the permissions granted to the owner of the file or directory. The group level refers to the permissions granted to the group associated with the file or directory.
* Explain CHOWN. What does it do ? Who can use it ? When ?
'chown' is a Linux command that is used to change the ownership of a file or directory. It allows you to specify a new owner and/or group for a file or directory, as well as recursively change the ownership of all files and directories within a directory.
* Explain CHGROUP. What does it do ? Who can use it ? When ?
'chgrp' is a Linux command that is used to change the group associated with a file or directory. It allows you to specify a new group for a file or directory, as well as recursively change the group of all files and directories within a directory.
* What is an orphaned file ?
An orphaned file is a file that is no longer being used or needed by any program, but still exists on the filesystem. Orphaned files can be created when a program or process creates a file and then crashes or is interrupted before the file can be deleted or closed properly.
Orphaned files can also be created when a file is deleted or moved, but its entry in the filesystem is not properly updated to reflect the change. This can happen if the filesystem is not properly unmounted or if the file is deleted using a low-level utility that bypasses the filesystem's normal delete mechanism.
Orphaned files can take up space on the filesystem and can potentially cause problems if they are left unaddressed. For example, if an orphaned file is still being used by a program or process, the program or process may crash or malfunction. Additionally, orphaned files can create confusion and clutter, making it difficult to keep track of the files that are actually being used.
* Which command statements could you use to determine your user's identity / group memberships ?
id
group
* Explain NEWGRP. What does it do ? Who can use it ? When ?
'newgrp' is a Linux command that is used to change the current user's primary group. It allows the user to temporarily switch to a different group, and then switch back to their original group when they are done.
## Permissions
* Which three permissions can a file have ?
Read permission (R): If a file has read permission, it means that the user can read the contents of the file. This includes the ability to view the file's contents, copy the file, and display the file on the screen.
Write permission (W): If a file has write permission, it means that the user can modify the contents of the file. This includes the ability to edit the file, delete the file, and create a new file with the same name.
Execute permission (X): If a file has execute permission, it means that the user can execute the file as a program. This is only applicable to files that are programs or scripts, and is not relevant for other types of files.
* What are the three levels in which permissions are set ?
User level: The user level permissions apply to the owner of the file. The owner has full control over the file, including the ability to read, write, and execute it, as well as the ability to change the permissions and ownership of the file.
Group level: The group level permissions apply to the group associated with the file. Members of the group may have less restrictive permissions than the owner, but more restrictive permissions than other users.
Other level: The other level permissions apply to all users who are not the owner of the file or members of the group associated with the file. These users typically have the least restrictive permissions, and may only be able to read or execute the file, but not write to it.
* Consider this : "-rw-r--r--. 1 root root 4135 May 27 21:08 /etc/passwd" . What does the first - mean in this case ? What else could you see there ?
Chat GPT:
In the example you provided, -rw-r--r-- is a string that represents the permissions of the file /etc/passwd. The first - indicates that the file is a regular file, rather than a directory or some other type of special file.
The rest of the string is made up of three sets of three characters, which represent the permissions for the user level, group level, and other level, respectively. In this case, the permissions are:
rw- for the user level, which indicates that the file has read and write permissions for the owner (root).
r-- for the group level, which indicates that the file has read permission for the group (also root).
r-- for the other level, which indicates that the file has read permission for all other users.
The rest of the line provides additional information about the file:
1: The number of links to the file.
root: The owner of the file.
root: The group associated with the file.
4135: The size of the file in bytes.
May 27 21:08: The date and time that the file was last modified.
/etc/passwd: The name and path of the file.
In this case, the file /etc/passwd is a regular file that is owned by the user root and the group root. The file has read and write permissions for the owner and read permissions for the group and other users. The file is 4135 bytes in size and was last modified on May 27 at 21:08.
* How do set permissions result in effective permissions for a given user in Linux ?
Chat GPT:
In Linux, the effective permissions for a given user are determined by the combination of the user's own permissions, the group permissions, and the other permissions for a file or directory.
The effective permissions for a user are calculated as follows:
If the user is the owner of the file, the effective permissions are the user level permissions.
If the user is not the owner of the file, but is a member of the group associated with the file, the effective permissions are the group level permissions.
If the user is neither the owner of the file nor a member of the group associated with the file, the effective permissions are the other level permissions.
For example, consider the following permissions string: rw-rw-r--. In this case:
The owner of the file has read and write permissions (rw-).
Members of the group associated with the file have read and write permissions (rw-).
All other users have read permissions (r--).
If a user who is the owner of the file tries to access the file, they will have read and write permissions. If a user who is a member of the group associated with the file tries to access the file, they will have read and write permissions. If any other user tries to access the file, they will only have read permissions.
It is also possible for a user to have permissions that are more restrictive than the permissions granted at any of the three levels. For example, if a user is a member of the group associated with a file that has rw- permissions, but the user's own permissions are r--, the user's effective permissions for the file will be r--, since they are more restrictive than the group level permissions.
The effective permissions for a user are used by the system to determine whether the user is allowed to perform a given action on a file or directory. If the user does not have the necessary permissions, the action will be denied.
* Explain CHMOD. What does it do ? Who can use it ? When ?
'chmod' is a Linux command that is used to change the permissions of a file or directory. It allows you to specify the permissions for each level (user, group, and other) separately, as well as set permissions recursively for all files and directories within a directory.
* What is the difference between using CHMOD symbolically or numerically ?
When using symbolic mode, you specify the permissions using a string of characters, where each character represents a different permission. For example, the permissions rwxrwxrwx can be represented as a=rwx.
Symbolic mode allows you to specify the permissions in a more human-readable way, using familiar symbols such as r, w, and x to represent read, write, and execute permissions, respectively. It also allows you to specify multiple permissions at once, using a combination of + and - to grant and revoke permissions.
When using numeric mode, you specify the permissions using a three-digit number, where each digit represents the permissions for a different level (user, group, and other). For example, the permissions rwxrwxrwx can be represented as 777.
Numeric mode allows you to specify the permissions more concisely, using a single number to represent all three levels of permissions at once. It is also easier to use when you want to set the permissions to a specific value, as you can simply specify the desired permissions directly.
* Explain UMASK. What does it do ? Who can use it ? When ?
'umask' is a Linux command that is used to set the default permissions for newly created files and directories. It determines which permissions are turned off (i.e., masked) when a new file or directory is created, and therefore which permissions are allowed by default.
* Explain ACL. What does it do ? Who can use it ? When ?
ACL stands for "access control list," and it is a feature of the Linux operating system that allows you to set fine-grained permissions for files and directories. ACLs allow you to specify permissions for individual users and groups, in addition to the traditional owner, group, and other permissions.
* Explain SETUID. What does it do ? Who can use it ? When ?
'setuid' is a special permission that can be set on a file or program in Linux. When a file or program has the setuid permission set, it is executed with the privileges of the owner of the file, rather than the privileges of the user who is running it.
* Explain SETGUID. What does it do ? Who can use it ? When ?
'setgid' is a special permission that can be set on a file or program in Linux. When a file or program has the setgid permission set, it is executed with the privileges of the group owner of the file, rather than the privileges of the user who is running it.
* Explain the sticky bit. What does it do ? Who can use it ? When ?
The sticky bit is a special permission that can be set on a file or directory in Linux. When a file or directory has the sticky bit set, it means that only the owner of the file or directory, or the root user, can delete or rename it. Other users are not allowed to delete or rename the file or directory, even if they have write permissions for it.
The sticky bit is typically used on directories that are used by multiple users, to prevent users from deleting or renaming each other's files. For example, the /tmp directory is often set with the sticky bit, to prevent users from deleting or renaming files that belong to other users.
## Boot
* In which stages can you split up a system's boot process ?
The boot process of a Linux system can typically be divided into the following stages:
BIOS (Basic Input/Output System) boot: This is the first stage of the boot process, and it involves the system's BIOS or UEFI firmware booting up and performing initial hardware checks.
Boot loader: After the BIOS boot stage, the system's boot loader is loaded from a bootable device, such as a hard drive or USB stick. The boot loader is responsible for loading the Linux kernel and initial RAM disk (initrd) into memory, and then transferring control to the kernel.
Kernel boot: The Linux kernel is responsible for initializing the system's hardware and setting up the basic system environment. It mounts the root filesystem, and then starts the init process, which is the first user space process to run on the system.
Init process: The init process is responsible for starting all of the other processes on the system, including system services and user programs. It reads the system's configuration files and starts the appropriate processes based on the system's runlevel.
System initialization: During the system initialization stage, the init process starts all of the necessary system services and user programs. The system is now fully booted and ready for use.
Note that the exact details of the boot process may vary depending on the specific Linux distribution and configuration. Some systems may have additional stages or may organize the boot process differently.
* What is the difference between firmware/bios/uefi ?
Firmware is a type of software that is programmed into a hardware device, such as a printer or router. It provides the necessary instructions for the device to perform its specific functions.
BIOS (Basic Input/Output System) is a type of firmware that is stored on a computer's motherboard. It is responsible for booting the computer and providing basic instructions for the operating system to start up.
UEFI (Unified Extensible Firmware Interface) is a newer type of firmware that replaces the traditional BIOS. It is designed to improve the boot process and provide more advanced features, such as support for larger hard drives and more powerful hardware.
* What is a bootloader ?
A bootloader is a small program that is responsible for loading the operating system (OS) of a computer or device. It is usually stored in a special area of the device's storage called the boot partition.
When the device is turned on, the bootloader is the first program that runs. Its main job is to load the OS and hand control over to it. The bootloader may also provide options for selecting different boot configurations or booting from a different device, such as a USB drive or network.
In general, the bootloader is an important part of the boot process and is responsible for ensuring that the OS is properly loaded and ready to run.
* Bootloaders are usally called 2-(or multi)stage bootloaders. Why ?
A two-stage bootloader is a bootloader that consists of two separate programs. The first stage is a very small, simple program that is responsible for loading the second stage of the bootloader. The second stage is a more complex program that performs the actual boot process, such as loading the operating system and handing control over to it.
The reason for using a two-stage bootloader is to make the boot process more efficient and reliable. The first stage of the bootloader is designed to be very simple and small, so it can be easily stored in a dedicated area of the device's storage called the boot ROM (read-only memory). This ensures that the first stage of the bootloader is always available and can be executed even if the rest of the device's storage is damaged or inaccessible.
The second stage of the bootloader is responsible for performing the more complex tasks of the boot process, such as loading the operating system and providing options for selecting different boot configurations. Because it is stored in a separate area of the device's storage, the second stage of the bootloader can be updated or modified without affecting the first stage.
* How does grub2 "boot" a system ?
GRUB2 (GNU GRand Unified Bootloader version 2) is a bootloader that is used on many Linux systems to boot the operating system. When GRUB2 is used as the bootloader, the boot process occurs in the following steps:
1. The computer is powered on and the BIOS or UEFI firmware begins to execute.
2. The BIOS or UEFI firmware loads the first stage of GRUB2 from the boot partition of the device's storage.
3. The first stage of GRUB2 loads the second stage of GRUB2 from the boot partition.
4. The second stage of GRUB2 displays a menu of available boot options and allows the user to select one.
5. GRUB2 loads the selected operating system and hands control over to it.
6. The operating system finishes booting and becomes fully operational.
* What does systemD atually "do" ?
systemd is a software program that is responsible for controlling the initialization of a Linux system and managing various system processes. It is the default initialization system on many Linux distributions, including Fedora, Red Hat Enterprise Linux, CentOS, and Ubuntu.
Some of the main tasks that systemd performs include:
- Booting the system and starting the necessary system services
- Managing system processes, including starting, stopping, and restarting them as needed
- Managing system resources, such as CPU, memory, and disk usage
- Providing a unified interface for managing system services and their dependencies
- Handling system shutdown and reboot procedures
* Which commands/statements could you use to troubleshoot/monitor a booting system ? 
dmesg: This command displays the kernel ring buffer, which contains messages and logs related to the system boot process. You can use it to view messages that are generated during the boot process and identify any errors or issues that might be causing problems.
