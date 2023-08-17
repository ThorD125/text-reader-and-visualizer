# Course Questions - Lecture 3
**Chapter 1**
* Terminology: What is the difference between a process and a binary/executable?
binary/executable
* passive
* has no state
* program code
* (= is not running)
---
process
* active
* has a state
* program code + program counter + stack + data section + heap + …
* In the context of a process, what is "the stack" and what is "the heap"?
The Answer
* What parts of a process are on the stack?
The Answer
* What parts of a process are on the heap?
The Answer
* Given some code, know what is on the stack and know what is on the heap.
The Answer
* List all different process states in a diagram. Can every state go to every other state?
No.
New, running, waiting, ready, terminated.
* What is a process control block?
A process control block (PCB) is a data structure in an operating system that stores information about a specific process or task. It is used by the operating system to manage and keep track of the process as it executes. The information stored in a PCB includes the process identifier (PID), status of the process (e.g., running, waiting, blocked), priority level, memory usage, and other relevant data.
* What is meant with "context switch" in the context of processes.
Saving/storing the state of a process (or thread) 
-> As a result a single CPU can allow multiple processes -> multitasking operating system!
* Why are pointers so important in low level programming?
Pointers are an important tool in low-level programming because they give the programmer a high degree of control over how memory is used and accessed in the program.
* What is Big-O?
Big-O notation is a way of expressing the complexity of an algorithm in terms of the amount of resources (such as time or memory) it consumes. It provides a high-level measure of the efficiency of an algorithm, which can be useful for comparing the performance of different algorithms or for predicting the scalability of a particular algorithm as the size of the input data grows.
* What is the difference between pass by value and pass by reference programming languages?
Pass by value
