from celery.task import task

@task
def fav_doctor():
    with open('doctor.txt', 'r+') as f:
        for line in f:
            nums = line.rstrip().split()

            print 'The {} doctor is my favorite'.format(nums[0])

            for num in nums[1:]:
                print 'Wait! its {} doctor is my favorite'.format(num)

            last_num = int(nums[-1])
            new_last_num = last_num + 1

            f.write(str(new_last_num) + ' ')
