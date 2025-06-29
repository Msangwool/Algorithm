from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque() # (weight, exit_time)
    current_weight = 0
    truck = deque(truck_weights)
    
    while bridge or truck:
        time += 1
        
        if bridge and time == bridge[0][1]:
            exit_weight, _ = bridge.popleft()
            current_weight -= exit_weight
            
        if truck and truck[0] + current_weight <= weight and len(bridge) < bridge_length:
            current_weight += truck[0]
            bridge.append((truck.popleft(), time + bridge_length))
    
    return time
