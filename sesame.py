from uuid import UUID
from pysesame2 import Sesame
import time
import RPi.GPIO as GPIO
import settings

def close_sesame(_gpio_pin):
    if not sesame.get_status()['locked']:
        sesame.lock()

GPIO.setmode(GPIO.BCM)
GPIO.setup(settings.GPIO_PIN, GPIO.IN)
GPIO.add_event_detect(settings.GPIO_PIN, GPIO.FALLING, callback=close_sesame, bouncetime=500)
sesame = Sesame(UUID(settings.SESAME_DEVICE_ID), settings.SESAME_AUTH_TOKEN)

if __name__ == '__main__':
    try:
        while True:
            time.sleep(settings.INTERVAL_SEC)
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.remove_event_detect(settings.GPIO_PIN)
        GPIO.cleanup()
