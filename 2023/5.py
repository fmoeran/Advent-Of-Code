with open("5.txt", "r") as f:
    arr = [line.strip() for line in f]

def make_range(start, end):
    return [start, end-start]

s = list(map(int, arr[0][6:].split()))
ranges = []
new_ranges = [s[i:i+2] for i in range(0, len(s), 2)]

for line in arr[1:]:
    if not line:
        continue
    if ":" in line:
        ranges.extend(new_ranges)
        new_ranges = []
    else:
        c_start, b_start, b_range = map(int, line.split())
        b_end = b_start + b_range
        update_ranges = []
        for a_start, a_range in ranges:
            a_end = a_start+a_range
            if b_start <= a_start <= b_end:
                if b_end <= a_end:
                    new_ranges.append(make_range(c_start+a_start-b_start, c_start+b_range))
                    if b_end != a_end:
                        update_ranges.append(make_range(b_end+1, a_end))
                else:
                    new_ranges.append(make_range(c_start+a_start-b_start, c_start+a_end-b_start))

            elif a_start<b_start and b_end<a_end:
                new_ranges.append([c_start, b_range])
                update_ranges.append(make_range(a_start, b_start-1))
                update_ranges.append(make_range(b_end+1, a_end))
            elif b_start <= a_end <= b_end:
                new_ranges.append(make_range(c_start, c_start+a_end-b_start))
                update_ranges.append(make_range(a_start, b_start-1))
            else:
                update_ranges.append([a_start, a_range])
        ranges = update_ranges

ranges.extend(new_ranges)
print(min(ranges, key=lambda x:x[0]))













