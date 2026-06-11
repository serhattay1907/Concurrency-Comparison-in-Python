# Concurrency Comparison in Python 🔄

A comprehensive exploration of **threading vs multiprocessing** in Python, demonstrating performance differences between CPU-bound and I/O-bound tasks.

## 📌 Overview

This project compares different concurrency approaches in Python by implementing real-world examples:
- **CPU-Bound Tasks**: SIR Epidemiological Model Simulation
- **I/O-Bound Tasks**: File Read & Write Operations

The goal is to understand when to use **Threads** and when to use **Multiprocessing** for optimal performance.

---

## 📁 Project Structure

```
Concurrency Comparison in Python/
│
├── SIR Model Testing/
│   ├── 1-CPU_BOUND_PROCESSES.py      (Multiprocessing approach)
│   └── 2-CPU_BOUND_THREADS_1.py      (Threading approach)
│
└── File Read&Write Test/
    ├── 3-IO_BOUND_PROCESSES_2.py     (Multiprocessing approach)
    └── 4-IO_BOUND_THREADS_1.py       (Threading approach)
```

---

## 🚀 Quick Start

### Prerequisites
```bash
python 3.8+
```

### Run Examples

**CPU-Bound (SIR Model):**
```bash
cd "SIR Model Testing"

# Compare performance
python 1-CPU_BOUND_PROCESSES.py
python 2-CPU_BOUND_THREADS_1.py
```

**I/O-Bound (File Operations):**
```bash
cd "File Read&Write Test"

# Compare performance
python 3-IO_BOUND_PROCESSES_2.py
python 4-IO_BOUND_THREADS_1.py
```

---

## 📊 Concurrency Concepts

### **What's the Difference?**

| Feature | Threads | Multiprocessing |
|---------|---------|-----------------|
| **CPU-Bound** | 🐢 Slow (GIL blocks) | ⚡ Fast |
| **I/O-Bound** | ⚡ Fast | 🐢 Slower (overhead) |
| **Memory** | Low | High |
| **Context Switch** | Fast | Slower |
| **GIL Impact** | Yes ❌ | No ✅ |

### **GIL (Global Interpreter Lock)**
Python's GIL prevents true parallelism in threads for CPU-bound tasks. Multiprocessing bypasses this by using separate processes.

---

## 🧪 Project Details

### 1️⃣ **SIR Model Testing** (CPU-Bound)

**What is SIR Model?**
- Susceptible → Infected → Recovered epidemiological model
- Heavy mathematical computations
- **Perfect for demonstrating multiprocessing benefits**

**Files:**
- `1-CPU_BOUND_PROCESSES.py` - Uses multiprocessing
- `2-CPU_BOUND_THREADS_1.py` - Uses threading

**Expected Results:**
```
Multiprocessing: ~0.5-1.0 seconds
Threading:       ~3-5 seconds (much slower)
```

**Why?** CPU-bound tasks can't release the GIL, so threading is inefficient.

---

### 2️⃣ **File Read&Write Test** (I/O-Bound)

**What is I/O-Bound?**
- File operations (read/write)
- Network requests
- Database queries
- **Perfect for demonstrating threading benefits**

**Files:**
- `3-IO_BOUND_PROCESSES_2.py` - Uses multiprocessing
- `4-IO_BOUND_THREADS_1.py` - Uses threading

**Expected Results:**
```
Threading:        ~0.01-0.05 seconds (faster)
Multiprocessing:  ~0.5-1.0 seconds (slower)
```

**Why?** During I/O waits, threads can switch to other tasks efficiently without multiprocessing overhead.

---

## 📈 Performance Comparison

```
┌─────────────────────────────────────────┐
│   CPU-Bound (SIR Model)                 │
├─────────────────────────────────────────┤
│ Multiprocessing: ████████ FAST          │
│ Threading:       ████████████ SLOW      │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│   I/O-Bound (File Operations)           │
├─────────────────────────────────────────┤
│ Threading:       ████ FAST              │
│ Multiprocessing: ████████ SLOWER        │
└─────────────────────────────────────────┘
```

---

## 🎓 Key Learnings

✅ **Use Multiprocessing when:**
- CPU-intensive computations
- Heavy mathematical operations
- Need true parallelism

✅ **Use Threading when:**
- I/O operations (files, network)
- Many concurrent tasks
- Low overhead needed
- Shared memory required

⚠️ **Avoid Threading for:**
- CPU-bound tasks (GIL blocks parallel execution)

⚠️ **Avoid Multiprocessing for:**
- I/O operations (unnecessary overhead)
- Need fast context switching

---

## 🔬 How to Analyze Results

Run both versions and compare timing:

```python
# Look for this in output:
print(f"Total time: {end_time - start_time:.4f} seconds")
```

**Expected observations:**
1. CPU-bound: Multiprocessing significantly faster
2. I/O-bound: Threading slightly faster
3. Memory usage: Multiprocessing uses more RAM

---

## 📚 Resources

- [Python Concurrency Documentation](https://docs.python.org/3/library/concurrency.html)
- [Understanding Python's GIL](https://realpython.com/python-gil/)
- [threading Module](https://docs.python.org/3/library/threading.html)
- [multiprocessing Module](https://docs.python.org/3/library/multiprocessing.html)
- [Real Python: Concurrency](https://realpython.com/intro-to-python-threading/)

---

## 🛠️ Modifications & Extensions

**Try These:**
- Increase `days` parameter in SIR model (more CPU load)
- Add more threads/processes
- Implement asyncio for I/O operations
- Add logging to track execution flow
- Measure memory usage with `psutil`

---

## 📝 Example Output

```bash
$ python "SIR Model Testing/1-CPU_BOUND_PROCESSES.py"
Process 1 finished with 987.45 infected and 2.34 recovered after 100 days.
Process 2 finished with 987.45 infected and 2.34 recovered after 100 days.
Process 3 finished with 987.45 infected and 2.34 recovered after 100 days.
Process 4 finished with 987.45 infected and 2.34 recovered after 100 days.
Total time for processes: 0.8234 seconds.

$ python "SIR Model Testing/2-CPU_BOUND_THREADS_1.py"
Thread 1 finished with 987.45 infected and 2.34 recovered after 100 days.
Thread 2 finished with 987.45 infected and 2.34 recovered after 100 days.
Thread 3 finished with 987.45 infected and 2.34 recovered after 100 days.
Thread 4 finished with 987.45 infected and 2.34 recovered after 100 days.
Total time for threads: 3.4521 seconds.
```

---

## ⚡ Performance Tips

1. **Profile your code** before choosing concurrency model
2. **Use `time.time()`** to measure actual performance
3. **Consider memory constraints** with multiprocessing
4. **Test with realistic workloads**
5. **Monitor with `top` or `Task Manager`** during execution

---

## 🤝 Contributing

Feel free to fork, modify, and experiment with these examples!

**Ideas:**
- Add asyncio examples
- Implement connection pooling for I/O
- Create benchmark comparisons chart
- Add more complex CPU/IO scenarios

---

## 📄 License

MIT License - Feel free to use for learning and projects

---

## 👤 Author

Volkan Deniz  
Computer Engineering Student | TEKNOFEST Participant  
[@GitHub](https://github.com/volkan)

---

## 🎯 Learning Outcomes

After studying this project, you'll understand:
- ✅ When to use threading vs multiprocessing
- ✅ How Python's GIL affects performance
- ✅ CPU-bound vs I/O-bound task characteristics
- ✅ Performance measurement and analysis
- ✅ Practical concurrency patterns in Python

---

**Happy Coding! 🚀**

*Last Updated: June 2024*
