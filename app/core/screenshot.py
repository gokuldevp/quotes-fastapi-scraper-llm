import os
from datetime import datetime
from app.core.config import SCREENSHOTS_DIR

def take_screenshot(driver, prefix="error"):
    os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    filename = f"screenshots/{prefix}_{timestamp}.png"

    driver.save_screenshot(filename)
    return filename
