def reward_function(params):
    # Extract input parameters
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    steering_angle = params['steering_angle']
    speed = params['speed']

    # Normalize distance from center
    norm_distance = distance_from_center / (track_width / 2)  # Normalize to [-1, 1]

    # Calculate reward based on distance from center
    if norm_distance <= 0.1:
        reward = 1.0
    elif norm_distance <= 0.25:
        reward = 0.5
    elif norm_distance <= 0.5:
        reward = 0.1
    else:
        reward = 1e-3  # Likely crashed or close to off track

    # Penalize reward if steering angle is too high
    abs_steering = abs(steering_angle)
    max_steering_threshold = 30 + (speed / 10)  # Adjust based on speed
    ABS_STEERING_THRESHOLD = max_steering_threshold
    if abs_steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8

    return float(reward)