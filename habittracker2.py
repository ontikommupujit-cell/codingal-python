habit_info=("Reading",True,7,20.5)
print(habit_info)
weekly_habits=(1,0,1,1,0,1,1)
print(weekly_habits)
print("Total days tracked:",len(weekly_habits))
print("Day 1 status:",weekly_habits[0])
print("Day 4 status:",weekly_habits[3])
first_three_days=weekly_habits[0:3]
print("First three days:",first_three_days)
weekend_days=weekly_habits[5:7]
print("Weekend days:",weekend_days)
print("Reversed record:",weekly_habits[::-1])
weekly_habits=weekly_habits+(1,)
print("After adding one more day:",weekly_habits)
completed=weekly_habits.count(1)
missed=weekly_habits.count(0)
print("Completed days:",completed)
print("Missed days:",missed)
done=0
not_done=0
for day in weekly_habits:
    if day==1:
        done+=1
    else:
        not_done+=1
completion_rate=(done/len(weekly_habits))*100
if done>not_done:
    message="Great habit progress!"
else:
    message="Try to be more consistent!"
print(message)
print("")
print("===== WEEKLY HABIT TRACKER =====")
print("Habit Name:",habit_info[0])
print("Habit Active:",habit_info[1])
print("Target Days:",habit_info[2])
print("Average Minutes:",habit_info[3])
print("Weekly Record:",weekly_habits)
print("Completed:",done)
print("Missed:",not_done)
print("Completion Rate:",round(completion_rate,2),"%")
print("================================")