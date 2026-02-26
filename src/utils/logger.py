def log(message: str, request_id: str = None):
    prefix = f"[{request_id}] " if request_id else ""
    print(prefix + message)
