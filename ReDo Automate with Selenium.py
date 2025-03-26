# Required framework and library
import pyautogui
from tkinter import messagebox as msg
"Trying to automate the task using selenium"
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

# Set up the WebDriver (Edge in this example)
options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Suppress DevTools message
driver = webdriver.Chrome(options=options)


# Navigate to the result portal
driver.get("https://result.mdu.ac.in/postexam/result.aspx")

student_details = []

# Pause to ensure the page loads fully
pyautogui.sleep(1)
students_detail = [(2312051470,6071607,8076954807,"rajuyadav782760@gmail.com"),(2312051471,6071611,9115004409,"ritikyadav4409@gmail.com"),(2312051513,6071579,7982538645,"yadavnitin24821@gmail.com")]

for Registration_No,Roll_no,Phone_No,Email_ID in students_detail:
    try:

        # Locate the Registration No and Roll No fields and enter the data
        driver.find_element(By.ID, "txtRegistrationNo").send_keys(Registration_No)  # Replace with your Registration No
        driver.find_element(By.ID, "txtRollNo").send_keys(Roll_no)  # Replace with your Roll No

        # Submit the form
        driver.find_element(By.ID, "cmdbtnProceed").click()

        # Pause to let the results load
        pyautogui.sleep(3)
        driver.find_element(By.ID,"imgComfirm").click()
        pyautogui.sleep(4)

        view_link = driver.find_element(By.ID, "rptMain_ctl01_lnkView")  # Locate the element view and click on it
        view_link.click()

        pyautogui.sleep(5)


        student_name_element = driver.find_element(By.ID,"lblStudentName")
        student_name = student_name_element.text
        print(student_name)
        pyautogui.sleep(1)
        "Code for Printing the marksheet"

        # print_button = driver.find_element(By.ID,"btnPrint")
        # print_button.click()
        # pyautogui.sleep(3)
        # pyautogui.press('enter')
        # print("button is pressed")

        # pyautogui.moveTo(199,228)
        # print("Mouse is moved to the cordination")
        # pyautogui.click()
        # print("Mouse is clicked")
        # pyautogui.moveTo(199,235,0.3)
        # print("Mouse is moved to the cordination")

        # pyautogui.scroll(-200)
        # pyautogui.press('enter')
        # pyautogui.sleep(0.4)
        # pyautogui.write(str(student_name))
        # pyautogui.sleep(0.3)
        # pyautogui.press('enter')

        # driver.refresh()

        "Getting all data from the result window"
        father_name = driver.find_element(By.ID,"lblFatherName").text
        print(father_name)
        os_marks = driver.find_element(By.XPATH,"//table//tr[2]//td[8]").text
        ds_marks = driver.find_element(By.XPATH,"//table//tr[3]//td[8]").text
        database_marks = driver.find_element(By.XPATH,"//table//tr[4]//td[8]").text
        comm_skill_marks = driver.find_element(By.XPATH,"//table//tr[5]//td[8]").text
        sw_lab_marks = driver.find_element(By.XPATH,"//table//tr[6]//td[8]").text

        data = {"Operating System" : os_marks,
                "Data Structure-I " : ds_marks,
                "Database " : database_marks,
                "Communication Skill" :comm_skill_marks,
                "software Lab" : sw_lab_marks
                }

        student_details.append(data)
        pyautogui.sleep(1)
        driver.refresh()
        pyautogui.sleep(2)
    except Exception as e:
        print(f"Error is occured In {Registration_No} and \nError is {e}")

print(student_details)

pyautogui.sleep(20)


# Close the browser
driver.quit()

