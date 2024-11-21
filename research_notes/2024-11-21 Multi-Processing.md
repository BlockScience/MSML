# Multi-Processing Research

## Executive Summary

- The following research note deals with research into what multi-processing paradigms exist in Python and which ones might serve MSML and cadCAD the best

## Past Exploration

- There has been use of `Ray` in the past in the fork of cadCAD called radCAD
- `Ray` shares the same underlying api at the `multiprocessing` module but can be distributed and scaled
- In the past, we have struggled with the time taken for pickling and unpickling which has hurt performance time
- The `multiprocessing` is currently used but is running very slow when there are simulations with large data structures

## Primary Objectives of Multi-Processing

- Provide a way to parallelize simulations
- Speed up the simulation process significantly
- Provide a simple interface to use and debug

## Secondary Objectives

- Allow for ease of debugging simulations
- Allow for distribution to multiple machines automatically
- Easily support cloud runs of the multi-processing

## High Level Options

1. **`multiprocessing` Module**: Python's built in module which creates separate processes to be run on different CPU cores
2. **`concurrent.futures.ProcessPoolExecutor`**: A higher-level API for managing process pools, however, it has less fine-grained control and also the same overhead as `multiprocessing` so we will not explore more
3. **`joblib`**: A library optimized for parallelism, commonly used in data science and machine learning, but it is more geared towards python/numpy objects so we will ignore for this exploration
4. **`dask`**: A parallel computing library for dynamic task scheduling, which while more complex, can be better for scalability
5. **`Ray`**: A flexible, distributed framework for parallel and distributed Python applications which does come with a steeper learning curve
6. **`subprocess` Module**: Used for running external processes, however it spawns shell processes so we will ignore for this exploration as it might get too complicated
7. **`Celery`**: A distributed task queue library with support for parallel task execution, however it requires a message broker which likely makes it overkill for use in simple location simulations


## Candidate 1: **`multiprocessing` Module**

- Python's built in module for multi-processing
- Separate processes are created that can run on different CPU cores, avoiding Python's Global Interpreter Lock (GIL).
- Process-based parallelism.
- Allows sharing data using `Queue`, `Pipe`, `Value`, and `Array`.

- **Strengths**:
  - True parallelism across multiple CPU cores.
  - Easy to use, with a simple API similar to `threading`.
  - Built into Python, no external dependencies.
  - Supports shared memory with `multiprocessing.Array` or `multiprocessing.Value`
  - Well-documented and widely supported

- **Weaknesses**:
  - Higher memory overhead because each process has its own memory space.
  - Inter-process communication (IPC) can be slower than in-thread communication.
  - Starting processes can have higher latency compared to threads.
  - Limited support for handling large datasets due to pickling/unpickling overhead
  - Debugging is harder compared to single-threaded solutions

## Candidate 2: **`dask`**

- A parallel computing library for dynamic task scheduling.
- Scales from a single machine to a distributed cluster, with support for task-based and data parallelism.
- Handles both in-memory computation and out-of-core processing for large datasets.
- Integrates well with pandas, numpy, and scikit-learn.

- **Strengths**:
  - Great for big data tasks.
  - Scalable from single-core to distributed systems.
  - Can handle complex, directed acyclic graphs (DAGs) for computations.

- **Weaknesses**:
  - More complex than other options for simple tasks.
  - Requires additional setup for distributed usage.


## Candidate 3: **`Ray`**

- A flexible, distributed framework for parallel and distributed Python applications.
- Provides parallelism across CPUs and GPUs, making it suitable for machine learning and AI workloads.
- Supports actors, tasks, and scalable scheduling.
- Integrates with TensorFlow, PyTorch, etc.

- **Strengths**:
  - Highly scalable for advanced workloads.
  - Supports a wide variety of computational patterns.
  - Simple API for parallel and distributed execution.
  - Built-in tools for handling failures, scheduling, and monitoring.
  - Integrates well with machine learning frameworks like PyTorch and TensorFlow.


- **Weaknesses**:
  - Steeper learning curve for beginners.
  - Heavier dependency and setup.
  - Overkill for simple simulations on a single machine.

## Objectives Comparison Table

| **Approach**                 | **Parallelism** | **Ease of Use** | **Performance Overhead** | **Debugging Ease** | **Scaling Across Machines Ease** | **Cloud Integration** |
|------------------------------|-----------------|-----------------|--------------------------|--------------------------|--------------------------|--------------------------|
| `multiprocessing`            | High            | Moderate        | High                    | High | Low | Low |
| `dask`                       | High            | Low to Moderate        | Moderate to High        | Moderate | Moderate to High | Moderate |
| `Ray`                        | High            | Low to Moderate        | Moderate to High        | Low to Moderate | High | High |


