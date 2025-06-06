from pydantic import BaseModel
from pathlib import Path

class Config(BaseModel):
    """Plugin Config Here"""
    screen_shot_blur_radius: int = 10
    temp_screen_shot_path: Path = Path.cwd() / "Temp" / "ScreenShot"
    stalk_name: str = "Fresca"