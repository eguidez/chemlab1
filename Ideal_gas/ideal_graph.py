# This code produces scatter plots to analyze the ideal gas law
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Box dimensions
# -----------------------------
length = np.array([5, 7, 10, 12, 15])  # nm
height = 8.75                            # nm
depth = 4.0                              # nm
N = 100                                  # particles

# Calculate box volume (nm^3)
box_volume = length * height * depth

# Convert box volume to m^3
box_volume_m3 = box_volume * 1e-27

# Calculate molar volume (m^3/mol)
NA = 6.02214076e23
molar_volume = (box_volume_m3 / N) * NA

# Calculate inverse molar volume
inverse_molar_volume = 1 / molar_volume  # mol/m^3

# -----------------------------
# Temperature (K)
# -----------------------------
temperature = np.array([100, 200, 300, 500])

# -----------------------------
# Temperature (K)
# -----------------------------
inverse_temperature = 1/temperature
# -----------------------------
# Pressure data (atm)
# Rows correspond to lengths
# Columns correspond to temperatures
# -----------------------------
pressure_atm = np.array([
    [7.74, 15.6, 23.4, 38.98],
    [5.40, 10.96, 16.54, 27.6],
    [3.96, 7.72, 11.74, 19.26],
    [3.26, 6.50, 10.06, 16.08],
    [2.52, 5.14, 7.92, 12.84]
])

# Convert pressure from atm to Pa
pressure_Pa = pressure_atm * 101325

# -----------------------------
# Create three subplots
# -----------------------------
fig, ax = plt.subplots(2, 2, figsize=(10, 5))

# ==========================================
# Subplot 1: P vs Vm
# ==========================================
for i in range(len(length)):
    ax[0,0].plot(molar_volume[i],
               pressure_Pa[:, 0][i],
               'o-')

# Plot each temperature
for j, T in enumerate(temperature):
    ax[0,0].plot(molar_volume,
               pressure_Pa[:, j],
               'o-',
               label=f'{T} K')

ax[0,0].set_xlabel('Molar Volume (m$^3$/mol)')
ax[0,0].set_ylabel('Pressure (Pa)')
ax[0,0].set_title('Pressure vs. Molar Volume')
ax[0,0].grid(True, alpha=0.3)
ax[0,0].legend()

# ==========================================
# Subplot 2: P vs 1/Vm
# ==========================================
for j, T in enumerate(temperature):
    x = inverse_molar_volume
    y = pressure_Pa[:, j]

    # Linear fit: P = m(1/Vm) + b
    m, b = np.polyfit(x, y, 1)

    # Calculate R^2
    y_fit = m * x + b
    ss_res = np.sum((y - y_fit) ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    r2 = 1 - ss_res / ss_tot

    ax[0,1].plot(inverse_molar_volume,
               pressure_Pa[:, j],
               'o-',
               label=f'{T} K')

# Equation text
    equation = f'P = {m:.2f}(1/Vm) {b:+.1f}'

    # Position text near the corresponding line
    ax[0,1].text(
        x[0] * 0.5,
        y_fit[1],
        equation,
        fontsize=9,
        ha='left',
        va='top'
    )

ax[0,1].set_xlabel(r'$1/V_m$ (mol/m$^3$)')
ax[0,1].set_ylabel('Pressure (Pa)')
ax[0,1].set_title(r'Pressure vs. inverse molar volume')
ax[0,1].grid(True, alpha=0.3)
ax[0,1].legend()

# ==========================================
# Subplot 3: P vs T
# ==========================================
for i, Vm in enumerate(molar_volume):
    x = temperature
    y = pressure_Pa[i, :]

    # Linear fit: P = m(1/Vm) + b
    m, b = np.polyfit(x, y, 1)

    # Calculate R^2
    y_fit = m * x + b
    ss_res = np.sum((y - y_fit) ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    r2 = 1 - ss_res / ss_tot

    # Equation text
    equation = f'P = {m:.2f}(T) {b:+.1f}'

    # Position text near the corresponding line
    ax[1,0].text(
        x[2],
        y_fit[2],
        equation,
        fontsize=9,
        ha='left',
        va='top'
    )

    ax[1,0].plot(temperature,
               pressure_Pa[i, :],
               'o-',
               label=f'$V_m$ = {Vm:.2e} m$^3$/mol')

ax[1,0].set_xlabel('Temperature (K)')
ax[1,0].set_ylabel('Pressure (Pa)')
ax[1,0].set_title('Pressure vs. Temperature')
ax[1,0].grid(True, alpha=0.3)
ax[1,0].legend(fontsize=8)


# ==========================================
# Subplot 4: P vs 1/T
# ==========================================
for i, Vm in enumerate(molar_volume):
    ax[1,1].plot(inverse_temperature,
               pressure_Pa[i, :],
               'o-',
               label=f'$V_m$ = {Vm:.2e} m$^3$/mol')

ax[1,1].set_xlabel('Inverse Temperature (1/K)')
ax[1,1].set_ylabel('Pressure (Pa)')
ax[1,1].set_title('Pressure vs. Inverse Temperature')
ax[1,1].grid(True, alpha=0.3)
ax[1,1].legend(fontsize=8)
plt.tight_layout()
plt.show()
plt.savefig("high_res_plot.png", dpi=300, bbox_inches="tight")


