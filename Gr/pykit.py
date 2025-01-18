import sy
import time
if system().lower() in ("windows", "darwin"):
    from PIL import ImageGrab

    def take_screenshot(
        file_name: str = "pywhatkit_screenshot", delay: int = 2, show: bool = True
    ) -> None:
        """Take Screenshot of the Screen"""

        time.sleep(delay)
        screen = ImageGrab.grab()
        if show:
            screen.show(title=file_name)
        screen.save(f"{file_name}.png")

take_screenshot()
print("taking screenshot")