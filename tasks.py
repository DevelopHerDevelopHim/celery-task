from celery.task import task

@task
def multiply(x,y):
	multiplication = x * y
	return "The result is " + str(multiplication)