from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import os
import time
import subprocess

def check_java_environment():
    try:
        result = subprocess.run(['java', '-version'], capture_output=True, text=True)
        if result.returncode == 0:
            print("Java доступна")
            return True
        else:
            print("Java не доступна")
            return False
    except Exception as e:
        print(f"Ошибка проверки Java: {e}")
        return False

def get_android_devices():
    try:
        result = subprocess.run(['adb', 'devices'], capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            lines = result.stdout.strip().split('\n')[1:]  # Пропускаем первую строку
            devices = []
            for line in lines:
                if line.strip() and '\tdevice' in line:
                    device_id = line.split('\t')[0]
                    devices.append(device_id)
            return devices
        return []
    except Exception as e:
        return []

def check_android_environment():
    try:
        android_home = os.environ.get('ANDROID_HOME') or os.environ.get('ANDROID_SDK_ROOT')
        if not android_home:
            print("ANDROID_HOME и ANDROID_SDK_ROOT не установлены")
            return False

        print(f"ANDROID_HOME: {android_home}")
        
        result = subprocess.run(['adb', 'version'], capture_output=True, text=True)
        if result.returncode != 0:
            print("ADB не доступен")
            return False
        
        print("ADB доступен")
        
        devices = get_android_devices()
        if not devices:
            print("Не найдено подключенных Android устройств")
            return False
        
        print(f"Найдены устройства: {devices}")
        return True
        
    except Exception as e:
        print(f"Ошибка проверки окружения: {e}")
        return False

def test_note_app():
    if not check_java_environment():
        return
    if not check_android_environment():
        return

    devices = get_android_devices()
    if not devices:
        print("Нет доступных устройств")
        return

    device_id = devices[0]

    current_dir = os.path.dirname(os.path.abspath(__file__))
    apk_path = os.path.join(current_dir, "NoteApp.apk")

    if not os.path.exists(apk_path):
        print("APK файл не найден!")
        return

    try:
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.device_name = device_id
        options.app = apk_path
        options.automation_name = "UiAutomator2"
        options.app_package = "com.example.noteapp"
        options.app_activity = ".MainActivity"
        options.auto_grant_permissions = True
        options.new_command_timeout = 120
        options.platform_version = "14.0"
        options.udid = device_id
        options.no_sign = True
        
        driver = webdriver.Remote('http://localhost:4723', options=options)

        time.sleep(15)

        edit_text = driver.find_element(AppiumBy.ID, "com.example.noteapp:id/editTextNote")
        edit_text.send_keys("Заметка из Appium")

        save_button = driver.find_element(AppiumBy.ID, "com.example.noteapp:id/buttonSave")
        save_button.click()

        time.sleep(5)
        
        print("Заметка успешно добавлена")
        
    except Exception as e:
        print(f"Тест не пройден: {e}")
        import traceback
        traceback.print_exc()
        
    finally:
        if 'driver' in locals():
            driver.quit()

if __name__ == "__main__":
    test_note_app()
