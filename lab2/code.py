import numpy as np
import matplotlib.pyplot as plt

# Функция варианта 8 (первая часть)
def f(x):
    return 1 / (1 + 25 * x**2)

# Производная
def f_prime(x):
    return -50 * x / (1 + 25 * x**2)**2

# Данные
x = np.linspace(0, 0.6, 500)
y = f(x)

# Точка касания
x0 = 0.3
y0 = f(x0)
k = f_prime(x0)

# Касательная
x_t = np.linspace(x0 - 0.15, x0 + 0.15, 100)
y_t = y0 + k * (x_t - x0)

# График
plt.figure(figsize=(9, 5))
plt.plot(x, y, label='f(x)', linewidth=2, color='blue')
plt.plot(x_t, y_t, label='Касательная', linewidth=2, color='red', linestyle='--')
plt.plot(x0, y0, 'ro', markersize=8)
plt.annotate(f'({x0}, {y0:.3f})', xy=(x0, y0), xytext=(x0+0.1, y0+0.1),
             arrowprops=dict(arrowstyle='->', color='red'))

plt.title('График функции варианта 8 и касательная', fontsize=12, fontweight='bold')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.axhline(0, color='k', linewidth=0.5)
plt.axvline(0, color='k', linewidth=0.5)

plt.savefig('task4_graph.png', dpi=300, bbox_inches='tight')
plt.show()

print(f"Точка: x0={x0}, f(x0)={y0:.4f}, f'(x0)={k:.4f}")
print(f"Касательная: y = {y0:.4f} + {k:.4f}(x - {x0})")