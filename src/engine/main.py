import uvicorn

from engine.configs.common import GlobalSettings, AppSettings

if __name__ == "__main__":
    settings = GlobalSettings(app=AppSettings())
    uvicorn.run("engine.server.app:app", host=settings.app.host, port=settings.app.port, reload=settings.app.reload)
