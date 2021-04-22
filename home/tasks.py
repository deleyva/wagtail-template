from celery import shared_task


@shared_task
def count_hompage():
    print('¿Se ve?')
    return "ouuuu mama"