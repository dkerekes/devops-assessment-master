# FastAPI for simple API request and appropriate exepions.
from fastapi import FastAPI, HTTPException

# BaseModel to concert RestAPI paramethers to Python objects.
from pydantic import BaseModel

# To reach the environment variables in the OS.
import os

# Starts a FastAPI instance.
my_app = FastAPI(title="Config API", version="1.0.0")

# In-memory configuration storage.
# Python empty map variable, accepts key-value pairs.
# Exaple: config_store["foo"] = "bar"
config_store = {}

# Class to store configuration data.
class ConfigItem(BaseModel):
    name: str
    value: str

# Simple health check endpoint. Does not conway the inner state of the application only that it is running.
@my_app.get("/health")
def health():
    return {"status": "ok"}

# Returns appplication version.
@my_app.get("/version")
def version():
    return {"version": my_app.version}

# Returns environment variable read from the container where this app runs.
@my_app.get("/env")
def environment():
    return {
        "environment": os.getenv("ENVIRONMENT", "")
    }

# Accepts a key value pair and appends it to the config_store map.
# If the key already exists, it will overwrite the value with the new one.
# Retunrs the read in ConfigItem as confirmation.
@my_app.post("/config")
def create_config(config: ConfigItem):
    config_store[config.name] = config.value
    return config

# Tryies to read an entry from storage and return it.
# Raises error if key is not found.
@my_app.get("/config/{name}")
def get_config(name: str):
    if name not in config_store:
        raise HTTPException(
            status_code=404,
            detail="Configuration not found"
        )

    return {
        "name": name,
        "value": config_store[name]
    }

# Tryies to delete an entry from storage.
# Raises error if key is not found.
@my_app.delete("/config/{name}")
def delete_config(name: str):
    if name not in config_store:
        raise HTTPException(
            status_code=404,
            detail="Configuration not found"
        )

    del config_store[name]
    return {"deleted": True}
