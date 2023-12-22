import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

def bubble_sort(data):
    n = len(data)

    for i in range(n):
        for j in range(0,n-i-1):
            if data[j]>data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]
                yield data.copy()


def generate_data(size):
    return [random.randint(1,100) for _ in range(size)]

def update_plot(frame,bars):
    for bar,val in zip(bars, frame):
        bar.set_height(val)
    return bars

def main():
    size = 30
    data = generate_data(size)

    fig,ax = plt.subplots()
    bars = ax.bar(range(len(data)),data,color='blue')
    ax.set_xlim(0, len(data))
    ax.set_ylim(0, max(data) + 10)

    ani = animation.FuncAnimation(fig, update_plot, fargs=(bars,),frames=bubble_sort(data), repeat=False, interval=50)

    plt.show()

if __name__ == "__main__":
    main()