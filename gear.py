import math

def find_teeth(num_total):
    print("For {} teeth total:".format(num_total))
    ratios = [
        0.6147625725,
        0.2407500588,
        1,
        1.881383749
    ]

    values = []
    for b in range(1, num_total):
        a = num_total - b
        c = a/b

        values.append((a, b, c))

    sum_diff = 0
    for r in ratios:
        best_match = min(values, key=lambda x: abs(r-x[2]))
        diff = abs(r - best_match[2])
        sum_diff += diff
        print("Ratio {}, Actual {}, Diff {}, g1:{}, g2:{}".format(r, best_match[2], diff, best_match[0], best_match[1]))

    print(sum_diff)

import heapq

def stacky_mcstackerson(desired_ratio, g1_tooth_count):
        g2_tooth_range = range(12, 60)
        g3_tooth_range = range(12, 60)
        g4_tooth_range = range(12, 60)
        g5_tooth_range = range(12, 60)
        ratio_with_tooth_counts = []
        for g2_tooth_count in g2_tooth_range:

            ratio_a = g1_tooth_count / g2_tooth_count
            print("G2 Tooth Count: {}".format(g2_tooth_count))

            for g3_tooth_count in g3_tooth_range:

                for g4_tooth_count in g4_tooth_range:

                    ratio_b = g3_tooth_count/g4_tooth_count

                    for g5_tooth_count in g5_tooth_range:

                        #g5 + g6 < g1
                        minimum_possible_g6_count = max(g1_tooth_count - g5_tooth_count, 12)
                        g6_tooth_range = range(minimum_possible_g6_count, 60)
                        for g6_tooth_count in g6_tooth_range:
                            ratio_c = g5_tooth_count / g6_tooth_count

                            total_ratio = ratio_a * ratio_b * ratio_c
                            diff = abs(desired_ratio - total_ratio)
                            gear_object = (1/diff,
                                            diff,
                                            total_ratio,
                                            g1_tooth_count,
                                            g2_tooth_count,
                                            g3_tooth_count,
                                            g4_tooth_count,
                                            g5_tooth_count,
                                            g6_tooth_count)
                            if len(ratio_with_tooth_counts) > 10:
                                heapq.heappushpop(ratio_with_tooth_counts, gear_object)
                            else:
                                ratio_with_tooth_counts.append(gear_object)
            sorted_ratios = sorted(ratio_with_tooth_counts, key=lambda x: x[0])

            print("Best thus far: {}".format(sorted_ratios[0]))

        sorted_ratios = sorted(ratio_with_tooth_counts, key=lambda x: x[0])

        for i in sorted_ratios:

            print(i)


def find_stack_values():
    g1_teeth = 50
    desired_ratio = 0.6666670913
    tooth_restriction = True
    ratios = []
    min_teeth = 12
    max_teeth = 60
    max_output_gear_size = 60

    available_range = range(min_teeth, max_teeth)
    if tooth_restriction:
        min_tooth_restriction = max(g1_teeth + min_teeth, 66)
        max_tooth_restriction = 66
        available_range = range(min_tooth_restriction - g1_teeth, max_tooth_restriction - g1_teeth + 1)

    for i in available_range:
        ratio = g1_teeth / i
        total = g1_teeth + i

        new_desired_ratio = desired_ratio / ratio
        for j in range(min_teeth, total - min_teeth):
            g1 = j
            g2 = total - j

            if g2 > max_output_gear_size:
                continue

            total_ratio = ratio * (g1/g2)

            diff = abs(total_ratio - desired_ratio)

            obj_storage = (diff, g1_teeth, i, g1, g2)
            ratios.append(obj_storage)
            #print ("g1a: {} g2a: {} g1b: {} g2b: {}")

    sorted_values = sorted(ratios, key=lambda x: x[0])
    count = 0
    for i in sorted_values:
        if count > 10:
            break
        total = i[1] + i[2]
        diff = i[0]
        ratio = (i[1] / i[2]) * (i[3] / i[4])
        print("Total: {} Diff: {} Ratio: {} Gears: {} {} {} {}".format(total, diff, ratio,  i[1], i[2], i[3], i[4]))
        count += 1

stacky_mcstackerson(0.4575999209, 52)
#find_stack_values()

# 100
# 50 50 - 1.0
# 33 67 - .5
#

# where a / b = c
# a + b = 100
