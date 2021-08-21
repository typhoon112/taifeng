import matplotlib.pyplot as plt
import numpy as np

def tanh(x, k=np.e):
    lnk = np.log(k)
    A = np.exp(x * lnk)
    B = np.exp(-x * lnk)
    return (A - B) / (A + B)

sp = 1.005

plt.rcParams["font.size"] = 9

def fig2():
    x = [0, 1, 2, 3, 4, 5]
    y = [0.0, 35.23043002859886, 65.77179638720536, 108.3704277005494, 125.22440017824003, 165.3982369918131]
    z = 1 - tanh(np.array(y), sp)
    xt = ["A", "B", "C", "D", "E", "F"]
    fig = plt.figure(figsize=(6, 3))
    ax1, ax2 = fig.subplots(1, 2)
    fig.subplots_adjust(wspace=0.35)
    ax1.set_title("(a) Similarity Distances")
    ax1.set_xticks(x)
    ax1.set_xticklabels(xt)
    ax1.grid(True, axis="y", linewidth=0.3)
    ax1.set_ylim((0, 176))
    ax1.bar(x, y)
    for a, b in zip(x, y):
        ax1.text(a, max(0.05, b + 0.05), "{:.2f}".format(b), ha="center", va="bottom", fontsize=7)
    ax2.set_title("(b) Similarity Percentages")
    ax2.set_xticks(x)
    ax2.set_xticklabels(xt)
    ax2.set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1])
    ax2.set_yticklabels(["0%", "20%", "40%", "60%", "80%", "100%"])
    ax2.grid(True, axis="y", linewidth=0.3)
    ax2.set_ylim((0, 1.07))
    ax2.bar(x, z)
    for a, b in zip(x, z):
        ax2.text(a, max(0.005, b + 0.005), "{:.1f}%".format(b * 100), ha="center", va="bottom", fontsize=7)
    # plt.show()
    plt.savefig("fig2.png", dpi=300, bbox_inches="tight")
    
def fig4():
    x = [0, 1, 2, 3]
    y = [0.0, 84.82319022531512, 85.28292208877455, 88.2207472763635]
    z = 1 - tanh(np.array(y), sp)
    xt = ["G", "H", "I", "J"]
    fig = plt.figure(figsize=(5, 2.5))
    ax1, ax2 = fig.subplots(1, 2)
    fig.subplots_adjust(wspace=0.35)
    ax1.set_title("(a) Similarity Distances")
    ax1.set_xticks(x)
    ax1.set_xticklabels(xt)
    ax1.grid(True, axis="y", linewidth=0.3)
    ax1.set_ylim((0, 95))
    ax1.bar(x, y)
    for a, b in zip(x, y):
        ax1.text(a, max(0.05, b + 0.05), "{:.2f}".format(b), ha="center", va="bottom", fontsize=7)
    ax2.set_title("(b) Similarity Percentages")
    ax2.set_xticks(x)
    ax2.set_xticklabels(xt)
    ax2.set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1])
    ax2.set_yticklabels(["0%", "20%", "40%", "60%", "80%", "100%"])
    ax2.grid(True, axis="y", linewidth=0.3)
    ax2.set_ylim((0, 1.07))
    ax2.bar(x, z)
    for a, b in zip(x, z):
        ax2.text(a, max(0.005, b + 0.005), "{:.1f}%".format(b * 100), ha="center", va="bottom", fontsize=7)
    # plt.show()
    plt.savefig("fig4.png", dpi=300, bbox_inches="tight")

def fig6():
    x = np.arange(0, 10, 0.001)
    plt.plot(x, 1 - tanh(x), label="A.$f(x;e)$")
    plt.text(1.6, 0.1, "A", fontsize=12)
    plt.plot(x, 1 - tanh(x, 1.4), label="B.$f(x;1.4)$")
    plt.text(3.9, 0.15, "B", fontsize=12)
    plt.plot(x, 1 - tanh(x, 1.5), label="C.$f(x;1.5)$")
    plt.text(1.9, 0.25, "C", fontsize=12)
    plt.plot(x, 1 - tanh(x, 6), label="D.$f(x;6)$")
    plt.text(0.1, 0.3, "D", fontsize=12)
    plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1], ["0%", "20%", "40%", "60%", "80%", "100%"])
    plt.grid()
    plt.legend(fontsize=12)
    # plt.show()
    plt.savefig("fig6.png", dpi=300, bbox_inches="tight")

def fig7():
    x = [0, 1, 2, 3, 4, 5]
    y = [0.0, 10.084393883620377, 10.19264440662973, 15.83903406145715, 18.013189612059257, 18.802659386374042]
    z = 1 - tanh(np.array(y), sp)
    xt = ["K", "L", "M", "N", "O", "P"]
    fig = plt.figure(figsize=(6, 3))
    ax1, ax2 = fig.subplots(1, 2)
    fig.subplots_adjust(wspace=0.35)
    ax1.set_title("(a) Similarity Distances")
    ax1.set_xticks(x)
    ax1.set_xticklabels(xt)
    ax1.grid(True, axis="y", linewidth=0.3)
    ax1.set_ylim((0, 19.8))
    ax1.bar(x, y)
    for a, b in zip(x, y):
        ax1.text(a, max(0.05, b + 0.05), "{:.2f}".format(b), ha="center", va="bottom", fontsize=7)
    ax2.set_title("(b) Similarity Percentages")
    ax2.set_xticks(x)
    ax2.set_xticklabels(xt)
    ax2.set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1])
    ax2.set_yticklabels(["0%", "20%", "40%", "60%", "80%", "100%"])
    ax2.grid(True, axis="y", linewidth=0.3)
    ax2.set_ylim((0, 1.07))
    ax2.bar(x, z)
    for a, b in zip(x, z):
        ax2.text(a, max(0.005, b + 0.005), "{:.1f}%".format(b * 100), ha="center", va="bottom", fontsize=7)
    # plt.show()
    plt.savefig("fig7.png", dpi=300, bbox_inches="tight")

# fig2()
# fig4()
# fig6()
fig7()