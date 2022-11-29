import uvicorn

uvicorn.run(
    'servisdb.app:app',
    reload=True
)