walk_speed = [1,2,5,10,23]

def least_time(speed: list):
    return sum(speed) + ((len(speed) - 3) * min(speed))

print(least_time(walk_speed))
