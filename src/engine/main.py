import uvicorn

from engine.configs.common import GlobalSettings, AppSettings
from engine.utils.logger_config import set_logger_config

if __name__ == "__main__":
    set_logger_config()
    settings = GlobalSettings(app=AppSettings())
    uvicorn.run("engine.server.app:app", host=settings.app.host, port=settings.app.port, reload=settings.app.reload)
