<h1>ExpNo 1 :Developing AI Agent with PEAS Description</h1>
<h3>Name : ELavarasan M</h3>
<h3>Register Number :  212224040083</h3>


<h3>AIM:</h3>
<br>
<p>To find the PEAS description for the given AI problem and develop an AI agent.</p>
<br>
<h3>Theory</h3>
<h3>Medicine prescribing agent:</h3>
<p>Such this agent prescribes medicine for fever (greater than 98.5 degrees) which we consider here as unhealthy, by the user temperature input, and another environment is rooms in the hospital (two rooms). This agent has to consider two factors one is room location and an unhealthy patient in a random room, the agent has to move from one room to another to check and treat the unhealthy person. The performance of the agent is calculated by incrementing performance and each time after treating in one room again it has to check another room so that the movement causes the agent to reduce its performance. Hence, agents prescribe medicine to unhealthy.</p>
<hr>
<h3>PEAS DESCRIPTION:</h3>
<table>
  <tr>
    <td><strong>Agent Type</strong></td>
    <td><strong>Performance</strong></td>
     <td><strong>Environment</strong></td>
    <td><strong>Actuators</strong></td>
    <td><strong>Sensors</strong></td>
  </tr>
    <tr>
    <td><strong>Medicine prescribing agent</strong></td>
    <td><strong>Treating unhealthy, agent movement</strong></td>
     <td><strong>Rooms, Patient</strong></td>
    <td><strong>Medicine, Treatment</strong></td>
    <td><strong>Location, Temperature of patient</strong></td>
  </tr>
</table>
<hr>
<H3>DESIGN STEPS</H3>
<h3>STEP 1:Identifying the input:</h3>
<p>Temperature from patients, Location.</p>
<h3>STEP 2:Identifying the output:</h3>
<p>Prescribe medicine if the patient in a random has a fever.</p>
<h3>STEP 3:Developing the PEAS description:</h3>
<p>PEAS description is developed by the performance, environment, actuators, and sensors in an agent.</p>
<h3>STEP 4:Implementing the AI agent:</h3>
<p>Treat unhealthy patients in each room. And check for the unhealthy patients in random room</p>
<h3>STEP 5:</h3>
<p>Measure the performance parameters: For each treatment performance incremented, for each movement performance decremented</p>

<h3>Program : </h3>

```python

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

```

<h3>OUTPUT : </h3>

![alt text](images/image.png)

<h3>RESULT : </h3>
<p>Thus the Developing AI Agent with PEAS Description was implemented using python programming.</p>