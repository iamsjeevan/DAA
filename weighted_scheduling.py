def weighted_interval_scheduling(intervals):
    intervals.sort(key=lambda x: x[1])

    n = len(intervals)
    dp = [0] * n

    dp[0] = intervals[0][2] 
    for i in range(1, n):
        value_incl = intervals[i][2]
        j = find_latest_non_overlapping(intervals, i)
        if j != -1:
            value_incl += dp[j]

        value_excl = dp[i-1]

        dp[i] = max(value_incl, value_excl)

    return dp[n-1]

def find_latest_non_overlapping(intervals, current_index):
    for j in range(current_index - 1, -1, -1):
        if intervals[j][1] <= intervals[current_index][0]:
            return j
    return -1

def input_intervals():
    n = int(input("Enter the number of intervals: "))
    intervals = []
    for i in range(n):
        start_time = int(input(f"Interval {i+1} start time: "))
        end_time = int(input(f"Interval {i+1} end time: "))
        value = int(input(f"Interval {i+1} value: "))
        intervals.append((start_time, end_time, value))
    return intervals

intervals = input_intervals()
max_value = weighted_interval_scheduling(intervals)
print(f"Maximum value subset of intervals: {max_value}")
