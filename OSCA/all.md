Operating system concepts

H1:
Programming languages:
-	Php
-	Java
-	C
-	…
Compiler VS Interpreter:
	Compiler:
	Takes all code and translates to machine code
	More time, but quicker execution
	Linking (Requires more memory)
	C, C++…
	Interpreter:
	Translate 1 statement at a time
	Less time, slower execution
	No object code, memory efficient
	Python, ruby…
Computers are 1’s and 0’s:
	This statement stands. Circuit boards consist of logic gates, inputs and outputs. All of these electronics are controlled through math!
Operating systems:
-	Linux
-	Windows
-	Apple
-	Android
-	…
What has an operating system?
	Computers
	Fridges/Microwaves (depends: I fit has more functions on single buttons there is probably software on there. If it’s fully mechanical, it isn’t.)
	Game consoles
What is an operating system?
	Software
	Set of programs
What’s the function of an operating system?
	Managing system resources
	Communicates with the user to hide complexity
Types of OS’s:
-	The point of view of the user
	User friendliness
	Simplicity
	Customization
-	The point of view of the system
	Efficiency
	Management
-	The Focus:
	Performance used to be important, but now ease for the user is.
Mainframe:
	Central computer
Functions of the OS:
-	Booting
-	Managing
-	Memory management
-	Loading & executing
-	Data security
-	Disk & Device management
-	The OS can interrupt and communicate where a resource is needed
Kernel VS User Space:
-	Kernelspace = system mode / privilege / supervisor / secure / unrestricted
-	Userspace = ordinary mode / user / restricted
History of computers:
	Needed to automate math
	First hand and fingers
	Then Chinese abacus
	Then Pascal’s calculator
	Then Leibniz Calculating machine
	Charles Babbage first computer
	Ada Lovelace first programmer and helped Babbage
	Jacquard’s Loom
	Punch cards
	Tabulating Machine
	Konrad Zuse with first programmable computer
	Alan Turing Enigma
	Mark-I
	ENIAC
	EDSAC
	UNIVAC mainframes
	IBM
	PC with RAM
Moore’s law:
	Number of transistors on a chip doubles every 2 years
UNIX:
	Ken Thompson
	B programming language
	UTF-8
	Dennis Ritchie
	C
	Linux and BSD are spiritual successors of UNIX
UNIX core principles:
-	Make each program do one thing well, build afresh rather then complicate old.
-	Expect the output of each program to become input of another
-	Design and build software, even OS. Don’t be afraid to throw away the clumsy parts and rebuild
-	Use tools in preference of unskilled help to lighten a programs task
	Build simple, short, clear , modular and extensible code
Posix:
-	Portable OS interface
-	IEEE
-	API
-	Utility interfaces
-	UNIX was standard
-	Manufacturer neutral
Character encoding:
	ASCII CODE
	0-127
	UNICODE -> standard
	UTF-8
	Ascii only 127 values
	Other Languages?
GNU:
	Not linux
	Richard stallman
	Free software
	Unix-like
	For all purpose
	Freedom for most things
	Linus Torvalds made the first kernal + Supporting GNU
	OPEN SOURCE

COURSE QUESTIONS:
What does it truly mean if people say: "computers work on 0's and 1's"?
•	What is a "framework"?
 a layered structure indicating what kind of programs can or should be built and how they would interrelate
•	What is a "library"?
collection of non-volatile resources used by computer programs
•	What is the difference between a compiler and an interpreter?
One translates code step by step the other translates all at once and one takes more time to execute but compiles quicker
•	What type of programming languages exist? Why are some called high- and others low-level programming languages?
Low level is code that needs to be turned into machine code, high level is for example Python which needs a interpreter or compiler for other languages
•	What is the difference between assembly code and machine code? What is disassembly in this context?
Assembly code is low level code and has to be “dissasembled” into machine code so a pc can execute it
•	What is a PCB (in a hardware context) and how are electronics and logical gates related? 
A PCB is a circuit board that has logic gates and uses math to function. 
Give 5 names of different Operating Systems (flavors)
Linux, macOS, android, windows, BSD
•	Which families are still common today / most used?
BSD and LINUX
•	How old are they?
1970
•	What is a Linux distribution?
An operating system which has branched out of Linux
Give a definition for "Operating System" (in a classic sense and as defined in this course)
An operating system is a software and a set of programs that manages the computer
•	Do a microwave, a fridge or a classic Game Boy have operating systems? (Note: we are not talking about smart fridges or microwaves ;)
In this case microwave, no
Fridge, no
Game Boy, yes
•	Explain the difference between virtualisation, emulation and simulation?
Emulation is acting like its a different system
Virtualization can still access hardware and acts like a different computer
Simulation is mimicing basic function of a computer
•	What is a mainframe?
Central computer
•	What is/are the primary goal(s) of an Operating System?
Managing memory, loading, booting, data security…
Why is there a new way of looking at "Operating Systems" (in a cloud / micro service / more modern sense)?
Explain the difference between User space and Kernel space.
Kernal space is unrestricted and priviliged
What are system calls?
Functions the operating system executes
What are drivers?
Set of files that tell hardware what to do
General Computer History (up to present day)
•	What made Pascal so special ?
First Calculator
•	Why are people like Charles Babbage and Ada Lovelace so critical in the evolution of (modern) computers ?
They created the first computer
•	Was there ever such a thing as a non-electronic computer ?
Yes, a “steampunk “computer
•	How did Alan Turing win the war ?
They had computers that could decipher enigma code
•	Which functions does a punch card have for a computer ?
Punch cards were used for Jacquard’s loom
•	What do we mean when we talk about the Von Neumann bottleneck ?
There was a throughput limitation, so neumann wanted to have data stored in memory
•	How does Moore's Law impact your cost of digital living ?
Every 2 years the transistors on a chip double but the price halves
A Matter of Unix
•	Why was Unix made at all ?
The current OS’ out there were insufficient so they made Unix
•	Why was Dennis Ritchie a crucial element in the evolution of the computer ?
He created the C language and UNIX
•	Who was Ken Thompson ?
Together with Dennis made the UNIX OS
•	What was the role of the evolution of B & C in the creation of Unix and subsequent Operating Systems ?
Dennis ritchie and Ken decided to create a new OS because current ones were lacking , but therefore needed to create a new language which would support their goals so C was created as successor of B
•	What are the core principles of the Unix Philosophy ?
See UP
•	Why is worse (sometimes) better in modern operating systems ?
A microkernel was better than a Monolithic Kernel based OS
•	Sketch the three main family lines that evolved from Unix
-BSD
Unix	- unix
	-GNU - linux

•	What is POSIX ?
A portable OS interface
•	What is UTF 32-16-8 ?
These are encoding formats
•	What's GNU ?
A unix-like OS 
•	What is a distro ?
A distribution of an operating system
•	How do you find out wich distros are most used and why would you want to know ?









H2:

Virtualization:
-	Hypervisor
	Type 1
	Runs on bare metal
	Type 2
	Runs on top of OS
Cloud:
-	Pay and use what you need
	Is a full blown machine needed?
	Is a virtual machine needed?
	…
Egress:
-	Outbound data: from inside to outside world
-	Watch out: in a lot of cases impact on the bill
Ingress:
-	Inbound data: from outside to inside instance
Careful: access ingress <-> network ingress

Scaling:
-	Vertical scaling:
	More memory, cpu, storage
	limited
-	Horizontal scaling:
	Make more
	Distribute workload
	Load balancing
Containerization:
	Docker!
	Used a lot in cloud
	Smaller footprint
	Less resources
	Faster
	Doesn’t matter for the user
	Docker swarm / Kubernetes
	An orchestrator for all these containers, a microservice/ OS for these containers.
	Often not needed
Serverless computing:
-	Serverless  servers but not worries about them
-	Pay as you go
-	Examples:
	Google cloud run
	Aws lambda
Caveats of cloud computing:
-	Vendor lock in
	Making sure it’s hard to pull out once everything is set up
-	Management
	Not easy to manage everything
-	Abstraction
	One click solutions are easy but no clue what they actually do
-	Security
	Easier automation, but also easier to forget stuff
-	Overwhelming
History:
-	How optimize efficiency
-	Make the most of a server
-	Hypervisors & VM
-	Today containers
Traditional software usage:
-	Different software you use involves:
	Different websites/ interfaces to download software
	Different licenses
