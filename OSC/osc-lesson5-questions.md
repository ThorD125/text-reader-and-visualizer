# Course Questions - Lecture 5
**Chapter 1**
* What are the differences between processes and threads?
A process is an instance of a program that is being executed by a computer. It is a self-contained execution environment and can be thought of as a "virtual" computer within a computer. A process has its own memory space and resources, and it runs independently of other processes.
A thread is a lightweight process that can be created within a process. It shares the process's memory and resources, and it can be scheduled by the operating system to run concurrently with other threads within the same process or on different processors.
In general, processes are heavier and more resource-intensive than threads, and they are typically used to run independent programs or tasks. Threads, on the other hand, are used to divide a program into smaller, concurrent units of execution that can run in parallel and make better use of multi-core processors.
There are several differences between processes and threads:
Scheduling: Processes are typically scheduled by the operating system to run on a single processor or a set of processors, while threads are scheduled to run concurrently on a single processor or a set of processors.
Memory: Processes have their own memory space and resources, while threads share the memory and resources of their parent process.
Communication: Processes typically communicate with each other through inter-process communication (IPC) mechanisms such as pipes, sockets, or message queues, while threads can communicate with each other through shared memory or by using synchronization mechanisms such as mutexes and semaphores.
Context switching: Context switching between processes is typically more expensive than context switching between threads, because it involves switching between different memory spaces and resources.
* What are the similarities between processes and threads?
Both processes and threads are units of execution that can be scheduled by the operating system to run concurrently on a single processor or a set of processors. They both have a program counter, a stack, and a set of registers that store the current state of the execution. They also both have an associated priority level that determines their order of execution.
Both processes and threads can create and terminate new processes and threads, and they can communicate with other processes and threads through various inter-process communication (IPC) mechanisms.
Both processes and threads can also be preempted by the operating system and moved to a waiting state if they are blocked on a resource or if a higher-priority process or thread becomes ready to run.
In general, processes and threads are similar in that they are both units of execution that can run concurrently within a computer system, and they both have a set of resources and a priority level that determine their execution order.
They both have:
- a Thread ID
- a program counter
- a stack
- a set of registers 
* What are the benefits of threads?
Powerpoint: 
- Responsiveness
- Resource sharing
- Economy (it is less costly to manage threads then process)
- Scalability
ChatGPT:
Threads are a way for a program to split itself into two or more concurrently running tasks. There are several benefits to using threads:
Improved performance: By using threads, a program can run multiple tasks concurrently, which can improve its overall performance. For example, if a program has a task that takes a long time to run, it can use a thread to run that task in the background while continuing to run other tasks in the foreground.
Responsiveness: Threads can be used to keep a program responsive to user input. For example, if a program has a task that takes a long time to run, it can use a thread to run that task in the background while continuing to accept user input.
Resource sharing: Threads can share resources such as memory and file handles, which can make it easier to write programs that use shared resources.
Simplicity: Using threads can simplify the design of a program, since it allows the program to perform multiple tasks concurrently within a single process. This can be easier to understand and maintain than using multiple processes to achieve the same result.
It's worth noting that using threads can also introduce some complexity, since you need to consider issues such as synchronization and race conditions. However, in many cases, the benefits of using threads outweigh the additional complexity.
* Give an example of a downside of using threads in an application?
Powerpoint:
- Programming (harder to write, harder to debug, harder to manage)
- Concurrency issues with shared resources
    - Similar problems with transactions in databases! 
        - Dirty read
        - Loss update
        - Phantom read
        - It is never set in stone that a “Java thread” is always mapped to an “OS thread”.
    - You have to trust the libraries/frameworks or write everything yourself if you want that.
    - Luckily we rarely have to worry about that as a programmer 
    - -> User and kernel threads
    