## Conclusion & Next Steps

- All three are potential solutons but really we can break it down into higher ease of use without scalability for using `multiprocessing` vs. higher scalability and power with `dask` / `Ray` if we are willing to put more effort in
- It might be prudent to try all three solutions with MSML and clock performance time on a test case so that we can compare local machine performance and also get an idea of how hard it would be to set up workflows with any of these

## Appendix

### ChatGPT Response 1

- Question: If I want to run multi-processing in python what options do I have and what are the costs and benefits?

Running multi-processing in Python can be achieved through several approaches, each with its own trade-offs. Here's an overview of the most common options:

---

#### 1. **`multiprocessing` Module**
This is Python's built-in module for multi-processing.

- **How It Works**: It creates separate processes that can run on different CPU cores, avoiding Python's Global Interpreter Lock (GIL).
  
- **Key Features**:
  - Process-based parallelism.
  - Allows sharing data using `Queue`, `Pipe`, `Value`, and `Array`.

- **Pros**:
  - True parallelism across multiple CPU cores.
  - Easy to use, with a simple API similar to `threading`.
  - Built into Python, no external dependencies.

- **Cons**:
  - Higher memory overhead because each process has its own memory space.
  - Inter-process communication (IPC) can be slower than in-thread communication.
  - Starting processes can have higher latency compared to threads.

---

#### 2. **`concurrent.futures.ProcessPoolExecutor`**
A higher-level API for managing process pools.

- **How It Works**: Manages a pool of worker processes to which tasks can be submitted.

- **Key Features**:
  - Simpler and more intuitive than `multiprocessing`.
  - Automatically handles the process pool.

- **Pros**:
  - Cleaner and more Pythonic syntax.
  - Good for task-based parallelism.
  - Built-in support for asynchronous execution with `Future` objects.

- **Cons**:
  - Less fine-grained control compared to `multiprocessing`.
  - Similar overhead as `multiprocessing`.

---

#### 3. **`joblib`**
A library optimized for parallelism, commonly used in data science and machine learning.

- **How It Works**: Provides easy parallelism for loops or functions, leveraging multiprocessing under the hood.

- **Key Features**:
  - Specially optimized for numpy/pandas objects.
  - Includes utilities like `Parallel` and `delayed`.

- **Pros**:
  - Simple to parallelize loops.
  - Efficient for numerical computations.

- **Cons**:
  - Limited to task-level parallelism.
  - Slightly less flexible than `multiprocessing` for complex workflows.

---

#### 4. **`dask`**
A parallel computing library for dynamic task scheduling.

- **How It Works**: Scales from a single machine to a distributed cluster, with support for task-based and data parallelism.

- **Key Features**:
  - Handles both in-memory computation and out-of-core processing for large datasets.
  - Integrates well with pandas, numpy, and scikit-learn.

- **Pros**:
  - Great for big data tasks.
  - Scalable from single-core to distributed systems.

- **Cons**:
  - More complex than other options for simple tasks.
  - Requires additional setup for distributed usage.

---

#### 5. **`Ray`**
A flexible, distributed framework for parallel and distributed Python applications.

- **How It Works**: Provides parallelism across CPUs and GPUs, making it suitable for machine learning and AI workloads.

- **Key Features**:
  - Supports actors, tasks, and scalable scheduling.
  - Integrates with TensorFlow, PyTorch, etc.

- **Pros**:
  - Highly scalable for advanced workloads.
  - Supports a wide variety of computational patterns.

- **Cons**:
  - Steeper learning curve for beginners.
  - Heavier dependency and setup.

---

#### 6. **`subprocess` Module**
Used for running external processes.

- **How It Works**: Spawns new processes to execute shell commands or external scripts.

- **Key Features**:
  - Not specifically designed for parallelism but can be adapted.

- **Pros**:
  - Useful for interacting with system-level processes.
  - Works well for external command execution.

- **Cons**:
  - Limited flexibility for Python parallelism.
  - Does not natively handle shared data or inter-process communication.

---

#### Key Costs and Benefits

