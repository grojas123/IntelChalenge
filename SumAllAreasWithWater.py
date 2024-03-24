def water_areas(height):
    areas = []
    left = 0
    right = len(height) - 1

    while left < right:
        area = min(height[left], height[right]) * (right - left)
        areas.append(area)  # Append current area to the list
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return sum(areas)

