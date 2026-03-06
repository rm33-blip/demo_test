from src.libraries.common_utils import format_log_line


def log(message: str, request_id: str = None):
    prefix = f"[{request_id}] " if request_id else ""
    print(prefix + message)


def log_structured(message: str, request_id: str = None, fields: dict = None, structured: bool = False):
    if not structured:
        log(message, request_id=request_id)
        return

    payload = {"request_id": request_id, "message": message}
    if fields:
        payload.update(fields)

    print(format_log_line(message="event", fields=payload))
