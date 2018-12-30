'''
You have 2 laundromats - L1, L2
To use L1, you need to pay a flat fee of r per load (r * l) per week
To use L2, you need to pay a flat fee of w per 3 weeks regardless of the load (w * 3)
Given a list of weekly load values, find a sequence of 
Landromat schedules that minimizes the cost
'''

import math

def laundromat(r, w, loads):
    min_vals = [None] * len(loads)
    schedule = []

    def laundromat_rec(load, i):
        if i < 0:
            return 0
        if i == 0:
            if (not min_vals[i]):
                min_vals[i] = r * load[i]
                schedule.append("L1")
            return min_vals[i]
        elif i == 1:
            if (not min_vals[i]):
                min_vals[i] = r * load[i] + laundromat_rec(load[:-1], i - 1)
                schedule.append("L1")
            return min_vals[i]
        else:
            if min_vals[i] is None:
                with_r = r * load[i] + laundromat_rec(load[:-1], i - 1)
                with_w = w * 3 + laundromat_rec(load[:-3], i - 3)
                if with_r < with_w:
                    min_vals[i] = with_r
                    schedule.append("L1")
                else:
                    min_vals[i] = with_w
                    schedule.append("L2")
                return min_vals[i]
            else:
                return min_vals[i]
    
    for i in range(0, len(loads)):
        laundromat_rec(loads, i)
    
    print(schedule)
    print(min_vals)

    return
                
laundromat(10, 80, [5,8,10,11,9,6,7])
laundromat(10, 80, [90, 99, 90, 2000])
