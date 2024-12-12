"""
TI-84 Plus CE Python calculator cannot allocate enough ram if this was included in the main kinematics file.
If you are planning to send to your calculator, please do so as two seperate files. If not, feel free to combine them into one.
"""

import math
import sys

def calculate_final_velocity(velocity_initial, acceleration, time):
    return velocity_initial + acceleration * time

def calculate_final_velocity_from_displacement(velocity_initial, acceleration, displacement):
    vf_squared = velocity_initial ** 2 + 2 * acceleration * displacement
    return math.sqrt(vf_squared)

def calculate_displacement_with_acceleration(velocity_initial, acceleration, time):
    return velocity_initial * time + 0.5 * acceleration * time ** 2

def calculate_time_from_velocities(velocity_final, velocity_initial, acceleration):
    if acceleration == 0:
        raise ValueError("Acceleration cannot be zero.")
    return (velocity_final - velocity_initial) / acceleration

def calculate_acceleration_from_displacement(velocity_initial, velocity_final, displacement):
    if displacement == 0:
        raise ValueError("Displacement cannot be zero.")
    return (velocity_final ** 2 - velocity_initial ** 2) / (2 * displacement)

def calculate_projectile_range(velocity, angle, use_radians):
    angle = angle if use_radians else math.radians(angle)
    return (velocity ** 2 * math.sin(2 * angle)) / 9.8

def calculate_projectile_max_height(velocity, angle, use_radians):
    angle = angle if use_radians else math.radians(angle)
    return (velocity ** 2 * math.sin(angle) ** 2) / (2 * 9.8)

def calculate_projectile_time_of_flight(velocity, angle, use_radians):
    angle = angle if use_radians else math.radians(angle)
    return (2 * velocity * math.sin(angle)) / 9.8

def extras_menu():
    print("\n\nWhat would you like to calculate?")
    print("1. Extra Velocity, Acceleration, and Time")
    print("2. Projectile Motion")
    print("3. Exit Program")
    choice = input("Enter the number of your choice: ")

    if choice == '1':
        advanced_kinematics_menu()
    elif choice == '2':
        projectile_motion_menu()
    elif choice == '3':
        print("Program terminated")
        sys.exit()
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
        extras_menu()

def advanced_kinematics_menu():
    print("\nExtra Kinematics:")
    print("1. Final Velocity from Initial Velocity, Acceleration, and Time")
    print("2. Final Velocity from Initial Velocity, Acceleration, and Displacement")
    print("3. Time from Initial and Final Velocities and Acceleration")
    sub_choice = input("Enter the number of your choice: ")

    if sub_choice == '1':
        try:
            velocity_initial = float(input("Enter initial velocity (m/s): "))
            acceleration = float(input("Enter acceleration (m/s^2): "))
            time = float(input("Enter time (s): "))
            if time <= 0:
                print("Error: time must be a positive value.")
                return
            velocity_final = calculate_final_velocity(velocity_initial, acceleration, time)
            print("Final Velocity is {:.2f} m/s".format(velocity_final))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
    elif sub_choice == '2':
        try:
            velocity_initial = float(input("Enter initial velocity (m/s): "))
            acceleration = float(input("Enter acceleration (m/s^2): "))
            displacement = float(input("Enter displacement (m): "))
            if displacement < 0:
                print("Error: displacement must be a non-negative value.")
                return
            velocity_final = calculate_final_velocity_from_displacement(velocity_initial, acceleration, displacement)
            print("Final Velocity is {:.2f} m/s".format(velocity_final))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
    elif sub_choice == '3':
        try:
            velocity_initial = float(input("Enter initial velocity (m/s): "))
            velocity_final = float(input("Enter final velocity (m/s): "))
            acceleration = float(input("Enter acceleration (m/s^2): "))
            if acceleration == 0:
                print("Error: acceleration must be non-zero.")
                return
            time = calculate_time_from_velocities(velocity_final, velocity_initial, acceleration)
            print("Time is {:.2f} seconds".format(time))
        except ValueError as e:
            print("Invalid input:", e)
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

def projectile_motion_menu():
    print("\n\nProjectile Motion Calculations:")
    print("Would you like to use angles in:")
    print("1. Radians")
    print("2. Degrees")
    unit_choice = input("Enter 1 for radians or 2 for degrees: ")
    use_radians = unit_choice == '1'

    print("\n\nSelect calculation:\n")
    print("1. Range of the projectile")
    print("2. Maximum height of the projectile")
    print("3. Time of flight of the projectile")
    sub_choice = input("Enter the number of your choice: ")

    if sub_choice in ['1', '2', '3']:
        velocity = float(input("\n\nEnter initial velocity (m/s): "))
        angle = float(input("Enter angle of projection: "))

        if sub_choice == '1':
            range_ = calculate_projectile_range(velocity, angle, use_radians)
            print("\n\n The range of the projectile is " + "{:.2f}".format(range_) + " meters")
        elif sub_choice == '2':
            max_height = calculate_projectile_max_height(velocity, angle, use_radians)
            print("\n\nThe maximum height of the projectile is " + "{:.2f}".format(max_height) + " meters")
        elif sub_choice == '3':
            time_of_flight = calculate_projectile_time_of_flight(velocity, angle, use_radians)
            print("\n\nThe time of flight of the projectile is " + "{:.2f}".format(time_of_flight) + " seconds")
    else:
        print("\n\nInvalid choice. Please select 1, 2, or 3.")
        projectile_motion_menu()

extras_menu()