-	Different installation
	32/64bit, windows /MAC
	Exe, zip …
	Different configurations
-	Different operation
	Different ways to run and stop
	Different ways to update
 
What is a container?
	An isolated process
Containerization == OS level virtualization
Default isolation:
-	CPU isolation
	Sequential execution of processes
-	Memory Isolation
	Standard process isolation
	Each has a virtual memory space
-	Privilege isolation
	Process run as admin has different access to other processes and files and resources than a regular user
Containers:
-	Docker is a toolset to manage containers
	Distribution of pre-defined images from repos
	Deploying containers
	Etc.
-	There are others:
	Rocket
	Comparable to docker but doesn’t use daemon
	By CoreOS
	LXC/LXD
	Linux containers
	Lightweight vm’s 
 


Linux containers:
-	LXC
	Linux containers
	Covers just about every containment feature supported by upstream kernel
	Focus on system rather than application
	Lightweight VM without overhead
-	LXD
	Extension to LXC
	User interface to manage containers
	Containers can be managed over network through REST API
-	Commercial support via Canonical (Ubuntu guys)
	Using LXCFS
	Container aware filesystem in userspace
Windows Containers:
-	Docker desktop
	Uses Hyper-V (doesn’t work well with VMWARE)
Docker nomenclature:
-	Docker uses IMAGES
	Small iso or blueprint
	Uses dockerfile
	From these images containers can be created
	A container can keep running but also stop after a job
-	Dockerfile
	A file containing commands to execute when running and creating a container
COURSE QUESTIONS:
What are containers?
Containers are isolated processes virtualizing on OS level
Why would anyone use containers? Aka. what is the prime goal/function of containers?
To cut costs and increase efficiency in for example servers
What is the difference between a container and a virtual machine?
A container is isolated and works on OS level
Why are the terms "container" and "docker" not synonyms?
Docker is a container manager, not necessarily a container itself!
List 2 other technologies to run a "container" without using "docker".
LXC/LXD
Rocket (rkt)
Is it possible to run the very same type of Docker container both on Linux and on Windows? Why or why not? How do Windows 10 and Windows 11 work around this?
A windows needs to have a linux subsystem to be able to use the exact same docker images
What is the difference between the Docker client (utilities) and the Docker server (~daemon)?
What is a Dockerfile?
A docker file is used to create an image, it is here where all commands are to setup and run the container
What is a Docker image?
An image is type of small iso and is used to create the container using the previously mentioned dockerfile
What is a Docker registry?
A place where you can find pre-defined docker images
What do the following docker commands do?
•	docker ps
Shows docker processes
•	docker images
Shows all images
•	docker run -d <imagename>
Creates and starts a new container using an image
•	docker exec -it <imagename> sh
Execute a docker container and open a new bash shell
docker compose up
Aggregates the output of each container
•	docker stop <containerid>
Stops a container
•	docker rm <containerid>
removes a container
What is the workflow (--> you should be able to do this yourself!) to properly deploy/ship/package an application:
1.	Create an application that prints "hello world" in a programming language.
2.	Create a Dockerfile for this application
3.	Build a Docker image from this Dockerfile
4.	Create and run a Docker container from this Docker image
5.	Interact with the container by entering (and gaining access with for example a shell) to the running Docker container
6.	Stop and remove the Docker container.
H3:
Processes:
-	Job = slightly older term
-	Process = same thing
Process vs Program:
-	Program/binary/executable:
	Passive
	No state
	Program code
	Not running
-	Process:
	Active
	Has a state
	Program code + counter + stack + data section + heap + …
Process states:
-	New: being created
-	Running: being executed
-	Waiting: waiting for event
-	Ready: waiting for assignment
-	Terminated: process finished execution
 

Process control block:
	Information associated with a process, a state saver
-	Process state
-	Program counter
-	CPU registers
-	CPU scheduling info
-	Memory management info
-	Accounting info
-	I/O status and related devices
-	List of open files
Context switch:
	Saving/storing a state of a process
	As a result a CPU can allow multiple processes
Stack vs heap:
	Stack uses LIFO and is a linear data structure
	Meanwhile heap is a hierarchial data structure

Big O:
-	Time and space complexity
-	Complexity chart shown with algortithms such as linear search etc…
Pass by value vs pass by reference:
-	Passed by reference:
	The caller and the callee use the same variable for the parameter, if the callee modifies it the caller sees the effect
-	Passed by value:
	The caller and callee have two independent variables with the same value, if one modifies it the other wont see.
Pointers:
	In low level programming is used to reference memory

COURSE QUESTIONS:
Terminology: What is the difference between a process and a binary/executable?
A process has a state and is active, meanwhile a program does not have a state and is passive
In the context of a process, what is "the stack" and what is "the heap"?
A stack is a linear data structure using LIFO, A heap is a hierarchial data structure
•	What parts of a process are on the stack?
•	What parts of a process are on the heap?
•	Given some code, know what is on the stack and know what is on the heap.
List all different process states in a diagram. Can every state go to every other state?
-	New
-	Ready
-	Terminated
-	Waiting
-	Running
No, some states such as the new state can only access one other state.
What is a process control block?
A data structure storing info about a process, such as program counter etc.
What is meant with "context switch" in the context of processes.
Using process control blocks you can store processes and move to a different process, allowing a single CPU to do multiple tasks at once
Why are pointers so important in low level programming?
This means a programming language such as C can access memory directly and store in variables for example
What is Big-O?
Time and space complexity using algorithms: one being a linear search
What is the difference between pass by value and pass by reference programming languages?
Pass by reference means both caller and callee are referencing the same parameter if one changes the value the other sees
Pass by value means the caller and callee have a parameter which has the same value but if one modifies it the other wont see it being changed

H4:

Deadlock:
	Multiple processes or programs are trying to access the same resource at once, this can cause issues such as corrupt data…
Dijkstra:
-	Wanted to illustrate deadlock issue, using the dining philosopher’s problem
-	5 people with a plate each but only one fork in between each pair of people
-	 
-	Deadlock conditions:
	Mutual exclusion:
	Only one process at a time can use the resource
	Hold and wait:
	A process must be holding at least one resource and wait to acquire additional resources that are being held by other processes
	No pre-emption:
	See CPU scheduling
	Circular wait:
	Cycle





Resource allocation graph:
	 
How to handle a deadlock:
-	Ignore it
-	Detect, recover (deadlock avoidance)
-	Take measures to avoid (deadlock prevention)
-	Deadlock prevention vs Deadlock avoidance
Safe sequences:
	How to:
-	Step 1: draw all processes and resources
-	Step 2: write down what process needs what resource
-	Step 3: go step by step and draw what process requires which resources
-	Step 4: go back to the first step of the sequence and draw the allocation
-	Step 5: write down all safe sequences possible after the allocation
-	Step 6: repeat until you are either out of safe sequences, meaning there is a change of a deadlock, or until all steps have been passed, meaning it’s safe.
See exercises

Memory management:
-	Basic hardware:
	Main memory and registers built into the processor itself, these are the only storage the CPU can access directly
	Processes need to be stored in memory
	Register built into CPU:
	Fast and accessible within one cycle of the CPU clock
	This isn’t the case with memory, so:
•	Add fast memory between CPU and main memory (A CACHE)
Process:
-	It lives in the memory unlike programs (that live in SSD/HDD)
-	Although there is Virtual memory:
	Use SSD/HDD as if its memory because of RAM shortage  SWAPPING
Memory management:
-	Consecutive memory allocation:
	Static partitioning
	Dynamic partitioning
-	Non-consecutive:
	Paging
	Segmentation
Partitioning:
-	Fragmentation:
	Internal fragmentation in case of static partitioning, the OS keeps track of average fragmentation so an improved partitioning can be determined
	External fragmentation in case of dynamic partitioning, OS decides to reorganize memory (Garbage collection)
	Coalescing:
•	Rebuild partition table, consecutive free partitions become one
	Compaction:
•	All occupied partitions will be stored consecutively followed by one partition, only possible in case of relocatable code
 








Non-consecutive:
-	Paging
	Basic method
	Logical address space:
•	Divided in pages
	Physical address space:
