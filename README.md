# 🟦 Bubble Sort Visualization in Python

This project demonstrates a real-time visualization of the Bubble Sort algorithm using Python's `matplotlib` library. By animating the sorting process, this tool helps users understand how Bubble Sort operates step by step as it arranges a list of random numbers in ascending order.

## ✨ Features

- **Dynamic Visualization:** Watch the Bubble Sort algorithm in action as the bars are rearranged in real time.
- **Random Data Generation:** Each run generates a new set of random numbers for sorting.
- **Educational Tool:** Great for students and educators to visually grasp sorting algorithms.

## 🛠️ Requirements

- Python 3.x
- matplotlib

## 🚀 How to Run

1. **Clone the repository or copy the script.**
2. **Install the required library:**
    ```bash
    pip install matplotlib
    ```
3. **Run the script:**
    ```bash
    python bubble_sort_visualization.py
    ```
4. **Enjoy the animated sorting process in the pop-up window!**

## 📁 How It Works

- The script generates a list of random integers.
- Bubble Sort is implemented as a generator, yielding the list at every swap.
- `matplotlib.animation.FuncAnimation` updates the bar heights to visualize the sorting process in real time.

---
