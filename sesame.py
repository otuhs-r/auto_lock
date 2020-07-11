from uuid import UUID
from pysesame2 import Sesame
import time
import RPi.GPIO as GPIO
import settings

def control_sesame(gpio_pin):
    # 誤検知で動くのを防ぐため、1秒同じ状態をキープしなければエッジとみなさない
    state = GPIO.input(gpio_pin)
    time.sleep(1)
    if GPIO.input(gpio_pin) != state:
        return

    if state == GPIO.HIGH:
        sesame.unlock()
    else:
        sesame.lock()

GPIO.setmode(GPIO.BCM)
GPIO.setup(settings.GPIO_PIN, GPIO.IN)
GPIO.add_event_detect(settings.GPIO_PIN, GPIO.BOTH, callback=control_sesame, bouncetime=500)
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