•	Divided in frames
 
 
	Normal page size: 512 bytes and 8KB
	Fragmentation:
	Internal
	½ frames average per process
	Page table needs internal memory, one entry per page
	Optimal page size?
	X = page size
	F(x) = overhead
	Optimal f’(x) = 0
-	Segmentation
-	Combination or segmentation and paging



Virtual memory:
-	When replacing a page an algorithm will be used:
	FIFO
	First in first out
	Oldest page gets swapped
	Easy
	Less suitable for frequently used page
	LFU
	Least frequently used
	Less used pages are swapped
	A page that has been used a lot in the past but not anymore will stay in memory
	LRU
	Least recently used
	Recent history as an indicator for the near future
	Timestamp usage
	Hardware assistance is necessary in other cases an LRU approximation is used
	OPT
	optimal
	Replace the page that will be inactive for the longest time
	Only theoretical, not implementable
-	Trashing
	More time spent on paging than execution
	CPU utilisation is low
-	Implication of virtual memory in code:
	Choose the right data structure
	Stack, queue -> good locality
	Hash table -> bad locality
	Choose the right algorithm
	Compare array access by row and access by column
-	Copy on write
	If 2 processes access the same page and one modifies the page, a copy of said page will be created
Address translation exercise:
-	Step 1:  get the power of input for ex. -> 4kb == 2^2 kb
-	Step 2: multiply it by 2^10 -> 2^2 * 2^10 == 2^12
-	Step 3: the power is the number of bits that must be the same to be a correct translation -> 12 bits == 3 hexadecimals
Memory management recap:
-	CPU = logical address = virtual address
-	Address register = physical address = real address

-	Consecutive memory (partitioning) = top to bottom and fill RAM

-	Non-consecutive (paging/segmentation/both) = assign chunks as a see fit, no order

-	Compaction = shift all free partitions to allow bigger processes to fit again

-	Segmentation = variant of dynamic partitioning, process broken into pieces, single process consists of heap, code, stack

COURSE QUESTIONS
•	What is deadlocking?
Multiple processes require the same resource at ones, with no rules applied, there will be a standstill
•	Who was Dijkstra?
Dijkstra knew of deadlocking and presented an easy-to-understand example: “The dining philophesors problem” where there would be 5 people dining but there would only be a utensil between each pair, and a person would require 2 utensils to eat. So, to solve this one person would pick up his utensils and eat whilst the others next to him waited for the utensil to be free again
•	What are the 4 deadlock conditions?
Mutual exclusion
Hold and wait
Circular cycle
No pre-emption
•	What is the difference between deadlock avoidance & deadlock prevention?
Deadlock avoidance is to detect a deadlock and try to recover, meanwhile a prevention is to make sure a deadlock never happens
•	What are safe sequences and why are they interesting?
With safe sequences you can tell if a order of processes will be able to safely execute without running into a deadlock, A safe sequence basically is a safe order for the processes to run one after another
•	What is the concept of virtual memory?
Using HDD/SSD as a place to store memory
•	What is the difference between the difference layer caches (1,2,3)?
•	What is the difference between an executable and a process?
An executable is stored on SSD/HDD and a process is stored in memory
•	What is "swapping"?
Using SSD/HDD as an alternative to RAM in case of RAM shortage
•	What is partitioning, paging, segmentation in the context of memory layout strategy's. Are they consecutive memory allocation or non-consecutive?
These are ways of storing memory, with partitioning storing processes in a linear block and segmentation splitting up processes.
Partitioning: consecutive
Paging: non
Segmentation: non
•	What is trashing?
More time spent on paging than execution, low CPU utilisation
•	What is the difference between a page and a frame?
A page is virtual, and a frame is physical
•	What is the copy-on-write principle?
If 2 processes are using a resource, that if one would make a change to said resource, that there will be a copy made of that resource

H5:

Thread:
	A lightweight process
	Minimize context switching time
	A blocking thread doesn’t block other threads
Threads vs Processes:
-	Processes and scheduling:
	Responsibility of the OS -> CPU scheduling
-	Threads and scheduling:
	Responsibility of application/program designer
Threads vs fork():
-	Fork -> system call that creates a new child process
-	Threads -> all part of the same process
Child and parent processes:
-	(linux/unix) if a parent dies, the child becomes an orphan and gets a new parent process (init/system (first process that starts with OS))
Process vs thread:
-	A thread is a basic unit of CPU utilization
	Thread ID
	Program counter
	Register set
	Stack
-	It shares with other threads:
	Code section
	Data section
	Other OS resources such as open file
Why threads?
	Image page gets frozen when downloading a file
	Multithreaded advantages In programming:
	Responsiveness
	Resource sharing
	Economy
	Scalability
	Disadvantages:
	Harder programming
	Never set in stone that a java thread is always mapped to an OS thread
Critical-unsafe-important code:
-	Important to understand which parts are sensitive
	Take care of it
	Shared resources
	Examples:
	Don’t use threads/ no sync
	Use semaphores signaling
	Use mutexes locking
	Add complexity for eventual consistency
COURSE QUESTIONS
- What are the differences between processes and threads?
A process is the responsibility of the OS and a thread of the programmer

- What are the similarities between processes and threads?
Both have a program counter, register and stack

- What are the benefits of threads?
Allows for Responsiveness, resource sharing, economy and scalability

- Give an example of a downside of using threads in an application?
Difficult programming

- What is function of the systemcall fork?
To create a new child process

- Is a childprocess the same as a thread?
No, a child process is linked to a parent, meanwhile all threads are part of the same process

- Can a child process live without its parent?
Depending on OS when a parent dies the child becomes orphaned, and will be assigned a new parent for example (init/systemd on linux)

- Can a thread live on its own?
Yes

- How can you protect a (critical) piece of code? Give the name of 2 examples. 1 is more a locking mechanism and the other a signaling mechanism.
Semaphore and mutex










H6:

File system:
	Service
	Abstract representation of secondary storage to the OS
Main memory vs Secondary storage:
	Main:
	Small
	Expensive
	Fast
	Volatile
	Directly accessible by CPU
	Interface:
	Memory address
Secondary:
	Large
	Cheap
	Slow
	Persistent
	Cannot be directly accessed by CPU
Virtual file system:
	Provides interface between data representation:
	By kernel, /dev/sda
	To the user process and data representation
	To kernel in memory, /home/user/myfile
	Because of the performance disparity between 
disk and CPU/memory, file system 
performance is the paramount issue for any OS
Secondary storage:
	Hard discs…
	Direct attacked (NAS) or network attached (SAN)
	Simple discs
	Described in geometry
	Minimum read/write size = sector size
	Access by surface, tack, sector
	SMART discs:
	SCSI, but also SAN&NAS
	Hide internal structure through HW controller
	Access by sector
	Don’t move the arm
	Sequential scan = 100x random access
Physical storages
	File systems always act the same, regardless of underlying physical medium
	A medium is mapped into a file location
	The power of /etc/fstab or /etc/vfstab or similar
Partitioning a hard disc
	Bucket  bits
	Partitioning = making accessible to an OS / give it a partition table
	2 options:
	Master boot record (MBR)
	GUID Partition table (GPT)
MBR:
-	First developed, wide backwards compatibility
-	Index located at specific point on disc
-	4 partitions max
-	But 1 and only 1 of them could be extended partition, may be split up into 23 logical partitions max
-	32 bit (2TB discs max)
GPT:
-	The standard in most modern OS
-	Index redundantly spread across disc
-	128 partitions max
-	64 bit
-	9.7 zetabytes discs max
		
Partitioning for dummies:
	Commands available:
	Fdisk
	Cfdisk
	Sfdisk
	Parted
	E.g. /dev/sda
	SCSI / SATA physical disk
	One disc per letter
	So /dev/sdc == third disk
Why partition?
	Flexibility
	Home directory explosion risk
	Swap control
	THINK BEFORE PART  CREATE A PARTITION PLAN:
 

File system flavours:
-	Ext2
-	Ext3
	Ext2 + journals
-	Ext4
	Ext3 + large file support
-	XFS
	High parallel throughput
	FAST
-	ZFS
	From solaris -> linux
	File checksum, remote replication
	PETABYTES
-	ReiserFS
	Fast, small files