| **Approach**                 | **Parallelism** | **Ease of Use** | **Performance Overhead** | **Best For**                              |
|------------------------------|-----------------|-----------------|--------------------------|------------------------------------------|
| `multiprocessing`            | High            | Moderate        | High                    | CPU-bound tasks                          |
| `ProcessPoolExecutor`        | High            | High            | High                    | Task-based parallelism                   |
| `joblib`                     | Medium          | High            | Moderate                | Numerical tasks and ML workflows         |
| `dask`                       | High            | Moderate        | Moderate to High        | Big data, scalable workflows             |
| `Ray`                        | High            | Moderate        | Moderate to High        | Scalable, distributed computing          |
| `subprocess`                 | Low             | Low             | High                    | System-level or external commands        |

---

#### Choosing the Right Tool
1. **Simple Parallelism**: Use `multiprocessing` or `ProcessPoolExecutor`.
2. **Data Science & ML**: Use `joblib` or `dask`.
3. **Scalable Systems**: Use `dask` or `Ray`.
4. **Interacting with System**: Use `subprocess`.


### ChatGPT Response 2

- Question: I am trying to build a simulation library in python and want to use multi-processing to run simulations in parallel? What are some options that are best for simulations and the strengths and weaknesses of each?

When building a simulation library in Python and leveraging multiprocessing for parallel simulations, there are several options you can consider. Here’s an overview of the most relevant approaches, along with their strengths and weaknesses:

---

#### 1. **Python's `multiprocessing` Module**
The `multiprocessing` module is built into Python and provides an easy way to spawn processes.

- **Strengths:**
  - Simple API for creating parallel processes (`Pool`, `Process`, etc.).
  - Can bypass Python's Global Interpreter Lock (GIL), allowing true parallelism on multi-core CPUs.
  - Supports shared memory with `multiprocessing.Array` or `multiprocessing.Value`.
  - Well-documented and widely supported.

- **Weaknesses:**
  - Overhead from process creation and inter-process communication (IPC).
  - Limited support for handling large datasets due to pickling/unpickling overhead.
  - Debugging is harder compared to single-threaded solutions.

---

#### 2. **`concurrent.futures` Module**
This module provides a high-level interface for managing threads and processes.

- **Strengths:**
  - High-level and simple API (e.g., `ProcessPoolExecutor`).
  - Good for tasks that can be split into independent, parallel chunks.
  - Easier to switch between threads and processes.

- **Weaknesses:**
  - Less fine-grained control compared to `multiprocessing`.
  - Still subject to process creation overhead when using `ProcessPoolExecutor`.

---

#### 3. **`joblib` Library**
`joblib` is often used in the scientific computing community for parallel processing.

- **Strengths:**
  - Optimized for memory sharing between workers (e.g., for numpy arrays).
  - Simple API for parallel loops (`Parallel` and `delayed`).
  - Good integration with scikit-learn.

- **Weaknesses:**
  - Less control over low-level multiprocessing.
  - Limited debugging tools.

---

#### 4. **`Ray` Library**
Ray is a distributed computing framework designed for scaling Python applications.

- **Strengths:**
  - Highly scalable for distributed systems and clusters.
  - Simple API for parallel and distributed execution.
  - Built-in tools for handling failures, scheduling, and monitoring.
  - Integrates well with machine learning frameworks like PyTorch and TensorFlow.

- **Weaknesses:**
  - Higher learning curve for distributed setups.
  - More complex dependencies.
  - Overkill for simple simulations on a single machine.

---

#### 5. **`Dask` Library**
Dask is a parallel computing library that integrates seamlessly with Pandas and NumPy.

- **Strengths:**
  - Can handle complex, directed acyclic graphs (DAGs) for computations.
  - Suitable for scaling from single machines to clusters.
  - Excellent for data-intensive simulations.

- **Weaknesses:**
  - Higher memory overhead compared to simpler libraries.
  - Configuration and setup for clusters can be challenging.

---

#### 6. **`Celery`**
A distributed task queue library with support for parallel task execution.

- **Strengths:**
  - Well-suited for workflows with task dependencies and asynchronous tasks.
  - Can scale across multiple machines.
  - Robust ecosystem with many extensions.

- **Weaknesses:**
  - Overkill for standalone simulations.
  - Requires a message broker like RabbitMQ or Redis.

---

#### Recommendations for Simulation Libraries
- **For small-scale, simple simulations:** Use `multiprocessing` or `concurrent.futures`.
- **For larger simulations needing shared memory:** Try `joblib` for its efficient memory handling.
- **For distributed or scalable solutions:** Explore `Ray` or `Dask`.
- **For task pipelines with complex dependencies:** Use `Celery` if task orchestration is a priority.