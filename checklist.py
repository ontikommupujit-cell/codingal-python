chores=["washing dishes","vacuming","laundry","setting up the table","filling up the waterbottles"]
count=len(chores)
print('you have ',count,'chores to finish today')
completed_count=0
while len(chores)>0:
    next_chores=chores[0]
    answer=input("have you finished"+next_chores+"?(yes/no):")
    if answer==('yes'):
        chores.pop(0)
        completed_count=completed_count +1
        print('great job, 1 chore is done')
    else:
        print('ok now finish it and check again')
    print('chores remaining:',len(chores))
    print("")
print('all chores completed')
print('great work completeing your checklist today')
print('')
print('')
print('')
#infinte loop starts from here
print('lets safely peek at our infinite loop')
test_value=0 
safety_counter=0
while test_value <=0:
    print('the condition never changes so this loop will go on forever')
    safety_counter+=1
    if safety_counter==3:
        print('stoping here on purpose a real infinite loop never stops on its own')
        break
print('')
print(' ========code checklist summery=======')
print('chores assigned today',count)
print('completed chores',completed_count)
print('chores remaining',len(chores))
print('=====================================================================')