File system concepts:
-	Hierarchically structured tree
-	Every location has meaning
-	Standardized, but variants exist
Mounting:
-	The root of a file system is stored somewhere
-	When HDD on a partition
-	You can combine several partitions to form the complete system
-	Combining one partition with the file system is called mounting a file system
-	Your file system is always seen as a tree structure, but parts of a tree can be located on a different partition, disk or even medium (usb…)
-	Identify a location of the file system as being a mount point
	E.g. /home is the mount point
	Under which every file is actuallu stored on a different location (everything below /home is stored on the second partition)
-	The partition you mount to the file system doesn’t need to know where it is mounted
-	You can mount users’ home directories at /home
-	But you could very well mount it at /srv/export/systems/remote/disk/users
Special partition types:
-	Proc
	Not linked to a device
	Pseudo filesystem
	Gateway to linux kernel
	The kernel talks with you through files that can be read/written to
-	Sysfs
	Not linked to a device
	Pseudo filesystem
	Gateway to linux kernel
	Why?
	More structured
	Tailored towards computer/software based parsing  human based parsing in /proc
-	Tmpfs
	Stored in memory
	Much faster than even ssd
	Data gone on poweroff
	Can still be slow on occasions
	Swap
	/tmp
	/dev/shm
	Shared memory
	Posix spec
	Very app dependent
•	ORACLE, VMWARE
-	Devtmps
	Contains device files managed by kernel
	Solves chicken and egg problem
	Start device on the fly
	Provides important device files
	Before udeb (device manager) is able to start up and take control
-	Devpts
	Pseudo filsystem
	Terminal emulation
	Ssh, telnet…
	Vs “on console”
	Dummy terminal allocation
	BEFOREhand
	Hundreds of fixed allocations
	/dev/tty
	Devpts creates and destroys device files as they’re needed
	Live in /dev/pts/number
	You can write to these files
-	Usbfs
	Pseudo filesystem
	Files are created and destroyed
	As USB devices are added or removed from the system
	Most usb devices are generic (belonging to a certain class, like usb storage)
	Linux has developed a framework that allows programs to work with usb devices based on characteristics through usbfs file system
	Deprecated sysfs
-	Nfs
	Network filesystem
	Allows filesystems that are hosted on remote machine to be mounted locally
	So /srv/export/systems/remote/disk/users
	On machine myhomehost.remotecompany.jp
	Can be mounted on local machines like /home
	Mount -F nfs
	My..jp:/srv/export/systems/remote/disk/users/home
-	Mqueu
	Pseudo filesystem
	Posix inter process message queue
-	Selinuxfs
	Pseudo filesystem
	Represents the SELinux subsystem in kernel
	Used in SELinux libraries
•	To interact with security servers
•	Query SELinux policy
•	And more
	Systems that don’t activate this wont have this filesystem mounted
Mount:
	Gone after reboot
	Easy to mount and unmount
Fstab:
	Makes it permanent
	/etc/fstab
	the device to mount
	the location to mount the device to
	the filesystem type
	addition options
	defaults for standard
	noatime (don’t register access times performance)
	users (allow reg users to mount)
	dump number
	file check order
File system locations:
-	/bin
	Executable programs needed to run system
	Migration towards /usr/bin and symbolic links compatibility
-	/etc
	Contains all config files for system
	Not user specific config
-	/lib
	System libraries to run system
	To run commands in /bin
	Migrated to /usr/lib
-	/sbin
	Executable programs to run system
	Contains solely for system administrative purposes
-	/usr
	Root of users
	Usually mount point of any medium
-	/usr/X11R(N)
	All files needed for graphical window
	Divided in binaries (/bin), libraries (/lib) and header definitions (/include)
	For programs relying on X11
-	/usr/bin
	Contains all executable programs
-	/usr/lib
	Contains all libraries for mentioned programs
-	/usr/share
	Contains all app data
-	/usr/local
	Often separate mount
	Contains programs specific to local system
	/usr might be shared across different systems in large environments
	Roaming system profile
-	/usr/sbin
	Executable programs
	Contains programs for system administrative purposes
-	/home
	Contains all homedirs of all local users
-	/boot
	Contains static boot files
	Not needed once system boots
	E.g. bootloader config
-	/media
	The mount point for detachable storage
-	/mnt
	Temp mounted media
-	/opt
	Add-on packages, usually used to install apps into
	Which are not provided by native package manager
	=> /usr
	Nor built specific to the local system
	=> /usr/local
-	/tmp
	Temporary files for system tools
-	/var
	Data that changes in size, log files, caches, etc.
How to do something with a file:
-	Through the file name:
	Get to the file’s file control block
	Using system catalog
	Commands:
	Open
	Close
	Set_attribute
-	The system catalog:
	Maps a file to FCB
	Checks permissions
Directories:
-	Files with information of other files
-	UNIX directory
	A file
	Has
•	Owner
•	Group owner
•	Size
•	Permissions
•	I-node type structure
•	Many file operations can be used on directories
•	Kernel imposes special structure on it when the command to create it used:
	Mkdir
•	Whose data is an array or list of filename/i-node#
•	Data is stored binary
	Was text
	Performance
Mkdir:
-	Creates a subdir file and an inode for it
-	Inode and file name are added to parent
Files and inodes:
-	Info of every local file in a structure  inode
-	1-1 mapping of file and inode
-	Multiple files may have the same inode
-	Each inode is identified through a number
-	The inode hash array is a list of allocated inode’s located at the beginning of the file system
-	Inode structures
	Are stored on the file system block E.g. disk
	In a predefined location on disk, UNIX -> inode list
	Where it is exactly is system  implementation specific
-	Inode numbers have only local meaning to each file system
-	One file system per partition, one inode table
-	Hierarchical structure: some FCBs are just a list of pointers to other FCBs
-	To work with a file the inode of the file is brought into main memory as an in-core inode (v-node)
Directory structures:
-	Link between INODE has list and directory files
-	The root /
	Inode = 2
	Directory data block is located through #2
-	Directory file entries include each entry <filename, inode#>
-	Hard link = direct pointer to a file INODe
-	Soft link = pointer to another directory entry
-	In a link, rm clears the directory record
	Inode is set to 0
	File may be unaffected
	The file inode is deleted
	When the last link is removed
	The data block for the file is also deleted/reclaimed
Superblock:
-	One per filesystem
	Size of file system
	Number of free blocks
	Size of logical file block
	List of free data blocks
	Index of next free block
	Size of INODE list
	Number of free Inodes
	List of free inodes
	Index of next free inode
-	Tune2fs -I /dev/sdax
	Display super block
Archiving and compression:
	Archiving:
	Collapse multiple files into one
	Few files or multiple directories
	Compression
	Make files smaller
	Remove redundant info, replace with smaller code
	Can be applied to files, group of files, directory trees
	Uses:
	Managing log files
	Sharing group of files
	Compression for efficient transfer
	Keep files together grouped by time
	Lossless:
	Decompressed file in original state
	Doesn’t compress super well
	Data to preserve
	Logs, docs, binaries, configs
	Lossy:
	Decompressed file might lose info
	Drops unimportant info
	Images/sound/movies
	Gzip & gunzip
	Uses Lempel-ziv coding
	Lossless compression, good efficiency
	Bzip2 & bunzip2
	Burrows wheeler block sorting
	Lossless compression, slightly more efficient, requires more CPU
	Almost identical to gzip
	Lempel-ziv:
	Directory-type compression
	Dictionary is built up when reading source
	Uses detected repeating patterns
	Perfect for tekst compression
	Also used in GID, TIFF
USERS:
-	Files in /etc contain system configuration
-	/etc/passwd defines account info for users
-	Each line:
	name:password placeholder:user id:primary group id:comment:home 
directory:shell
 
-	/etc/shadow contains info about user passwords
	Each line:
	Name:password:lastchange:min:max:warn:inactive:expire:reserved
 
To see account info grep ‘username’ /etc/passwd

System accounts:
-	Sys accounts are designed to provide accounts for services on the sys
-	UIDs between 1-499
-	Have non-login shells
-	Have * in password field
-	Critical for system operation
System groups:
-	Each user can be a member of one or more groups
-	/etc/passwd contains primary group per user
-	Supplemental groups in /etc/group
 
-	Create a file that owned by one of your secondary groups using:
	Newgrp group_name
-	If you are not a member you need to know the password
-	Open a new shell with new primary group
-	Use ID to verify
-	Use exit to return
Root:
-	Logging in
	Su –login / sudo
	Su opens a new shell as another user (UID changes but doesn’t assume all env)
	Su – to login as if the user executed a login
