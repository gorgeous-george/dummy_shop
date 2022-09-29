from celery import shared_task


@shared_task
def add(x, y):
    return x + y

# todo: add task to receive left_in_stock from storage