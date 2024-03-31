from .models import ActivityLog

def add_activity_log(service, timestamp, action):
    """
    Function to add a new activity log to the database.

    Parameters:
    - service: Name of the microservice generating the log.
    - timestamp: Timestamp of the log.
    - action: Action performed.

    Returns:
    - new_log: The newly created ActivityLog object.
    """
    new_log = ActivityLog(service=service, timestamp=timestamp, action=action)
    new_log.save()
    return new_log

def get_all_activity_logs():
    """
    Function to retrieve all activity logs from the database.

    Returns:
    - logs: List of all ActivityLog objects in the database.
    """
    logs = ActivityLog.objects()
    return logs
