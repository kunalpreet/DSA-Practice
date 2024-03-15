def maxArea(height):
    l, r = 0, len(height) - 1
    cap = 0

    while l < r:
        area = min(height[l], height[r]) * (r-l)
        if area > cap:
            cap = area
        else:
            if height[l] > height[r]:
                r = r - 1
            else:
                l = l + 1
    return cap


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
