import sys

def calculate_velocity(acceleration, time):
    return acceleration * time

def calculate_velocity_from_displacement_time(displacement, time):
    return displacement / time

def calculate_acceleration(velocity, time):
    return velocity / time

def calculate_acceleration_from_velocity_change(velocity_final, velocity_initial, time):
    return (velocity_final - velocity_initial) / time

def calculate_displacement(velocity, time):
    return velocity * time

def calculate_displacement_from_velocity_time(velocity_initial, velocity_final, time):
    return 0.5 * (velocity_initial + velocity_final) * time

def main_menu():
    print("\n\nWhat would you like to calculate?")
    print("1. Velocity")
    print("2. Acceleration")
    print("3. Displacement")
    print("4. Exit Program")
    choice = input("Enter the number of your choice: ")

    if choice == '1':
        velocity_menu()
    elif choice == '2':
        acceleration_menu()
    elif choice == '3':
        displacement_menu()
    elif choice == '4':
        print("Program terminated")
        sys.exit()
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")
        main_menu()

def velocity_menu():
    print("\n\nCalculate Velocity from:")
    print("1. Acceleration and Time")
    print("2. Displacement and Time")
    sub_choice = input("Enter the number of your choice: ")

    if sub_choice == '1':
        acceleration = float(input("\n\nEnter acceleration (m/s^2): "))
        time = float(input("Enter time (s): "))
        velocity = calculate_velocity(acceleration, time)
        print("\n\nVelocity is " + str(velocity) + " m/s")
    elif sub_choice == '2':
        displacement = float(input("\n\nEnter displacement (m): "))
        time = float(input("Enter time (s): "))
        velocity = calculate_velocity_from_displacement_time(displacement, time)
        print("\n\nVelocity is " + str(velocity) + " m/s")
    else:
        print("\n\nInvalid choice. Please select 1 or 2.")
        velocity_menu()

def acceleration_menu():
    print("\n\nCalculate Acceleration from:")
    print("1. Velocity and Time")
    print("2. Change in Velocity and Time")
    sub_choice = input("Enter the number of your choice: ")

    if sub_choice == '1':
        velocity = float(input("\n\nEnter velocity (m/s): "))
        time = float(input("Enter time (s): "))
        acceleration = calculate_acceleration(velocity, time)
        print("\n\nAcceleration is " + str(acceleration) + " m/s^2")
    elif sub_choice == '2':
        velocity_initial = float(input("\n\nEnter initial velocity (m/s): "))
        velocity_final = float(input("Enter final velocity (m/s): "))
        time = float(input("Enter time (s): "))
        acceleration = calculate_acceleration_from_velocity_change(velocity_final, velocity_initial, time)
        print("\n\nAcceleration is " + str(acceleration) + " m/s^2")
    else:
        print("Invalid choice. Please select 1 or 2.")
        acceleration_menu()

def displacement_menu():
    print("\n\nCalculate Displacement from:")
    print("1. Velocity and Time")
    print("2. Initial and Final Velocity and Time")
    sub_choice = input("Enter the number of your choice: ")

    if sub_choice == '1':
        velocity = float(input("\n\nEnter velocity (m/s): "))
        time = float(input("Enter time (s): "))
        displacement = calculate_displacement(velocity, time)
        print("\n\nDisplacement is " + str(displacement) + " meters")
    elif sub_choice == '2':
        velocity_initial = float(input("\n\nEnter initial velocity (m/s): "))
        velocity_final = float(input("Enter final velocity (m/s): "))
        time = float(input("Enter time (s): "))
        displacement = calculate_displacement_from_velocity_time(velocity_initial, velocity_final, time)
        print("\n\nDisplacement is " + str(displacement) + " meters")
    else:
        print("\n\nInvalid choice. Please select 1 or 2.")
        displacement_menu()

main_menu()