-	Sudo setup
	Configuration in /etc/sudoers
Who command:
	Displays a list of currently logged in users
W command:
	Displays detailed user and system info
 
COURSE QUESTIONS:
File Systems
What does it actually mean when we say data is "persistent" ?
Meaning it’s not volatile, the file is stored
Why does a  userland process needs to use a file system to store/read data on a storage medium (and not just direct IO access) ?
When taking about non-ssd discs, what is the advantage of sequential i/ ?
Is this advantage the same for ssd discs ?
Compare the two "versions" of partitioning (number of partitions, bios support, max disc size)
MBR -> 4 partitions, all bios, 2tb
GPT -> 23 partitions, needs uefi, 9 zetabytes
Why not throw everything into one single monster partition?
Structure, flexibility, swap control
What does /dev/sda3 mean ?
This is one of the possible partition table storing locations. /dev/sda[1-15]
Why can/should you give a hex code of a partition tyoe to a parititon when you create one ?
What form does "a swap" have in Linux ?
Tmpfs, which is a memory storage, which is faster than ssd
Which are the most used file system flavors in current linux ?
EXT2, EXT3…XFS, …
What does it mean when something is mounted on a certain directory location ?
Assigning a storage device to a directory so it can be accessed by the OS
What is a pseudo file system ?
File that isn’t a file but is supposed to represent more of an virtual entry
The tty command tells you which terminals you are currently using. Let's say one user gets as a reply /dev/tty1. and another user gets as a reply /dev/pts/0. what is the difference between those two users ?
What is an nfs type partition ?
Network file system
What does /etc/fstab do ?
Mount files permanently
Some directories are present in almost every linux distro. Name them and describe their role briefly.
/etc, /tmp, /var, /boot…
What is a FCB ?
A File control block
How so is a directory also a file ?
A directory is kinda a file that just holds info about the underlying files, using local inodes…
What is an INODE ?
A pointer containing a file name and location
Whast is the difference between a hard and a soft link ?
A hard link references the Inode number of a file, soft link references the file in its directory
What is a superblock ?
Block containing info about the filesystem such as free blocks, used blocks…
Archiving & Compression
Does archive always compress ?
No, they are 2 different things, archiving is mashing multiple files into one, meanwhile  compressing is cutting out useless info
What is the difference between lossless and lossy compression ? give an example of both.
Losing details/redundant info
Briefly describe a few archiving/compression tools commonly found in Linux.
Gzip, gunzip, bzip2, bunzip2
Users
What can you find in the /etc/passwd & /etc/shadow files ?
User info and password info
What is so special about system accounts in Linux ?
They are essential for a functional system and have no shell and their password fields is *
What are groups in Linux ?
Collections of users with set permissions and ownership
How many groups can a user be a member of/use at once ?
As many as their hearts desire, but only 1 primary group
What is the correct way of becoming root ?
Su – login or su -, NOT SU because then you will only be in the shell of root and not have all env
Describe the sudo concept
Being able to use a single command as a different user
Who's on your system right now ?
Use who

H7:

Ownership:
-	View file ownership:  ls -l
-	View directory ownership  ls -ld
-	View ownership  stat

	Every file is owned by  a user and group
	If a user creates a file, they are owner
	Chown  change file ownership (only root)
	System uses UID to associate file ownership
Orphaned files:
	If a user is deleted, or changes UID, their former UID is shown on files
	If a group is deleted, or has its GID changed, the former GID is shown also

identity info:
-	To see identity of current account  id
-	Also try whoami
Group membership:
-	See names of the groups you’re a part of  groups
-	If you’re added to a group while logged in, you have to log out and in again for the new membership
Change file/group ownership:
-	Chown to change user and group ownership
	Can only be used by root
-	Chgrp to change group ownership
	-R makes it recursive
-	Newgrp changes your effective primary group by opening a new shell with a different primary group
-	Usermod -g groupname username to permanently change group
Permissions:
-	Ls -l shows 10 first characters:
	1: filetype
	2-4: user permissions
	5-7: group permissions
	8-10: other permissions
-	Only 1 of three sets will apply to you:
	If you’re the user owner, the first 3 apply
	If you’re not the owner, but part of the group the second set of 3 applies
	If neither of the previous applies you are given the last set of 3
-	If a user owns a file but not the directory the user won’t have any access
Chmod:
-	Change mode
-	Modify permissions
-	Either:
	Symbolic
	Numeric
	4 = read
	2 = write
	1 = execute
 
Umask:
-	The umask value is used to determine default permissions that are set on a new file or directory
-	default permissions are determined by removing permissions in the umask from the maximum allowable permissions
-	max for:
	file: rw-rw-rw / 666
	directory: rwx-rwx-rwx / 777
-	to display current umask: umask
-	to set umask value: umask <value>
-	umask will only apply on current login session
-	to set the default, modify /.bashrc
-	umask has no effect on existing files or directories
ACL (access control list):
-	because others = “everyone else”
-	to enable  the filesystem must be mounted with acl option
-	the acl can be modified using setfacl:
	setfacl -m “u:user:permissions” <file/dir>
-	you’ll notice a + next to permission in ls -l
setuid permission:
-	is set on certain system utilities so that an ordinary user can execute the program as if it was run by the root user. This allows users to do common sys admin stuff without root
-	example; change setuid for /usr/bin/passwd -> users can change their password without root
-	files with setuid will have an s added to user permissions, if it’s an S that means there’s no execute permission
-	chmod can be used to set setuid:
	chmod u+s file
setgid permissions:
-	similar to setuid, but with group permissions
-	chmod can be used to set setgid:
	chmod g+s file
sticky bit permission:
-	is used to prevent others from deleting files that they do not own in a dir that is shared with others
-	normally if a user has write permission on the dir, it can delete any file in the dir
-	when sticky bit permission is set the letter t will be placed on the permissions
-	unlike setuid and gid, where capital letter indicated a problem that would prevent those permissions from working, the presence of the letter T doesn’t always mean sticky bit is set correctly
-	if either the user owner or group owner have execute permissions, then it is possible for the sticky bit permission to work as intended
-	if only the user has execute permission then It doesn’t make sense
-	setting sticky bit:
	chmod +t dir
Boot process:
-	4 stages:
	Firmware stage:
	Referred to as BIOS
	UEFI replaced BIOS on most systems
	2 primary jobs:
•	Power-on-self test, ensures hardware works
•	Load master boot record (MBR), contains drive partition table and loads first stage bootloader whose purpose is to load the second stage bootloader (next stage)
	First stage bootloader:
•	Max 446 bytes
•	64 bytes partition table 6 bytes crc
•	Loads kernel directly
	Most common bootloaders:
•	LILO – linux loader
•	ELILO – efi linux loader supports systems with UEFI
•	GRUB – grand unified bootloader supports UEFI and kernel flavour choice
	Other bootloaders:
•	SILO – SPARC improved bootloader supports linux on sun SPARC hardware
•	YABOOT
	Network booting:
•	PXE – preboot execution environment for hardware that supports TFTP
	Kernal phase:
	Grub2 loads the chosen kernel in memory and passes control to it using files in /boot
•	An initial ram disk image (initrd/initramfs)
	Temporary / as tmpfs
•	The kernel files (vmlinuz) with basic devices
•	Kernel start up: system becomes active
	PID 1
	SystemD phase:
	Set kernel options using /etc/sysctl.conf
	Starts udevd daemon to detect all devices
	Imports network config
	File system check the root file sys if necessary
	Decrypts filesys if encrypted
	Mount filesys according to /etc/fstab
	The real root is mounted
	Enable swap devices
	Eventually
•	System boots in a specific target mode
	system is managed by systemctl command
dmesg command:
-	executed after boot to view messages generated by the kernel during the boot process
	useful for troubleshooting
-	also executed upon connecting a new device to see device pathname
/var/log/messages:
-	kernel boot messages are stored in /var/log/dmesg which is overwritten each time the sys boots
-	file updated traditionally by syslogd and klogd daemons
-	syslogd and klogd have been replaced by rsyslogd and syslog-ng daemons
Daemons:
-	the admin can control which services will be provided by various daemons
-	a daemon is a running program that provides a service
systemctl:
-	used in systems that have system
-	services are a type of system unit
	configured in /etc/system/system
	.service files
