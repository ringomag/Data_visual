import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-4,4,100)
y = 0.25 * ( x + 4 )*( x + 1 )*( x - 2 )

#x_details, y_details
xd = np.linspace(-2, 2, 100)
yd = 0.25 * ( xd + 4 )*( xd + 1 )*( xd - 2 )

plt.figure(figsize=(1280/72,720/72), dpi=72)
plt.plot(x, y, c = 'blue')

#annotate
x_min = -1+np.sqrt(3)
y_min = 0.25 * ( x_min + 4 )*( x_min + 1 )*( x_min - 2 )
print("x_min i y_min", x_min, y_min)
plt.annotate("Minimum", size=16, xy=(x_min, y_min), xytext=(-1,3), arrowprops=dict(arrowstyle="-|>", mutation_scale=25, lw=5, facecolor="black"))

sub_axes = plt.axes([.6, .6, .25, .25])
sub_axes.set_xticks([-2,0,2])
sub_axes.set_yticks([-2,0,2])


sub_axes.plot(xd, yd, c = 'blue')
plt.setp(sub_axes)


plt.suptitle('f(x) = 0.25(x + 4)(x + 1)(x - 2 ), x ∈ ( − 4, 4 )', x=0.25, y=0.93, size=16)

# for saving .pdf
# plt.savefig('task_2.pdf')  


plt.show()