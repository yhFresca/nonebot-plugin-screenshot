from .config import *
from nonebot import get_plugin_config

pc = get_plugin_config(Config)

from PIL import Image, ImageFilter, ImageGrab
from nonebot import logger as log
import base64
from io import BytesIO

def getScreenShot():
    log.info("正在截图")
    screenshot = ImageGrab.grab()
    blurred_image = screenshot.filter(ImageFilter.GaussianBlur(radius=pc.screen_shot_blur_radius))
    
    pc.temp_screen_shot_path.mkdir(parents=True, exist_ok=True)
    blurred_image.save(pc.temp_screen_shot_path / 'pic.png')
    log.success(f"毛玻璃截图保存在{pc.temp_screen_shot_path / 'pic.png'}")

def image_to_base64(img: Image.Image, format='PNG') -> str:
    output_buffer = BytesIO()
    img.save(output_buffer, format)
    byte_data = output_buffer.getvalue()
    base64_str = base64.b64encode(byte_data).decode()
    return 'base64://' + base64_str

from nonebot import on_command
from nonebot.adapters.onebot.v11 import MessageSegment

stalk = on_command(f'视奸{pc.stalk_name}')

@stalk.handle()
async def _():
    getScreenShot()
    await stalk.finish(
        MessageSegment.image(
            image_to_base64(Image.open(pc.temp_screen_shot_path / 'pic.png'))
        ), 
        reply_message=True
    )