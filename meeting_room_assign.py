n = int(input())
meet_list = []

for _ in range(n):
    # pass

# print(meet_list)
# meet_list.sort(key=lambda x: (x[1], x[0]))
meet_list.sort()
# print(meet_list)

result_meet_cnt = 1
last_meet_end_time = meet_list[0][0]

for meet in meet_list:
    end_time, start_time = meet

    ## pass

print(result_meet_cnt)