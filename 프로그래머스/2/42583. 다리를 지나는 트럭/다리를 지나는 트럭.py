from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque()  
    current_weight = 0
    trucks = deque(truck_weights)
    
    while trucks or bridge:
        time += 1
        
        if bridge and bridge[0][1] == time:
            truck_weight, _ = bridge.popleft()
            current_weight -= truck_weight
        
        if trucks:
            if current_weight + trucks[0] <= weight and len(bridge) < bridge_length:
                truck = trucks.popleft()
                current_weight += truck
                bridge.append((truck, time + bridge_length))
    
    return time
