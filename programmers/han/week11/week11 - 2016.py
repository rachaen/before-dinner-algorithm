def solution(a, b):
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    weekends = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    
    sum_days = sum(days[:a-1]) + b - 1
    return weekends[sum_days % 7]
    