import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import signal

def M(s):
    return s**4 + 11*s**3 + 44*s**2 + 76*s + 48

def MClosed(s):
    return s**8 + 22 *s**7+ 209 *s**6+ 1120 *s**5+ 3719 *s**4+ 7909 *s**3+ 10660 *s**2+ 8436 *s+ 3024

def main():
    # OPEN SYSTEM - Z4
    
    omega = np.linspace(0, 25, 100)
    Re = M(omega * 1j).real
    Im = M(omega * 1j).imag
    angle = np.angle(M(omega * 1j), deg=False)  # Argument w radianach
    
    # Tworzenie wykresu Real vs Imaginary Parts
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    
    # Wykres Re vs Im
    ax1.axhline(linewidth=1, color='black')
    ax1.axvline(linewidth=1, color='black')
    ax1.plot(Re, Im, label='M(s)')
    ax1.set_xlabel('Real Part')
    ax1.set_ylabel('Imaginary Part')
    ax1.set_title('Real vs Imaginary Parts')
    ax1.grid(True)
    
    # Zaznaczenie punktów dla wybranych wartości ω
    omega_points = [0, 2*np.sqrt(33)/11, 3.1, 10.28]
    for omega_point in omega_points:
        M_point = M(omega_point * 1j)
        ax1.scatter(M_point.real, M_point.imag, color='red', label=f'ω = {omega_point}', zorder=5)
    
    ax1.legend()
    ax1.set_xlim([-500, 500])
    ax1.set_ylim([-500, 500])
    
    # Wykres zmiany argumentu funkcji M(jω)
    ax2.axhline(linewidth=1, color='black')
    ax2.axvline(linewidth=1, color='black')
    ax2.plot(omega, angle, label='Angle of M(s)', color='green')
    ax2.axhline(2*np.pi, linestyle='--', color='red', label='$2\pi$')
    ax2.set_xlabel('ω')
    ax2.set_ylabel('Angle (radians)')  # Zmieniamy etykietę na radiany
    ax2.set_title('Angle of M(ω * jω)')
    ax2.grid(True)
    
    # Zaznaczenie punktów dla wybranych wartości ω bliskich 2π
    for omega_point in omega_points:
        M_point = M(omega_point * 1j)
        angle_point = np.angle(M_point, deg=False)  # Argument w radianach
        ax2.scatter(omega_point, angle_point, color='red', label=f'ω = {omega_point}', zorder=5)
    
    ax2.legend()
    plt.tight_layout()
    plt.show()
    
    # STEP RESPONSE
    # OPEN SYSTEM
    k_values = [100, 208.37, 300]
    
    # Step Response - PART 1
    plt.figure(figsize=(8, 10))
    plt.subplot(2, 1, 1)
    plt.axhline(linewidth=1, color='black')
    plt.axvline(linewidth=1, color='black')
    for k in k_values:
        lti = signal.lti([k], [1, 11, 44, 76, 48])
        t1 = np.linspace(0, 100, 100)
        t, y = signal.step(lti, T=t1)
        plt.plot(t, y, label=f'k = {k}')
        poles = lti.poles
        if np.any(np.real(poles) > 0):
            print(f"For k = {k}, the system is unstable.")
        else:
            print(f"For k = {k}, the system is stable.")
        
    plt.title('Step Response for Different Values of k - Part 1')
    plt.xlabel('Time')
    plt.ylabel('Output')
    plt.grid(True)
    plt.legend()
    
    # Step Response - PART 2
    plt.subplot(2, 1, 2)
    plt.axhline(linewidth=1, color='black')
    plt.axvline(linewidth=1, color='black')
    for k in k_values:
        lti = signal.lti([1*k, 11*k, 44*k, 76*k, 48*k], [1, 22, 209, 1120, k + 3704, 11*k + 7744, 44*k+10000, 76*k+7296, 48*k+2304])
        t1 = np.linspace(0, 100, 100)
        t, y = signal.step(lti, T=t1)
        
        # Plot the step response
        plt.plot(t, y, label=f'k = {k}')
        
        # Check stability
        poles = lti.poles
        if np.any(np.real(poles) > 0):
            print(f"For k = {k}, the system is unstable.")
        else:
            print(f"For k = {k}, the system is stable.")
            
    plt.title('Step Response for Different Values of k - Part 2')
    plt.xlabel('Time')
    plt.ylabel('Output')
    plt.grid(True)
    plt.legend()
    
    plt.tight_layout()
    plt.show()
    
    
    # NIQUIST - CLOSED
    num_closed = [15, 165, 660, 1140, 720]
    den_closed = [1, 22, 209, 1120, 3719, 7909, 10660, 8436, 3204]
    s1_closed = signal.TransferFunction(num_closed, den_closed)
    
    # PART 1
    omega_closed, H_closed = signal.freqresp(s1_closed)
    angle_closed = np.angle(H_closed, deg=False)
    
    # PART 2
    H_closed_plus = H_closed + 1
    angle_closed_plus_1 = np.angle(H_closed_plus, deg=False)
    
    fig, axs = plt.subplots(2, 2, figsize=(12, 8))
    
    # Charakterystyka Nyquista - PART 1
    axs[0, 0].axhline(linewidth=1, color='black')
    axs[0, 0].axvline(linewidth=1, color='black')
    axs[0, 0].plot(H_closed.real, H_closed.imag, "b")
    axs[0, 0].plot(-1, 0, 'ro') 
    axs[0, 0].set_title('Charakterystyka Nyquista - PART 1')
    
    # Wykres zmiany argumentu funkcji zamkniętej - PART 1
    axs[1, 0].axhline(linewidth=1, color='black')
    axs[1, 0].axvline(linewidth=1, color='black')
    axs[1, 0].plot(omega_closed, angle_closed, label='Angle of H Closed(s)', color='green')
    axs[1, 0].set_xlabel('ω')
    axs[1, 0].set_ylabel('Angle (degrees)')
    axs[1, 0].set_title('Angle of K(jω) - PART 1')
    axs[1, 0].grid(True)
    axs[1, 0].legend()
    
    # Charakterystyka Nyquista - PART 2
    axs[0, 1].axhline(linewidth=1, color='black')
    axs[0, 1].axvline(linewidth=1, color='black')
    axs[0, 1].plot(H_closed_plus.real, H_closed_plus.imag, "b")
    axs[0, 1].plot(0, 0, 'ro') 
    axs[0, 1].set_title('Charakterystyka Nyquista - PART 2')
    
    # Wykres zmiany argumentu funkcji zamkniętej - PART 2
    axs[1, 1].axhline(linewidth=1, color='black')
    axs[1, 1].axvline(linewidth=1, color='black')
    axs[1, 1].plot(omega_closed, angle_closed_plus_1, label='Angle of H Closed(s) + 1', color='red')
    axs[1, 1].set_xlabel('ω')
    axs[1, 1].set_ylabel('Angle (degrees)')
    axs[1, 1].set_title('Angle of K(jω) + 1 - PART 2')
    axs[1, 1].grid(True)
    axs[1, 1].legend()
    
    plt.tight_layout()
    plt.show()
    
main()