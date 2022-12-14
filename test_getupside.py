from addons.generate_random_email import GenerateRandomEmail
from addons.visible_elements_operations import VisibleElementsOperations
from selenium.webdriver.common.by import By
from src.testproject.classes import DriverStepSettings, StepSettings
from src.testproject.decorator import report_assertion_errors
from src.testproject.enums import SleepTimingType
from src.testproject.sdk.drivers import webdriver
from subtests import test_bypass_handler
from subtests import test_logout
import pytest


"""
This pytest test was automatically generated by TestProject
    Project: Upside
    Package: TestProject.Generated.Tests.Upside
    Test: GetUpside
    Generated by: Christopher Wamble (cwsite.ma@gmail.com)
    Generated on 08/04/2022, 21:03:11
"""


@pytest.fixture()
def driver():
    capabilities = {
        "platformName": "Android",
        "udid": "09171JECB09072",
    }
    driver = webdriver.Remote(token="x6OtdGenIPjPU1c53S1LjlYCBDo5Cty5HVPGqe-Gndk1",
                              project_name="Upside",
                              job_name="GetUpside",
                              desired_capabilities=capabilities)
    step_settings = StepSettings(timeout=15000,
                                 sleep_time=500,
                                 sleep_timing_type=SleepTimingType.Before)
    with DriverStepSettings(driver, step_settings):
        yield driver
    driver.quit()


@report_assertion_errors
def test_main(driver):
    # Test Parameters
    email = ""

    # 1. Reset App
    # Clear application data and restart (Auto-generated)
    driver.reset()

    # 2. Click 'Sign up with email'
    # select to sign up with email
    sign_up_with_email = driver.find_element(By.ID,
                                             "com.upside.consumer.android.beta:id/login_sing_up_email_b")
    sign_up_with_email.click()

    # 3. Run Random Email Generator
    # call upon custom addon created by me in TestProject to generate a random unique email address
    step_output = driver.addons().execute(
        GenerateRandomEmail.generateemail(
            emailTag="testa",
            domain="myyahoo.com"))
    email = step_output

    # 4. Type '{email}' in 'com.upside.consumer.android.beta:id/s...'
    # enter random email address into email address field
    com_upside_consumer_android_beta_colon_id_slash_s_ = driver.find_element(By.ID,
                                                                             "com.upside.consumer.android.beta:id/sign_up_email_edit_et")
    com_upside_consumer_android_beta_colon_id_slash_s_.send_keys(f'{email}')

    # 5. Type 'Password1!' in 'com.upside.consumer.android.beta:id/s...1'
    # enter in a password
    com_upside_consumer_android_beta_colon_id_slash_s_1 = driver.find_element(By.ID,
                                                                              "com.upside.consumer.android.beta:id/sign_up_password_edit_et")
    com_upside_consumer_android_beta_colon_id_slash_s_1.send_keys("Password1!")

    # 6. Click 'Create account'
    # submit credentials
    create_account = driver.find_element(By.ID,
                                         "com.upside.consumer.android.beta:id/sign_up_email_b")
    create_account.click()

    # 7. Does 'A few more
    # details' contain 'A few more
    # details'?
    # validate next screen appears
    a_few_more_details = driver.find_element(By.ID,
                                             "com.upside.consumer.android.beta:id/account_details_title_tv")
    step_output = a_few_more_details.text
    assert step_output and ("A few more\ndetails" in step_output)

    # 8. Click 'Create account' if it's visible
    # move on with onboarding process
    create_account = (
        By.ID, "com.upside.consumer.android.beta:id/sign_up_email_b")
    driver.addons().execute(
        VisibleElementsOperations.clickifvisibleandroid(
            timeout=""), *create_account)

    # 9. Click 'Not Now' if it's visible
    # bypass the request for further data
    not_now = (
        By.ID, "com.upside.consumer.android.beta:id/permissions_negative_action_b")
    driver.addons().execute(
        VisibleElementsOperations.clickifvisibleandroid(
            timeout=""), *not_now)

    '''
    # (STEP DISABLED)
    # 10. Click 'Not Now' if it's visible
    # bypass the request for further data
    not_now = (By.ID, "com.upside.consumer.android.beta:id/permissions_negative_action_b")
    driver.addons().execute(
    VisibleElementsOperations.clickifvisibleandroid(
    timeout = ""), *not_now)
    '''

    # 11. This test was auto generated from steps of the 'GetUpside' test
    # This step was auto generated from several steps
    step_settings = StepSettings(sleep_time=6000,
                                 sleep_timing_type=SleepTimingType.Before)
    with DriverStepSettings(driver, step_settings):
        test_bypass_handler.test_main(driver)

    # 12. Is 'Search' visible?
    # validate use has reached the map screen
    try:
        search = driver.find_element(By.ID,
                                     "com.upside.consumer.android.beta:id/places_autocomplete_search_button")
        assert search.is_displayed()
    except Exception:
        # Failure Behaviour: RecoveryContinue
        pass

    # 13. This test was auto generated from steps of the 'GetUpside' test
    # logout from map screen
    test_logout.test_main(driver)
