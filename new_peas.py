
import random
import time

# Define rooms
room_A = (0, 0)
room_B = (1, 0)

# Agent class
class Agent:
    def __init__(self, program):
        self.alive = True
        self.performance = 0
        self.program = program
        self.location = random.choice([room_A, room_B])

# Agent decision logic using a table
def doctor_program(percept):
    location, status = percept
    if status == "unhealthy":
        return "treat"
    return "Right" if location == room_A else "Left"

# Environment class
class DoctorEnvironment:
    def __init__(self):
        self.status = {
            room_A: random.choice(["healthy", "unhealthy"]),
            room_B: random.choice(["healthy", "unhealthy"]),
        }
        self.agent = Agent(doctor_program)

    def percept(self):
        return self.agent.location, self.status[self.agent.location]

    def execute_action(self, action):
        loc = self.agent.location
        if action == "Right":
            self.agent.location = room_B
            self.agent.performance -= 1
        elif action == "Left":
            self.agent.location = room_A
            self.agent.performance -= 1
        elif action == "treat":
            temp = float(input(f"Enter temperature for patient in {loc}: "))
            if temp > 98.5:
                print("Prescribed: Paracetamol and antibiotic.")
                self.agent.performance += 10
            else:
                print("No medicine needed.")
            self.status[loc] = "healthy"

    def run(self, steps=2):
        for i in range(steps):
            print(f"\nStep {i+1}")
            percept = self.percept()
            action = self.agent.program(percept)
            self.execute_action(action)
            print(f"Room Status: {self.status}")
            print(f"Agent Location: {self.agent.location}")
            print(f"Performance: {self.agent.performance}")
            time.sleep(1)

# Run the simulation
env = DoctorEnvironment()
print("Initial Room Status:", env.status)
print("Starting Location:", env.agent.location)
env.run()
