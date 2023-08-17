# Course Questions - Lecture 1
**What does it truly mean if people say: "computers work on 0's and 1's"?** 
* What is a "framework"?
A framework in programming is a tool that provides ready-made components or solutions that are customized in order to speed up development. A framework may include a library, but is defined by the principle of inversion of control (IoC). 
* What is a "library"? 
In computer science, a library refers to a collection of precompiled, reusable files, functions, scripts, routines, and other resources that can be referenced by computer programmers, often for software development.
* What is the difference between a compiler and an interpreter?
1. Compiler transforms code written in a high-level programming language into the machine code, at once, before program runs, 
whereas an Interpreter converts each high-level program statement, one by one, into the machine code, during 
program run.
2. Compiled code runs faster while interpreted code runs slower.
3. Compiler displays all errors after compilation, on the other hand, 
the Interpreter displays errors of each line one by one.
4. Compiler is based on translation linking-loading model which requires more memory
5. Compiler takes an entire program whereas the Interpreter takes a single line of code.
6. Interpreter takes less time to analyze the source code but overall execution time is slower
Compiler example: C & C++
Interpreter example: Python & Ruby
* What type of programming languages exist? Why are some called high- and others low-level programming languages?
High: 
1. Java
2. C#
3. C++
4. Python
5. etc
Low:
1. Assembly
2. Binary
* What is the difference between assembly code and machine code?
The main difference between machine code and assembly language is that the machine code is a language that consists of binaries that can be directly executed by a computer while an assembly language is a low-level programming language that requires a software called an assembler to convert it into machine code.
* What is disassembly in this context?
Converting assembly code into machine code(binary)
ANSWER IS NOT COMPLETE FOR THE QUESTION BELOW
* What is a PCB (in a hardware context) and how are electronics and logical gates related? 
A printed circuit board (PCB) is a board with circuits that connect electronic components together. PCB's are used in computers and other electronic devices and are made of an electrically non-conductive material, usually fibreglass.
...
**Give 5 names of different Operating Systems (flavors)**
* Which families are still common today / most used?
1. Windows 
2. MacOS
3. iOS
4. Android
5. Linux
* How old are they?
1. November 20, 1985
2. 1984
3. 2007
4. November 5, 2007
5. 1991
* What is a Linux distribution?
A Linux distribution -- often shortened to "Linux distro" -- is a version of the open source Linux operating system that is packaged with other components, such as an installation programs, management tools and additional software such as the KVM hypervisor.
**Give a definition for "Operating System" (in a classic sense and as defined in this course)**
* Do a microwave, a fridge or a classic Game Boy have operating systems? (Note: we are not talking about smart fridges or microwaves ;)
An Operating System (OS) is a software that acts as an interface between computer hardware components and the user.
A device that only translates a basic input in one action has/is no OS. If there is some sort of managing by itself or it acts as something between the user and the device (hardware) we can speak about an operating system.
* Explain the difference between virtualisation, emulation and simulation
Virtualization -> Running multiple (virtual) devices on 1 device (VMWare)
Simulation -> the process of creating a model of a system or process and using it to study and predict the behavior of the system or process under different conditions.
eg: Car driving simulators, 3D Simulators, ..
Emulation -> Emulators mimic all the hardware and software features for the production environment of a real device.
eg: BlueStacks, Android Emulators, Nintendo DS Emulators, PS4 Emulator.
* What is a mainframe?
Mainframes are computers. At their core, mainframes are high-performance computers with large amounts of memory and processors that process billions of simple calculations and transactions in real time.
* What is/are the primary goal(s) of an Operating System?
1. To be the manager/managing part of the system.
2. Functionality: 
> Booting
> Memory management
> Loading & Execution
> Data security
> Disk/device management (in general – hardware management)
> Process management
> “Concurrency”-problems in databases are also present here => Information systems
3. Manage interruptions
> Hi there is this issue here. What do you as user want to do with it? -> Communication 
**Why is there a new way of looking at "Operating Systems" (in a cloud / micro service / more modern sense)?**
The answer
**Explain the difference between User space and Kernel space.**
Kernel has complete control and handles (almost) everything
Kernelspace = system mode – priviliged mode – supervisor mode – secure mode – unrestricted mode 
Userspace = ordinary mode – user mode – restricted mode 
**What are system calls?**
A function in C
In simple terms, a system call is a request made by a program to the operating system to perform a specific function or service. System calls allow programs to request access to system resources, such as input/output operations, memory allocation, and access to system hardware and peripherals. They are an essential part of the operating system and provide a way for programs to interact with the underlying hardware and operating system. System calls are usually made using a special function or instruction in the program code, and they are typically implemented in the kernel, which is the core of the operating system.
**What are drivers?**
In simple terms, drivers are software programs that enable communication between a computer and a device. They allow the operating system and other software on the computer to access and control the device. Drivers are typically specific to a particular device, such as a printer, a graphics card, or a network adapter, and are designed to work with the operating system of the computer. Without drivers, the computer would not be able to use the device or take advantage of its features. Drivers are an important part of how computers and devices interact and are an essential component of the overall functioning of a computer system.
**General Computer History (up to present day)**
* What made Pascal so special ?
The answer
* Why are people like Charles Babbage and Ada Lovelace so critical in the evolution of (modern) computers ?
Charles Babbage and Ada Lovelace are considered important figures in the history of computing because of their contributions to the development of the first mechanical computers. Babbage is credited with designing the first mechanical computer, known as the Difference Engine, which was intended to calculate and print tables of mathematical functions. Lovelace, who was a friend of Babbage and an accomplished mathematician in her own right, is known for her work on the Analytical Engine, a more advanced mechanical computer that Babbage designed but never built.
Lovelace is often referred to as the world's first computer programmer because of her work on the Analytical Engine. She wrote the first published algorithm intended to be processed by a machine, and her work laid the foundations for the development of modern computer programming. Lovelace and Babbage's contributions were critical to the evolution of modern computers because they demonstrated the feasibility of building mechanical devices that could perform complex calculations and laid the foundations for the development of more advanced computers in the future.
* Was there ever such a thing as a non-electronic computer ?
Yes, there have been non-electronic computers in the past. Before the development of electronic computers, mechanical computers were the primary type of computer in use. These computers were designed to perform calculations using mechanical devices, such as gears and levers, rather than electronic components. Some examples of early mechanical computers include the abacus, which was used for simple arithmetic calculations, and the mechanical calculators that were developed in the 19th and early 20th centuries.
Mechanical computers were used for a variety of purposes, including calculating and printing tables of mathematical functions, performing scientific calculations, and helping to solve complex problems in fields such as engineering and finance. While they were not as fast or powerful as modern electronic computers, mechanical computers played a critical role in the development of modern computing and laid the foundations for the development of more advanced computers in the future.
* How did Alan Turing win the war ?
He is particularly known for his work on the Enigma machine, a device used by the Germans to encode their messages. Turing and his team at Bletchley Park developed techniques for cracking the Enigma code and were able to intercept and decode a large number of German messages, providing the Allies with valuable intelligence about enemy plans and operations.
Because of this he had a strategic advantage by knowing the enemy's plans and movements.
* Which functions does a punch card have for a computer ?
The answer
* What do we mean when we talk about the Von Neumann bottleneck ?
The Von Neumann bottleneck is a concept in computer science that refers to the limited speed at which a computer can access and process data stored in its memory. This bottleneck is named after John von Neumann, a pioneer in computer science and one of the key figures in the development of modern computers.
The Von Neumann bottleneck occurs because computers have two main types of memory: random access memory (RAM) and storage memory (such as a hard drive). RAM is used to store data and instructions that the computer is currently working on, while storage memory is used to store data that the computer needs to access less frequently.
The problem is that the speed at which the computer can access and process data in RAM is much faster than the speed at which it can access data in storage memory. This means that if the computer needs to access data that is stored in storage memory, it has to first transfer the data to RAM, which takes time and slows down the computer's overall processing speed.
The Von Neumann bottleneck can be mitigated by using faster memory technologies or by optimizing the way in which data is accessed and processed. However, it is a fundamental limitation of computers that has not been completely eliminated.
* How does Moore's Law impact your cost of digital living ?
The number of transistors on a microchip would double approximately every two years, leading to exponential increases in computing power and decreases in the cost of computing over time.
**A Matter of Unix**
* Why was Unix made at all ?
The goal of the Unix project was to create an operating system that was more efficient, reliable, and flexible than the ones that were available at the time. To achieve this, the team designed Unix to be a modular system, with a small kernel that handled the basic functions of the operating system and a set of user programs that could be added or removed as needed. This made it easy to customize the system to meet the specific needs of different users and applications.
In addition to its modular design, Unix was also notable for its use of a high-level programming language (C) to implement the operating system and its utilities, which made it easier to develop and maintain. These features, along with its portability (it could run on a wide range of hardware platforms), made Unix popular with developers and researchers, and it eventually became the foundation for many other operating systems.
* Why was Dennis Ritchie a crucial element in the evolution of the computer ?
He was a member of the team led by Ken Thompson that developed the Unix operating system and was instrumental in developing the C programming language, which was used to implement much of the operating system. He was one of the creators of C
* Who was Ken Thompson ?
Thompson is best known for his work on Unix, a popular and influential operating system that was developed in the 1970s at Bell Labs, where Thompson worked as a researcher. He co-authored the Unix operating system with Dennis Ritchie, and was also involved in the development of the C programming language. He was also part of the development of the B programming language and the design of the UNIX File System (UFS). Thompson is also a Fellow of the Association for Computing Machinery (ACM) and the Institute of Electrical and Electronics Engineers (IEEE).
* What was the role of the evolution of B & C in the creation of Unix and subsequent Operating Systems ?
The B programming language and the C programming language played a significant role in the development of the Unix operating system. B was a high-level programming language developed by Thompson in the early 1970s, and it was used to write the first version of Unix. However, B had some limitations and was not well-suited for writing large programs, so Thompson and Ritchie decided to develop a new programming language called C that would be more efficient and flexible.
C was a significant improvement over B, and it became the primary programming language used to develop Unix. C was designed to be a portable language, which meant that it could be used to write programs that could be easily compiled and run on different types of computers. This made it a popular choice for developing operating systems and other software.
The use of C in the development of Unix had a lasting impact on the field of computer science, as C became widely used in the development of other operating systems and software. Many other programming languages, such as C++ and C#, were also influenced by C and are based on its syntax and design principles. C remains a popular programming language to this day, and it is used in a wide variety of applications.
* What are the core principles of the Unix Philosophy ?
1. Make each program do one thing well. To do a new job, build a fresh rather than complicate old programs by adding new "features".
2. Expect the output of every program to become the input to another, as yet unknown, program. Don't clutter output with extraneous information. Avoid stringently columnar or binary input formats. Don't insist on interactive input.
3. Design and build software, even operating systems, to be tried early, ideally within weeks. Don't hesitate to throw away the clumsy parts and rebuild them
4. Use tools in preference to unskilled help to lighten a programming task, even if you have to detour to build the tools and expect to throw some of them out after you've finished using them
* Why is worse (sometimes) better in modern operating systems ?
The answer
PWP: 44
* Sketch the three main family lines that evolved from Unix
Red Hat, Debian & Slackware Linux
* What is POSIX ?
In simple terms, POSIX (short for Portable Operating System Interface) is a set of standards that define how software should interact with operating systems. The goal of POSIX is to make it easier for software developers to write programs that can run on multiple types of operating systems, including Unix, Linux, and other Unix-like systems.
1.The POSIX standard for operating system interfaces, which defines a common set of functions and libraries that all POSIX-compliant operating systems should support.
2. The POSIX standard for shells and utilities, which defines a set of command-line tools and utilities that should be available on all POSIX-compliant systems.
3. The POSIX standard for threads, which defines a set of functions and libraries for creating and managing threads (small units of execution within a process).
Overall, the goal of POSIX is to provide a consistent, portable interface for software developers, so that they can write programs that can run on any POSIX-compliant operating system with minimal modification.
* What is UTF 32-16-8 ?
UTF-8 is a variable-width encoding that can represent any Unicode character in one to four 8-bit bytes. It is widely used on the web and in email because it is compact and can be used with ASCII, which is the most widely used character encoding standard for the English alphabet.
UTF-16 is a fixed-width encoding that represents each Unicode character in two 16-bit words (also known as a "code unit"). It is used in many modern operating systems and programming languages.
UTF-32 is a fixed-width encoding that represents each Unicode character in four 32-bit words (also known as a "code point"). It is not as widely used as UTF-8 or UTF-16 because it requires more storage space, but it is often used when performance is not a concern and a simple, fixed-width encoding is desired.
In summary, UTF-8, UTF-16, and UTF-32 are all Unicode character encoding standards that represent the same set of characters, but they use different numbers of bits per character and have different storage and performance characteristics.
* What's GNU ?
> GNU’s not unix.
> Richard Stallman
> Create a free software Unix-like
> Free to run a program for any purpose
> Freedom to study the mechanics of the program and modify it
> Freedom to redistribute copies
> freedom to improve and change modified versions for public use
> Rewrite “unix” to the highest standardization
> Linus Torvalds made the first kernel using + supporting GNU
> (GNU)LINUX !!
> 1991
> OPEN SOURCE OS
* What is a distro ?
A distro is short for distribution, and it refers to a version of a operating system that has been packaged and made available for users to install and use.
A distro typically includes the operating system kernel, as well as a range of software applications and utilities that are commonly used on the operating system. The software applications and utilities included in a distro can vary depending on the intended use of the operating system and the goals of the distro maintainers.
There are many different distros available for a variety of operating systems, including Linux, Unix, and other open source and proprietary operating systems. Some well-known examples of Linux distros include Ubuntu, Debian, and Fedora. Each of these distros has its own unique features and characteristics, and users can choose the distro that best meets their needs and preferences.
Distros are often used by individuals and organizations as a way to easily install and set up a complete operating system that includes a range of software applications and utilities. They can also be customized and modified to meet the specific needs of users and organizations.
* How do you find out wich distros are most used and why would you want to know ?
1. To find a distro that is popular and well-supported: you might want to start with a distro that is widely used and has a large user base.
2.To learn about new features and technologies: By keeping track of the most popular distros, you can learn about new features and technologies that are being developed and adopted by a large number of users.
3. To see how different distros compare: By comparing the popularity of different distros, you can get a sense of how they compare in terms of features, performance, and other characteristics. This can be helpful if you're trying to decide which distro is the best fit for your needs.