-	To start a service: systemctl start
-	To stop a service: systemctl stop
-	To check status: systemctl status
-	View all running services: systemctlk -a
-	To start a service automatically: systemctl enable
Target:
-	A state where a consistent number of services are running
-	Has:
	Required dependencies
	Parallel dependencies
	Conflicting dependencies
	Sequential dependencies
-	To change current target state: systemctl isolate graphical-target
-	To change the default target state: systemctl set-default multi-user.target
COURSE QUESTIONS

Ownership
Which command statements could you use to determine the ownership of a file/directory in linux ?
Ls -l and ls -ld
There are two levels of ownership in linux. Explain
User ownership (as user is assigned as owner) and group ownership (a group is assigned as owner)
Explain CHOWN. What does it do ? Who can use it ? When ?
Change ownership, used to change the user owner and or group owner of a file. Can only be used by root
Explain CHGROUP. What does it do ? Who can use it ? When ?
Same as chown but only changes group and can be used by a regular user
What is an orphaned file ?
A file of which the owner either has changed uid or has been deleted
Which command statements could you use to determine your user's identity / group memberships ?
Id and groups
Explain NEWGRP. What does it do ? Who can use it ? When ?
This creates a new shell in which you have temporarily set your primary group to a different one
Permissions
Which three permissions can a file have ?
Read, write, execute
What are the three levels in which permissions are set ?
User, group, others
Consider this : "-rw-r--r--. 1 root root 4135 May 27 21:08 /etc/passwd" . What does the first - mean in this case ? What else could you see there ?
Filetype, could be a d for example
How do set permissions result in effective permissions for a given user in Linux ?
Explain CHMOD. What does it do ? Who can use it ? When ?
Change permissions on a file using numeric or symbolic values, can only be done by root
What is the difference between using CHMOD symbolically or numerically ?
Using for example; 777 compared to u+rwx g+rwx +rwx
Explain UMASK. What does it do ? Who can use it ? When ?
Umask is a standard set of permissions which overlap any newly made files’ permissions so if the umask would be 022 and a file would be made with 666 then the permissions would become 644
Explain ACL. What does it do ? Who can use it ? When ?
Access control list, used to limit and allow users part of the others level
Explain SETUID. What does it do ? Who can use it ? When ?
Makes it so users can use a file as root without being root
Explain SETGUID. What does it do ? Who can use it ? When ?
Same as SETUID but for groups
Explain the sticky bit. What does it do ? Who can use it ? When ?
Makes it so a user that can access a directory but doesn’t have write permissions on a file in that directory to be able to delete that file
Boot
In which stages can you split up a system's boot process ?
Firmware
Kernel
systemd
What is the difference between firmware/bios/uefi ?
What is a bootloader ?
a loader with the purpose of loading the next stage, being the kernel stages
Bootloaders are usally called 2-(or multi)stage bootloaders. Why ?
it does  apower-on-self test and then loads the kernel stage
How does grub2 "boot" a system ?
gives control to the kernel using the files in /boot
What does systemD atually "do" ?
all system functions
Which commands/statements could you use to troubleshoot/monitor a booting system ? 
Dmesg


H8:

Firmware:
	first layer of software between OS and hardware
	does the hardware initialization and then hands over the control to the operation system
Coreboot:
-	open source firmware alternative
-	replaces UEFI or BIOS
-	Do as much as needed then jump to payload
Firmware hands over control:
-	To a payload
	Can be anything
-	The payload will hand it over to the OS
-	Bootloader, GRUB…
-	But can also be a stripped down linux kernelss~
Toolchain:
-	Set of programming tools used to perform complex software dev task or create a software product
-	Simple version:
	Compiler and linker
-	But different linux distros ship with different toolchains e.g. gcc versions
-	Make crossgcc-i386
QEMU:
-	Type 2 hypervisor
-	Linux
-	Good at emulating generic x86 PC
SystemD:
-	Decides what daemons are running
-	Consult it with systemctl
-	.service:
	Configuration
	Constructed so systemd knows what you want it to do
Unit section:
-	Description:
	Human readable title
-	After:
	Set dependency on a service
-	Before:
	Start current before another service
-	Service section:
	ExecStart:
	Command to be executed
	ExecReload:
	How a service is restarted
	Type:
	Start up type
	Restart:
	When it should be restarted
-	Install section:
	Wanted by:
	Similar to after & before
	Used to specify system-equivalent runlevels
	Required by:
	Similar to wanted by
	Specifies hard dependencies
COURSE QUESTIONS:

BOOT
Why would you replace your firmware with an open source version ?
Gives you more control of what happens when your pc is booting
What is a "payload" in the coreboot world ?
A payload can be anything, but it basically hands over control to the OS once it is finished.
What is a toolchain ?
Set of programs used to make complex software dev programs
Simplest version:
	Compiler & linker
When you ise Coreboot to build your own BIOS rom, are all black boxes gone then ?

What is Qemu ?
A type 2 linux hypervisor
What is Seasboot ?
Give some secondary payload examples.
How can you build a custom firmware rom for other hardware ?
SystemD
What does systemD "dp" when you get down to it ?
It controls what daemons are running
Which command allows you to communicate with SystemD ?
systemctl
What are .service files (for) ?
tasks that are executed on boot
Explain the following keywords that are often found in SystemD configuration files : Description, Before, After, ExecStart, ExecReload, Restart, WantedBy, RequiredBy
human readable title
has to be executed before
has to be executed after
command
reload instructions
when to restart
similar to before and after
similar to wanted by but hard dependencies
How can you make systemD aware of the presence of a new service ?
What happens when you "enable" a service that is wanted by a Target ?
What is the difference between a user level .service and a root level .service ?
How is the home directory specified differently in a script vs a .service file ?
What's the advantage of a SystemD service over a scheduled or a user-started process ?
WHat happens when you kill a process started via SystemD ?






H9:

Pros of windows:
-	Easier setup and config  no steep learning curve
-	Better technical support
-	Better integration with MS software
-	Most features are bundled and exist 
Cons of windows:
-	Less reliable for servers  more downtime
-	Most used  less secure because primary target for malware
-	Higher TCO (total ownership costs from licenses)
-	Less performant
Deployment:
	Putting in production/end users can use it
	End users have become critical:
	Want 100% uptime
	Generally want web apps (without realizing)
	So deployment on windows has seen a decrease
Recap hados:
-	Cmd(text output) is not powershell(object .NET output)
-	Process management  task manager, process explorer, get-process
-	User management  lusrmgr.msc, Get/Set-localuser
-	Logging/events  eventvwr.msc
-	PowerShell  Get-help, get-command
-	Windows version  winver
Windows client vs server:
-	Windows 10 and windows server 2016/2019 look the same and use the same NT-kernel but have many differences
-	Windows servers support higher end hardware
-	Server allows more concurrent remote connections
	As a file share system:
	Win 10: 20 max
	Win server: 2147483647  additional licensing (CALS = Client access license)
	As a remote system:
	Win 10: max 1
	Server max 2
-	Server includes a lot of software (DNS Server, DHCP server, file server, print server, web server)
-	Server can be installed without GUI (windows server Core)
-	Server only available in 64bit
-	Server has heightened security by default
-	Server doesn’t support signing in with MS accounts
-	Server is more expensive (licenses)
-	Configured to prioritize background tasks as opposed to programs
Windows server release channels:
-	2 primary channels:
	Long term servicing channel (LTSC)
	For longer servicing and functional stability
	Semi annual channel
	For customers who want OS capabilities at a faster pace
	
Editions:
-	Standard edition:
	Enterprise features, limited virtualization rights (only 2 hyperv containers)
-	Datacenter edition:
	Unlimited virtualization rights
-	Hyper-V server 2019:
	Bare metal hypervisor (no license cost), no GUI
Installation options:
-	Server core
	Small footprint  reduces required disk space and security attacks
	No desktop
	Default
-	Server with Desktop
	Largest footprint
-	Nano server:
	Smallest footprint
	Less security exposure
	Fewer required reboots
	Designed for cloud applications and containers
Where to install?
-	On premise:
	Lower TCO
	Complete control
	Uptime
-	Cloud advantages
	Anywhere and anytime access
	Worry free IT
	Quick deployment
	Scalability
