import time

#main function to determine traffic light status
def traffic_logic(time_of_day, cars_waiting, emergency_vehicle):
    #emergency override
    if emergency_vehicle == 'yes':
        return "Green light immediately(emergency 🚨)"
    
    # Invalidate if not in range(0 to 2400) simulates 24-hour format)
    if not (0 <= time_of_day <= 2400):
        return "Invalid time of day(please enter a number between 1 and 24)"
        
    # night with no traffic
    if time_of_day >= 2000 and cars_waiting == 0:
        return "Flashing yellow light(Night mode no traffic)"
        
    # day with traffic
    if cars_waiting >= 10:
        return "Longer green light"
        
    #default case
    return "standard cycle"

# 🚦 Light simulation function
def simulate_light_cycle(mode):
    print("\n 🚦 ----simulating traffic lights---\n")

    # simulate emergency override
    if mode == "Green light immediately(emergency 🚨)":
        print("🟢 GREEN LIGHT- Emergency override")
        time.sleep(3)

    # simulate flashing yellow light
    elif mode == "Flashing yellow light(Night mode no traffic)":
        for i in range(6):
            print("🟡 FLASHING YELLOW LIGHT ...")
            time.sleep(1)
    
    # simulate longer green light
    elif mode == "Longer green light":
        print("🔴 RED LIGHT")
        time.sleep(4)
        print("🟢 GREEN LIGHT (longer duration)")
        time.sleep(10)
        print("🟡 YELLOW LIGHT")
        time.sleep(4)

    # simulate standard cycle
    elif mode == "standard cycle":
        print("🔴 RED LIGHT")
        time.sleep(4)
        print("🟢 GREEN LIGHT (standard duration)")
        time.sleep(4)
        print("🟡 YELLOW LIGHT")
        time.sleep(4)

    else : 
        print("⚠️ Something went wrong.")

# Function to add the decision to a txt file
def log_decision(time_of_day, cars_waiting, emergency_vehicle, status):
    with open("traffic_log.txt", "a", encoding="utf-8") as log_file:
        log_file.write("---- Traffic Light log ----\n")
        log_file.write(f"Time of Day: {time_of_day}\n")
        log_file.write(f"Cars Waiting: {cars_waiting}\n")
        log_file.write(f"Emergency Vehicle: {emergency_vehicle}\n")
        log_file.write(f"Decision: {status}\n")
        log_file.write("---------------------------\n\n")



while True:
    print("\n--- Smart Traffic Light System ---")

    try:
        #Get user input
        time_of_day = int(input("Enter the time of day (0 to 2400): "))
        cars_waiting = int(input("Enter the number of cars waiting at the traffic light: "))
        emergency_vehicle = input("Is there an emergency vehicle approaching? (yes/no): ").strip().lower()
    except ValueError:
        print("❌ Invalid input. Please enter valid numbers.")
        continue
        
    # Get the status from the function
    status = traffic_logic(time_of_day, cars_waiting, emergency_vehicle)
    print(f"\n🚦 Traffic light status:\n{status}")

    log_decision(time_of_day, cars_waiting, emergency_vehicle, status)

    # Simulate the decision
    simulate_light_cycle(status)
    
    #ask user if they want to continue
    continue_choice = input("Do you want to simulate another traffic light scenario? (yes/no): ").strip().lower()
    if continue_choice != 'yes':
        print("Exiting the traffic light system.")
        break