ChatGPT: 
One downside of using threads is that they can introduce complexity to a program, since you need to consider issues such as synchronization and race conditions. Synchronization is the process of coordinating access to shared resources in a multi-threaded program to prevent race conditions, which can occur when two or more threads try to access the same resource simultaneously. Race conditions can lead to unpredictable behavior and even program crashes.
Another potential downside of using threads is that they can consume additional system resources, such as memory and CPU time. This can impact the overall performance of a program, especially if the program creates a large number of threads or if the threads are not used efficiently.
Finally, debugging a program that uses threads can be more challenging, since it can be difficult to determine the root cause of errors that occur in multiple threads simultaneously.
Overall, it's important to carefully consider whether the benefits of using threads outweigh the additional complexity and potential performance impact they can introduce.
* What is function of the systemcall fork?
Fork -> System call that creates a new child process
* Is a childprocess the same as a thread?
No, a child process is not the same as a thread.
A child process is a separate process that is created by another process (the parent process). Child processes are created using system functions such as fork() in Unix-like operating systems or CreateProcess() in Windows.
A thread, on the other hand, is a separate execution path within a single process. A process can contain multiple threads, which can run concurrently and share resources such as memory and file handles.
Both child processes and threads can be used to run multiple tasks concurrently, but they differ in how they are implemented and managed. Child processes have their own memory space and resources, and are typically used to run tasks that are independent of the parent process. Threads, on the other hand, share memory and resources with the parent process, and are typically used to run tasks that are closely related to the parent process.
* Can a child process live without its parent?
Yes, a child process can continue to run even if its parent process has terminated. In most operating systems, when a parent process creates a child process, the child process is created with a separate memory space and resources, and it is treated as an independent process. This means that the child process can continue to run and execute its own instructions even if the parent process has ended.
However, it is important to note that the child process is typically created and managed by the parent process, and the parent process may play a role in determining when the child process ends. For example, the parent process may send a signal to the child process to terminate, or the parent process may wait for the child process to complete before continuing its own execution.
* Can a thread live on its own?
In the context of computer programming, a thread is a separate flow of execution within a program. A thread is sometimes referred to as a lightweight process, as it shares some of the same properties as a process, but it requires fewer system resources to create and manage.
A thread can execute on its own, meaning that it can perform tasks and execute code independently of other threads within the same program. However, threads are usually created and managed by the operating system, and they are typically associated with a specific process or application.
In general, a thread cannot exist on its own outside of a process or application. It is a unit of execution within a larger program, and it relies on the resources and infrastructure provided by the operating system and the process or application in which it is running.
* How can you protect a (critical) piece of code? Give the name of 2 examples. 1 is more a locking mechanism and the other a signaling mechanism.
Semaphores and mutexes are types of locking mechanisms that can be used to protect a critical piece of code in a multithreaded environment.
A semaphore is a synchronization object that controls access to a shared resource by allowing a certain number of threads to access the resource at the same time. A semaphore can be binary (allowing either 0 or 1 threads to access the resource at a time) or counting (allowing a specific number of threads to access the resource at a time). To access the resource, a thread must acquire a semaphore by decrementing its value. If the semaphore's value is already 0, the thread will block until the semaphore becomes available. When the thread is finished with the resource, it must release the semaphore by incrementing its value.
A mutex (short for mutual exclusion) is similar to a semaphore, but it is typically used to protect a smaller, more critical section of code. A mutex can only be acquired by one thread at a time, and any other threads that try to acquire the mutex will be blocked until it is released. To protect a critical piece of code using a mutex, a thread would acquire the mutex before executing the code and release it afterwards.
Here is an example of using a semaphore to protect a critical piece of code in C:
Copy code
sem_t sem;
void func() {
  sem_wait(&sem);  // acquire the semaphore
  // critical section of code goes here
  sem_post(&sem);  // release the semaphore
}
And here is an example of using a mutex to protect a critical piece of code in C:
Copy code
pthread_mutex_t mutex;
void func() {
  pthread_mutex_lock(&mutex);  // acquire the mutex
  // critical section of code goes here
  pthread_mutex_unlock(&mutex);  // release the mutex
}
