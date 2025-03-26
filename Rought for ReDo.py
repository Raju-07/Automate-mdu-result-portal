import time
import pyautogui
import webbrowser
from tkinter import messagebox as msg
# students_detail = [(2312051470,6071607,8076954807,"rajuyadav782760@gmail.com"),(2312051471,607612,9115004409,"ritikyadav4409@gmail.com")]
# for i in range(len(students_detail)):
#     registration_no = students_detail[i][0]
#     roll_no = students_detail[i][1]
#     phone_no = students_detail[i][2]
#     email_id = students_detail[i][3]
#     print(f"{registration_no = }  {roll_no = }  {phone_no = }  {email_id = }")

# #     time.sleep(5.0)
print(pyautogui.position())
pyautogui.scroll(-200)
exit()
"Optimized approach for this task "

# students_detail = [(2312051470,6071607,8076954807,"rajuyadav782760@gmail.com"),(2312051471,607612,9115004409,"ritikyadav4409@gmail.com")]

# for Registration_No,Roll_no,Phone_No,Email_ID in students_detail:
#     pyautogui.write(str(Registration_No))
    

# webbrowser.open(url="https://result.mdu.ac.in/postexam/result.aspx")

# "Finding the cordinate for filling the data"
# time.sleep(5)
# print(pyautogui.position())

"Implimenting the code for adding more details "
# more_detail = msg.askquestion("More Details","Do we need more details for Result")
# if more_detail == "yes":
#     print("Yes we need more details ")
# else:
#     print("No, We don't need any other details")

# print("Hello World!")


# print(pyautogui.position())

"Write code for Copying the name of the students for saving the file uniquely"
# time.sleep(5)
# pyautogui.doubleClick(537,435)
# pyautogui.hotkey('ctrl','c')
# pyautogui.sleep(3)
# pyautogui.hotkey('ctrl','v')


"Using slanium for getting name here"
# from selenium import webdriver

# # Open the browser
# driver = webdriver.edge()
# driver.get('YOUR_WEBPAGE_URL')  # Replace with the URL of the webpage

# # Find the element containing the name
# student_name = driver.find_element('xpath', 'XPATH_OF_THE_NAME')  # Replace with the actual XPath
# print("Student Name:", student_name.text)

# # Optionally, you can copy it to the clipboard (using pyperclip or similar libraries)
# import pyperclip
# pyperclip.copy(student_name.text)
# print("Copied to clipboard!")

"Trying to automate the task using selenium"
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver (Edge in this example)

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Suppress DevTools message


driver = webdriver.Edge(options=options)


# Navigate to the result portal
driver.get("https://result.mdu.ac.in/postexam/result.aspx")

# Pause to ensure the page loads fully
time.sleep(1)

# Locate the Registration No and Roll No fields and enter the data
driver.find_element(By.ID, "txtRegistrationNo").send_keys("2312051470")  # Replace with your Registration No
driver.find_element(By.ID, "txtRollNo").send_keys("6071607")  # Replace with your Roll No

# Submit the form
driver.find_element(By.ID, "cmdbtnProceed").click()

# Pause to let the results load
time.sleep(3)

driver.find_element(By.ID,"imgComfirm").click()

time.sleep(4)

# Optional: Locate and download the result file if available
# For example, if the download link has an ID

view_link = driver.find_element(By.ID, "rptMain_ctl01_lnkView")  # Locate the element again
view_link.click()

# view_link = driver.find_element(By.ID, "rptMain_ctl01_lnkView").click()

# print("Link text:", view_link.text)  # Check if the link is located and visible
# print("Is displayed:", view_link.is_displayed())  # Ensure the element is visible on the page
# print("Is enabled:", view_link.is_enabled())  # Ensure the element is not disabled

"Handling the click on view with pyautogui"
# pyautogui.moveTo(1018,190)
# pyautogui.click(1018,190)

# view_link = driver.find_element(By.ID, "rptMain_ctl01_lnkView")
# driver.execute_script("arguments[0].scrollIntoView(); arguments[0].focus();", view_link)
# view_link.click()

time.sleep(5)
# driver.implicitly_wait(10)

student_name_element = driver.find_element(By.ID,"lblStudentName")
student_name = student_name_element.text
print(student_name)
time.sleep(1)
"Code for Printing the marksheet"

print_button = driver.find_element(By.ID,"btnPrint").click()
time.sleep(1)
pyautogui.press('enter')
time.sleep(0.4)
pyautogui.write(str(student_name))
time.sleep(0.3)
pyautogui.press('enter')

driver.refresh()

time.sleep(20)


# Close the browser
driver.quit()