Licensing:
-	Retail:
	FPP (Full packaged product) intended to be sold separately from the computer for install
	May be transferred with limitations
-	OEM:
	Preinstalled on a computer by the OEM (original equipment manufacturer)
	May not be transferred to another computer
-	Volume:
	Used in orgs to legitimize windows on multiple computers
	Uses a single license key, Volume license key (VLK)
-	Slmgr utility on the Cli
Windows server management:
-	How?
	Locally  not practical
	Remotely  using RDP (remote desktop protocol), RSAT (remote server administration tools)
-	Management tools:
	CLI:
	Legacy windows commands
	PowerShell commands
	Traditional GUI based tools:
	Server manager
	MMCs (Microsoft management consoles): DNS manager…
	Web based:
	WAC  Windows admin center
Windows Remote management (WinRM):
-	Windows native built in remote management protocol to interface with remote computers and servers
-	Default ports:
	5985, 5986
Why windows server:
-	Active directory
-	DHCP server
-	DNS server
-	File server
-	Web server
-	Certificates and Authority
-	Use cases:
	Application server (.NET), database server, back-up…
Windows network models:
-	2 main types:
	Workgroup model
	Decentralized management
	Domain model
	Centralized management
-	A freshly installed server is always part of a workgroup
Workgroup model:
	Small p2p network
	Each computer has its own local users, stored in SAM (security account manager), to log in you need a local user on that computer
	Each computer has its own local policies
	Workgroups are only suitable for home networks and small businesses
Domain model:
	Logical group of objects, stored in a shared(distributed) database (active directory/AD). 
	You can log into any computer if you have an account on the domain
	Has its own domain based policies
	Now: linked through azure active directory
Active directory structure:
	Hierarchical arrangement of objects
	Object can be a container or leaf
	Container is an object that contains other objects (domain container is root)
	leaf objects:
	resources: printers, GPOs…
	security principles: these kind of objects are assigned unique SIDs
	each object has a set of attributes
	can be accessed by LDAP (lightweight directory access protocol)
 







Organizational units:
-	administrators can create hierarchy within an AD by using special containers: Organizational units
-	an OU can be used to group objects within a domain
-	After install there is only 1 OU, Domain controllers
-	Why use them?
	Deploy group policies For example, deploy a policy to students
	Delegate administrator tasks
Computers in a domain model:
-	3 types:
	Domain controllers (holding AD)
	Member servers (DHCP…)
	Clients (win 10)
-	Linux can also join a windows domain with SAMBA (open source)
-	Each domain has a domain controller DC, 2 for good practise
-	Computers belonging to the same domain but different local network = sites
Domain model design:
-	Single domain model:
	Simplest, most used, one domain
	Small to medium orgs
-	Single domain tree model:
	1 or more domains in tree
	Big companies
-	Multiple domain tree model:
	1 or more domain trees linked together
	Security boundary within which objects are accessible
	Sometimes used in merging companies (that keep its own name)
User authentication:
-	When they logon, must be authenticated
-	Typically done by username and password
-	In domain:
	Domain based authentication
	Used to log into domain from any computer in domain
	Uses Kerberos protocol
	Local authentication:
	Can only be used to login locally (not possible on DC)
	Uses NTLM protocol
-	Authentication formats:
	Domain based:
	Domainname/username (legacy)
	username@DNSdomainname (UPN universal principal name)
	local:
	computername/username
	./username
Attention:
-	To convert a server to domain controller:
	Fixed IP address
	Configured as DNS server
-	Every server (full and core) can be promoted to DC
-	On domain controller you can only sign in using domain user account
-	Best practice:
	No extra roles on DC (except DNS)  most important server is DC
AD replication:
-	Changes made to AD on DC, are systematically synced with all DCs, this is called AD replication
-	Computers in domain also have a common namespace based on DNS:
	If name = firm.com, a pc could be computer.firm.com
Writable vs read only DCs:
-	Writable DC:
	Most commonly used type
	Contains an AD in which all read and write is possible
	First DC is always writable
-	Read only:
	Contains an AD in which only read operations are possible, can only replicate data from writable DCs and never replicate TO other DCs (ONLY INBOUND)
Single domain tree model:
-	Hierarchical
-	First domain = top level domain = root domain
-	Subdomains are called child domains of the domain (parent domain)
-	Shares contiguous namespace
AD partitions:
-	AD database is stored in system32/ntds.dit (NTDS NT directory services; DIT directory info tree) on every DC
-	AD database is divided up into at least 3 partitions:
	Domain partition  updates are replicated to all DCs within the domain
	Configuration partition  updates are replicated to all DCs within the forest
	Schema partition  updates are replicated to all DCs within the forest
-	There may be one or more app partitions
Global server catalog:
-	Special domain controller
-	Stores:
	Full copy of all objects in the directory for its host
	A partial set of attributes, read-only copy of all objects for all other domains in the forest
-	GCs are interesting for forest wide search operations
-	By default the only GC that is created, is the first domain controller in the forest root domain, you can add GC functionality to other Ads
-	Good practise:
	Atleast 2 GC (redundancy)
	1 CG per site
Round robin DNS:
-	Technique, used for load balancing when a web site is placed on a different physical web server
-	Multiple A records need to exist for it to work (one for each IP of physical servers)
-	When the first user accesses the web site, round robin DNS will sent him to the first IP address, second to the second….
Cryptography:
-	Disadvantage of private key cryptography: how to safely exchange?
-	Disadvantage of public key cryptography: algorithms are much more complicated, slower, only for small data
-	Usually a mix of both is used
Digital signature:
-	Authenticity 
	Ensure the signer is who they claim
-	Data integrity
	Ensure content has not been changed since signing
-	Non-repudiation
	Ensure the sender cannot deny having sent it
-	Creation and verification:
	Sender calculates the hash value and encrypts the value with a private key. The result is a digital signature or fingerprint
	The sender sends his message and digital signature
	The recipient decrypts the signature with the public key of the sender
Certificates:
-	In public key encryption, one must be able to verify the identity of the owner of the public key (anyone can create a pair). So, public keys are provided with a digital certificate, which is issues by a trusted third party/CA
-	X.509:
	Describes info and format of digital certificate
-	Every certificate has a digital signature, created with private key of CA. the signature is used to prove authenticity
-	Popular certificate: SSL-cert (HTTPS)
Certificate chain:
-	List of SSL certs, from root to end user cert
-	In google  settings menu
Certificate usage:
-	To setup HTTPS web server
-	SSL and TLS are cryptographic protocols
	Authentication of communication partners
	Confidentiality: exchanged data is encrypted, using symmetric key
	Data integrity: altered data can be detected because SSL/TLS is using MAC
-	SSL/TLS uses handshake procedure before data is exchanged
Authentication:
-	Ability to verify the identity of a user or device
-	Windows networks:
	NTLM:
	Relies on password authentication, used in workgroup model
	Introduced as default authentication protocol in old windows NT networks
	Kerberos:
	Relies on password authentication, used in domain model
NTLM:
-	Uses challenge/response protocol to authenticate without password
-	Steps:
	Client sends an authentication request to server
	Server sends a challenge (random number)
	Client calculated on that challenge, based on a secret that both client and server know. Here the calculation is based on the NT hash of the password of the user
	Server calculates the answer, just like client and compares its answer
-	2 versions:
	NTLMv1: lack of mutual authentication (just client)
	NTLMv2: also authenticates server, MD5 hashed
-	NTLM is vulnerable to pass the hash attack:
	Windows caches hashed passwords in reserved memory to implement single sign on
	Hackers use malware to steal those passwords from memory
	Hackers just feed this hash into the NTLM protocol to gain entry
Kerberos:
-	Authentication protocol, developed at MIT, named after 3 headed dog
-	Default authentication method in domain model, cant be used in workgroups
-	Thought to be more secure than NTLM
-	Ticket based system, once a ticket has been issued by a DC (called KDC = key distribution center) to a client, it can be used to quickly provide authorized access to other servers on the network
-	Tickets expire after a period of time
-	To protect against replay attacks, Kerberos relies on timestamps in its tickets
-	When a server receives a request, it compares the timestamp to its local time, if the difference is too big, the authentication request is rejected. This is why time sync is important in windows domains
-	Default time skew = 5min
Time sync:
-	All computers in a windows domain use time sync
-	Done by windows time service (w32time.exe)
-	Automatically performs time sync in a windows forest
	At machine start up
	At intervals
	Using time hierarchy
