import cv2
import pyautogui
import time

def find_and_click(image_path):
    while True:
        # 加载要查找的图像
        template = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        # 获取屏幕截图
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.png")
        screenshot = cv2.imread("screenshot.png", cv2.IMREAD_GRAYSCALE)

        # 使用模板匹配定位图像
        result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        threshold = 0.8  # 设置阈值，匹配结果大于该值时认为找到了目标
        if max_val >= threshold:
            top_left = max_loc
            h, w = template.shape

            # 计算中心点坐标
            center_x = top_left[0] + w // 2
            center_y = top_left[1] + h // 2

            # 移动鼠标并点击
            pyautogui.moveTo(center_x, center_y)
            pyautogui.click()
        else:
            time.sleep(1)  # 没有找到目标时，等待一秒继续检测

if __name__ == "__main__":
    image_path = "pokedback.png"  # 需要点击的元素的图像路径
    find_and_click(image_path)
