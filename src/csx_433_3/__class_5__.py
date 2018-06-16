from numpy import random, min, max, asarray
import pylab as plb

# Create a list A of 600 random numbers bound between [0:10]
A = random.randint(0, 10, 600)

# Create an array B of 500 elements bound in range -3pi to 2pi
B = plb.linspace(-plb.pi*3, plb.pi*2, 500, endpoint=True)


def func_a_update():
    average_of_a = (min(A)+max(A))/2
    length_of_a = range(0, len(A))
    for j in length_of_a:
            if A[j] <= 2 or A[j] > 9:
                A[j] = average_of_a
    normalized_a = (A-min(A))/((max(A)-min(A))*10)
    return normalized_a


norm_A = (A-min(A))/((max(A)-min(A))*10)


C = func_a_update()

C = asarray(C)

D = B + C[0:500]

plb.figure(figsize=(10, 6), dpi=120)

plb.subplot(2, 1, 1)
plb.title('Plot of sin, cos functions')
plb.plot(D, plb.sin(D), color="blue", linewidth=1.5, linestyle='-', label="sin")

plb.hold(True)
plb.plot(D, plb.cos(D), color="red", linewidth=1.2, linestyle='-.', label="cos")

plb.grid()

plb.ylabel('Y-Axis')
plb.legend(loc="lower right")

plb.subplot(2, 1, 2)
plb.title('Plot for tan functions')
plb.plot(D, plb.tan(D), color="red", linewidth=1.5, linestyle='-', label="tan")
plb.xlabel('X-axis')
plb.ylabel('Y-axis')
plb.grid()
plb.legend(loc="upper right")

plb.show()