Local vs domain user:
-	2 types
	Local user account:
	Are created on a member server or client
	Can only log on locally on the computer -> no DC
	Domain user account:
	Created on a domain
	Can only be used to log into domains
-	Every domain user must have a unique username. Password isn’t always required, but should be provided
User accounts storage:
-	Local account info is stored in SAM (security account manager) db of the local computer
-	System32/config/sam
-	Domain account info is stored on AD db
-	System32/ntfs.dit
-	When you setup a new DC as a first DC in a new domain, the local SAM db is migrated to AD. SAM db is made inaccessible.
SIDs:
-	All user, computer and group accounts have a SID (security identifier)
-	Used when dealing with accounts internally, granting/denying
-	Format: S-1-5-<local or domain ID>-<RID>
-	Domain admin RID = 500
GUIDs:
-	Each object in the AD has a unique 128bit GUID (globally unique identifier) to identify the object in the AD
-	Assigned to all objects
-	Reason for SIDs still existing  backwards compatibility
Password storage:
-	Stored in a file on the hard disk. Stored as hashes
-	2 kinds of hashing:
	LM hash: not very secure (uses DES); only available for backwards compatibility
	NTLM hash: more secure, no salting
Cached credentials:
-	Windows stores locally a number of domain credentials of users who have logged on to the domain from a computer
-	Let users log on when no DCs are available or gets disconnected
-	Cached credentials use salted hashes
-	Good practise to disable this feature
Name attributes of domain users:
-	Domain users have a lot of name attributes in the AD:
	Userprincipalname (UPN): preferred logon name in format username@DNSdomainname
	Distinguished name (DN): specifies location of that object in AD, consists if hierarchical path and includes domain name of each level of container
-	The DN attribute is used to access user accounts in the AD with LDAP = lightweight directory protocol
-	DN is a sequence of relative distinguished names (RDN)
User profiles:
-	User profile creates and maintains the desktop settings for each user’s work environment
-	is created for each individual when the user logs on for the first time
-	user profile settings are stored in C://users/Username
-	the profile settings are copied from:
	hidden folder C:/users/default
	the shared folder \\DCname\NETLOGON\Default (if it exists)
-	types:
	local user profile
	stored on local
	changes are specific to computer
	useful for personal computer
	Roaming user profile
	Stored on server
	Available each time you log on to a computer of the domain
	Changes are updated on the server
	Is cached by default
	Useful for users without personal computer
	Mandatory user profile
	Special form of roaming
	Changes are not updated
	Useful for kiosks
Local groups:
-	Collection of objects
-	Used to set permissions on files, shares, folder, printer…
-	Local groups can include:
	Local users
	Domain users
-	Local groups are stored in local SAM database
Domain groups:
-	Created in domain
-	Types:
	Security groups:
	Securing access to files…
	Used for mailing distribution list
	Distribution:
	Can only be used in mailing distribution
-	You can change type of group
-	Types based on scope:
	Domain local group:
	User for access resources in the domain
	From any domain in forest
	Global groups:
	Used for access to resources in the forest
	From own domain only
	Universal groups:
	Used for access to resources in the forest
	From any domain in forest
	Scope can be changed, but not all are permitted
Authorization:
-	Accomplished by using permissions and user rights
-	Permission is the auth to perform an operation on a specific object
-	User rights authorize users to perform specific actions on a computer, can be configured using group policies
-	2 types:
	Logon rights (E.g. the right to log on to the computer locally)
	Privileges (E.g. the right to back up files and folders ; the right to change system time)
-	User rights apply to user accounts and permissions attached to objects
-	Permissions are granted by an object’s owner and user rights are assigned by admin
-	In case of conflicts, privileges always override permissions
Security descriptor:
-	Main authorization attribute on the object side
-	Contains its permissions: tells the system who can do what with the object
-	Contains a list of permissions ACL, each ACL is made up of ACEs (access control entry)
Access tokens:
-	Main authorization attribute on the subject/user side
-	Includes:
	SID of user and SID of user’s security group
	A list of privileges assigned by the local security policy to the user and user’s security group
-	When a suer logs on, an access token is generated on the computer that the user logs on to
User account control (UAC):
-	Windows security feature that informs you when you want to perform a task that requires an admin level permission -> prevents potentially harmful programs from running
NTFS permissions:
-	Used to control the access that a user, group, or application has on a file or folders
-	2 kinds:
	Standard or basic permissions (5-6 permissions)
	Advanced or special permissions (13 permissions)
-	Basic permissions are logical groups of special permissions both kind can be allowed or denied
-	Some NTFS permission characteristics:
	Cumulative
	File permissions override folder permissions
	Can be inherited from parent to child
	You can have access even if you don’t have access to the parent
Permission Precedence:
-	Hierarchy of precedence for the permissions can be summarized (higher precedence = higher on list):
	Explicit deny
	Explicit allow
	Inherited deny
	Inherited allow
-	If you copy a file only the explicit carry over
Ownership:
-	User who created the file or folder, is the owner and has full control
-	To change the owner you need full control or Take ownership special permission
Other NTFS function:
-	File compression
-	File encryption (EFS) encrypting file system 
-	Quota management:
	Disk quota: applied to specific users and limit amount of disk space they can use
	Folder quota: limit amount of disk space user can use in a specific folder
-	File screening:
	Limit the type of files users can keep
-	Shadow copies of shared folders
Shared resources:
-	Resource you share over network
	Shared folders
	Shared printers
-	Access protocols for shared folders:
	SMB (server message block) default protocol on windows server
	NFS (network file system): Unix based protocol
-	Administrative shares = built-in shares
	Hidden root shares like C$, D$...
	ADMIN$ = windows system root
	NETLOGON: used by NETLOGON service
Shared folder permissions:
-	SMB permissions:
	Read
	Change
	Full control
-	Just like NTFS, cumulative
-	When a user gains access to a shared folder over the internet, the NTFS and share permissions are combined, most restrictive is applied
-	When a user gains access to a shared folder by logging on locally, only NTFS is applied
COURSE QUESTIONS:
•	Why would a company choose for Windows Servers?
	Easier setup and config  no steep learning curve
	Better technical support
	Better integration with MS software
	Most features are bundled and exist 
•	Give a difference between a Windows client OS and a Server OS.
A windows client is set for program performance, meanwhile server is set to background and service performance
•	What is the difference between LTSC and SAC?
Long term service channel is meant for stability on long term
Semi annual channel is meant for customers who want OS functionality at a faster pace
•	What different editions and installation options can you install when it comes to a Windows server?
Standard: limited virtualization
Datacenter: full virtualization
Hyperv: bare metal hypervisor
•	What is the difference between a retail, an OEM and a volume licensing?
OEM comes with a license that can’t be transferred, retail requires a separate license but can be transferred but limited. Volume is one key for multiple and is used in organizations
•	What is the Win32 API?
A windows programming Api
•	What is the WinRM?
Windows remote management
•	Give 5 examples what a company typically uses a Windows server for.
	Active directory
	DHCP server
	DNS server
	File server
	Web server
	Certificates and Authority
	Use cases:
	Application server (.NET), database server, back-up…

•	What is AD?
Active directory, used in domain controllers
•	What is an OU?
A special container type in active directories that can group objects
•	What is a DC?
A windows server assigned as domain controller
•	What is a RODC?
A read only domain controller, only accepts inbound. 
•	What are the different options to logon to a Windows machine (authenticate) when domain-joined?
NTLM and Kerberos
•	What is typically stored in an X.509 certificate (the most important things)?
It contains info and format of the certificate
•	What is a SID, a GUID and NTLM?
Security identifier (assigned to users), Global unique identifier (assigned to objects), an authentication protocol that uses challenge and response
•	What is more secure, a LM hash or an NT(LM) hash?
NTLM, LM only uses DES
•	What is LDAP and why is this interesting for developers?
Easy to access files
•	What different domain groups exist?
security, distribution, domain local, global, and universal group 
•	How do NTFS and Share permissions interact with each other?
If the file is being access through domain, it will combine the permissions and accept the strictest rules.
If it is local, then it will only apply the NTFS rules


