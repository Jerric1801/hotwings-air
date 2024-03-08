from .models import ErrorLog
from datetime import datetime
import uuid

# Service to add a new error log
def add_error_log(flight_id, user_email, error_description):
    log_id = str(uuid.uuid4())  # Generate a unique log ID
    date_time = datetime.now()  # Get the current date and time

    # Create a new ErrorLog instance
    error_log = ErrorLog(
        log_id=log_id,
        date_time=date_time,
        flight_id=flight_id,
        user_email=user_email,
        error_description=error_description
    )
    # Save the error log to the database
    error_log.save()
    return error_log

# Service to retrieve all error logs
def get_all_error_logs():
    # Retrieve all error logs from the database
    error_logs = ErrorLog.objects.all()
    return error_logs