import os

import uvicorn


def serve():
    import sys

    reload = "--reload" in sys.argv
    HOST = os.getenv("API_HOST", "0.0.0.0")
    PORT = int(os.getenv("API_PORT", "8080"))
    uvicorn.run("app.server:app", host=HOST, port=PORT, reload=reload)
