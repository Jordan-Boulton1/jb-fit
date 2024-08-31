# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| about | about.html | ![screenshot](documentation/testing/validation/html/html-validation-about.png) | Pass: No Errors |
| accounts | add_weight_log.html | ![screenshot](documentation/testing/validation/html/html-validation-add-weight-log.png) | Pass: No Errors |
| accounts | edit_profile.html | ![screenshot](documentation/testing/validation/html/html-validation-profile-edit.png) | Pass: No Errors |
| accounts | edit_weight_log.html | ![screenshot](documentation/testing/validation/html/html-validation-edit-weight-log.png) | Pass: No Errors |
| accounts | profile.html | ![screenshot](documentation/testing/validation/html/html-validation-profile.png) | Pass: No Errors |
| accounts | signup.html | ![screenshot](documentation/testing/validation/html/html-validation-signup.png) | I am aware of this error from the validator and is happening due to allauth. I have attempted to remove the `aria-describedby` in the signup form however I was unable to fix it for that reason error will still show up in the validator. |
| checkout | checkout.html | ![screenshot](documentation/testing/validation/html/html-validation-checkout.png) | Pass: No Errors |
| checkout | checkout_success.html | ![screenshot](documentation/testing/validation/html/html-validation-checkout-success.png) | Pass: No Errors |
| contact | contact_form.html | ![screenshot](documentation/testing/validation/html/html-validation-home.png) | Pass: No Errors - Contact form is on every page. |
| faq | faq.html | ![screenshot](documentation/testing/validation/html/html-validation-faq.png) | Pass: No Errors |
| home | home.html | ![screenshot](documentation/testing/validation/html/html-validation-home.png) | Pass: No Errors |
| plans | plans.html | ![screenshot](documentation/testing/validation/html/html-validation-plans.png) | Pass: No Errors |
| | logout.html | ![screenshot](documentation/testing/validation/html/html-validation-logout.png) | Pass: No Errors |
| | login.html | ![screenshot](documentation/testing/validation/html/html-validation-login.png) | Pass: No Errors |
| | password_reset.html | ![screenshot](documentation/testing/validation/html/html-validation-password-reset.png) | Pass: No Errors |
| | password_reset_done.html | ![screenshot](documentation/testing/validation/html/html-validation-password-reset-done.png) | Pass: No Errors |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| accounts | profile.css | ![screenshot](documentation/testing/validation/css/css-validation-profile.png) | Pass: No Errors |
| checkout | checkout.css | ![screenshot](documentation/testing/validation/css/css-validation-checkout.png) | Pass: No Errors |
| plans | plans.css | ![screenshot](documentation/testing/validation/css/css-validation-plans.png) | Pass: No Errors |
| static | base.css | ![screenshot](documentation/testing/validation/css/css-validation-base.png) | Pass: No Errors |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| about | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jordan-Boulton1/jb-fit/main/about/urls.py) | ![screenshot](documentation/testing/validation/python/about/python-validation-about-urls.png) | |
| about | test_urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jordan-Boulton1/jb-fit/main/about/tests/test_urls.py) | ![screenshot](documentation/testing/validation/python/about/python-validation-about-test-urls.png) | |
| about | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jordan-Boulton1/jb-fit/main/about/views.py) | ![screenshot](documentation/testing/validation/python/about/python-validation-about-views.png) | |
| about | test_views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jordan-Boulton1/jb-fit/main/about/tests/test_views.py) | ![screenshot](documentation/testing/validation/python/about/python-validation-about-test-views.png) | |
| accounts | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jordan-Boulton1/jb-fit/main/accounts/admin.py) | ![screenshot](documentation/testing/validation/python/accounts/python-validation-accounts-admin.png) | |
| accounts | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jordan-Boulton1/jb-fit/main/accounts/forms.py) | ![screenshot](documentation/testing/validation/python/accounts/python-validation-accounts-forms.png) | |
| accounts | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jordan-Boulton1/jb-fit/main/accounts/models.py) | ![screenshot](documentation/testing/validation/python/accounts/python-validation-accounts-models.png) | |
| accounts | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jordan-Boulton1/jb-fit/main/accounts/urls.py) | ![screenshot](documentation/testing/validation/python/accounts/python-validation-accounts-urls.png) | |
| accounts | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jordan-Boulton1/jb-fit/main/accounts/views.py) | ![screenshot](documentation/testing/validation/python/accounts/python-validation-accounts-views.png) | |
| accounts | test_forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jordan-Boulton1/jb-fit/main/accounts/tests/test_forms.py) | ![screenshot](documentation/testing/validation/python/accounts/python-validation-accounts-test-forms.png) | |
| accounts | test_models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jordan-Boulton1/jb-fit/main/accounts/tests/test_models.py) | ![screenshot](documentation/testing/validation/python/accounts/python-validation-accounts-test-models.png) | |
| accounts | test_urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jordan-Boulton1/jb-fit/main/accounts/tests/test_urls.py) | ![screenshot](documentation/testing/validation/python/accounts/python-validation-accounts-test-urls.png) | |
| accounts | test_views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jordan-Boulton1/jb-fit/main/accounts/tests/test_views.py) | ![screenshot](documentation/testing/validation/python/accounts/python-validation-accounts-test-views.png) | |
| checkout | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jordan-Boulton1/jb-fit/main/checkout/forms.py) | ![screenshot](documentation/testing/validation/python/checkout/python-validation-checkout-views.png) | |
| checkout | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jordan-Boulton1/jb-fit/main/checkout/models.py) | ![screenshot](documentation/testing/validation/python/checkout/python-validation-checkout-models.png) | |
| checkout | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jordan-Boulton1/jb-fit/main/checkout/urls.py) | ![screenshot](documentation/testing/validation/python/checkout/python-validation-checkout-urls.png) | |
| checkout | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jordan-Boulton1/jb-fit/main/checkout/views.py) | ![screenshot](documentation/testing/validation/python/checkout/python-validation-checkout-views.png) | |
| checkout | webhooks.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jordan-Boulton1/jb-fit/main/checkout/webhooks.py) | ![screenshot](documentation/testing/validation/python/checkout/python-validation-checkout-views.png) | |
| contact | context_processors.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jordan-Boulton1/jb-fit/main/contact/context_processors.py) | ![screenshot](documentation/testing/validation/python/contact/python-validation-contact-context-processors.png) | |
| contact | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jordan-Boulton1/jb-fit/main/contact/forms.py) | ![screenshot](documentation/testing/validation/python/contact/python-validation-contact-forms.png) | |
| contact | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jordan-Boulton1/jb-fit/main/contact/models.py) | ![screenshot](documentation/testing/validation/python/contact/python-validation-contact-models.png) | |
| contact | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jordan-Boulton1/jb-fit/main/contact/urls.py) | ![screenshot](documentation/testing/validation/python/contact/python-validation-contact-urls.png) | |
| contact | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jordan-Boulton1/jb-fit/main/contact/views.py) | ![screenshot](documentation/testing/validation/python/contact/python-validation-contact-views.png) | |
| contact | test_forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jordan-Boulton1/jb-fit/main/contact/tests/test_forms.py) | ![screenshot](documentation/testing/validation/python/contact/python-validation-contact-test-forms.png) | |
| contact | test_models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jordan-Boulton1/jb-fit/main/contact/tests/test_models.py) | ![screenshot](documentation/testing/validation/python/contact/python-validation-contact-test-models.png) | |
| contact | test_urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jordan-Boulton1/jb-fit/main/contact/tests/test_urls.py) | ![screenshot](documentation/testing/validation/python/contact/python-validation-contact-test-urls.png) | |
| contact | test_views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jordan-Boulton1/jb-fit/main/contact/tests/test_views.py) | ![screenshot](documentation/testing/validation/python/contact/python-validation-contact-test-views.png)
|  | custom_storages.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jordan-Boulton1/jb-fit/main/custom_storages.py) | ![screenshot](documentation/testing/validation/python/python-validation-custom-storages.png) | |
| faq | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jordan-Boulton1/jb-fit/main/faq/urls.py) | ![screenshot](documentation/testing/validation/python/faq/python-validation-faq-urls.png) | |
| faq | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jordan-Boulton1/jb-fit/main/faq/views.py) | ![screenshot](documentation/testing/validation/python/faq/python-validation-faq-views.png) | |
| faq | test_urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jordan-Boulton1/jb-fit/main/faq/tests/test_urls.py) | ![screenshot](documentation/testing/validation/python/faq/python-validation-faq-test-urls.png) | |
| faq | test_views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jordan-Boulton1/jb-fit/main/faq/tests/test_views.py) | ![screenshot](documentation/testing/validation/python/faq/python-validation-faq-test-views.png) | |
| jb_fit | settings.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jordan-Boulton1/jb-fit/main/jb_fit/settings.py) | ![screenshot](documentation/testing/validation/python/jb_fit/python-validation-settings.png) | |
| jb_fit | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jordan-Boulton1/jb-fit/main/jb_fit/urls.py) | ![screenshot](documentation/testing/validation/python/jb_fit/python-validation-urls.png) | |
|  | manage.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jordan-Boulton1/jb-fit/main/manage.py) | ![screenshot](documentation/testing/validation/python/python-validation-manage.png) | |
| plans | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jordan-Boulton1/jb-fit/main/plans/admin.py) | ![screenshot](documentation/testing/validation/python/plans/python-validation-plans-admin.png) | |
| plans | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jordan-Boulton1/jb-fit/main/plans/models.py) | ![screenshot](documentation/testing/validation/python/plans/python-validation-plans-models.png) | |
| plans | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jordan-Boulton1/jb-fit/main/plans/urls.py) | ![screenshot](documentation/testing/validation/python/plans/python-validation-plans-urls.png) | |
| plans | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jordan-Boulton1/jb-fit/main/plans/views.py) | ![screenshot](documentation/testing/validation/python/plans/python-validation-plans-views.png) | |
| plans | test_urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jordan-Boulton1/jb-fit/main/plans/tests/test_urls.py) | ![screenshot](documentation/testing/validation/python/plans/python-validation-plans-test-urls.png) | |
| plans | test_views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jordan-Boulton1/jb-fit/main/plans/tests/test_views.py) | ![screenshot](documentation/testing/validation/python/plans/python-validation-plans-test-views.png) | |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | About | Plans | FAQ | Profile | Edit Profile | Logout | Login | Register | Checkout | Checkout Success | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/testing/browser-compatibility/chrome/chrome-home.png) | ![screenshot](documentation/testing/browser-compatibility/chrome/chrome-about.png) | ![screenshot](documentation/testing/browser-compatibility/chrome/chrome-plans.png) | ![screenshot](documentation/testing/browser-compatibility/chrome/chrome-faq.png) | ![screenshot](documentation/testing/browser-compatibility/chrome/chrome-profile.png) | ![screenshot](documentation/testing/browser-compatibility/chrome/chrome-edit-profile.png) | ![screenshot](documentation/testing/browser-compatibility/chrome/chrome-logout.png) | ![screenshot](documentation/testing/browser-compatibility/chrome/chrome-login.png) | ![screenshot](documentation/testing/browser-compatibility/chrome/chrome-register.png) | ![screenshot](documentation/testing/browser-compatibility/chrome/chrome-checkout.png) | ![screenshot](documentation/testing/browser-compatibility/chrome/chrome-checkout-successful.png) | Works as expected |
| Firefox | ![screenshot](documentation/testing/browser-compatibility/firefox/firefox-home.png) | ![screenshot](documentation/testing/browser-compatibility/firefox/firefox-about.png) | ![screenshot](documentation/testing/browser-compatibility/firefox/firefox-plans.png) | ![screenshot](documentation/testing/browser-compatibility/firefox/firefox-faq.png) | ![screenshot](documentation/testing/browser-compatibility/firefox/firefox-profile.png) | ![screenshot](documentation/testing/browser-compatibility/firefox/firefox-edit-profile.png) | ![screenshot](documentation/testing/browser-compatibility/firefox/firefox-logout.png) | ![screenshot](documentation/testing/browser-compatibility/firefox/firefox-login.png) | ![screenshot](documentation/testing/browser-compatibility/firefox/firefox-signup.png) | ![screenshot](documentation/testing/browser-compatibility/firefox/firefox-checkout.png) | ![screenshot](documentation/testing/browser-compatibility/firefox/firefox-checkout-successful.png) | Works as expected |
| Edge | ![screenshot](documentation/testing/browser-compatibility/edge/edge-home.png) | ![screenshot](documentation/testing/browser-compatibility/edge/edge-about.png) | ![screenshot](documentation/testing/browser-compatibility/edge/edge-plans.png) | ![screenshot](documentation/testing/browser-compatibility/edge/edge-faq.png) | ![screenshot](documentation/testing/browser-compatibility/edge/edge-profile.png) | ![screenshot](documentation/testing/browser-compatibility/edge/edge-edit-profile.png) | ![screenshot](documentation/testing/browser-compatibility/edge/edge-logout.png) | ![screenshot](documentation/testing/browser-compatibility/edge/edge-login.png) | ![screenshot](documentation/testing/browser-compatibility/edge/edge-signup.png) | ![screenshot](documentation/testing/browser-compatibility/edge/edge-checkout.png) | ![screenshot](documentation/testing/browser-compatibility/edge/edge-checkout-successful.png) | Works as expected |
<<<<<<< Updated upstream
| Safari | ![screenshot](documentation/testing/browser-compatibility/safari/safari-home.png) | ![screenshot](documentation/testing/browser-compatibility/safari/safari-about.png) | ![screenshot](documentation/testing/browser-compatibility/safari/safari-plans.png) | ![screenshot](documentation/testing/browser-compatibility/safari/safari-faq.png) | ![screenshot](documentation/testing/browser-compatibility/safari/safari-profile.png) | ![screenshot](documentation/testing/browser-compatibility/safari/safari-edit-profile.png) | ![screenshot](documentation/testing/browser-compatibility/safari/safari-logout.png) | ![screenshot](documentation/testing/browser-compatibility/safari/safari-login.png) | ![screenshot](documentation/testing/browser-compatibility/safari/safari-signup.png) | ![screenshot](documentation/testing/browser-compatibility/safari/safari-checkout.png) | ![screenshot](documentation/testing/browser-compatibility/safari/safari-checkout-successful.png) | Minor CSS differences |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Home | About | Plans | FAQ | Profile | Edit Profile | Logout | Login | Register | Checkout | Checkout Success | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/testing/responsiveness/mobile/mobile-home.png) | ![screenshot](documentation/testing/responsiveness/mobile/mobile-about.png) | ![screenshot](documentation/testing/responsiveness/mobile/mobile-plans.png) | ![screenshot](documentation/testing/responsiveness/mobile/mobile-faq.png) | ![screenshot](documentation/testing/responsiveness/mobile/mobile-profile.png) | ![screenshot](documentation/testing/responsiveness/mobile/mobile-edit-profile.png) | ![screenshot](documentation/testing/responsiveness/mobile/mobile-logout.png) | ![screenshot](documentation/testing/responsiveness/mobile/mobile-login.png) | ![screenshot](documentation/testing/responsiveness/mobile/mobile-signup.png) | ![screenshot](documentation/testing/responsiveness/mobile/mobile-checkout.png) | ![screenshot](documentation/testing/responsiveness/mobile/mobile-checkout-successful.png) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/testing/responsiveness/tablet/tablet-home.png) | ![screenshot](documentation/testing/responsiveness/tablet/tablet-about.png) | ![screenshot](documentation/testing/responsiveness/tablet/tablet-plans.png) | ![screenshot](documentation/testing/responsiveness/tablet/tablet-faq.png) | ![screenshot](documentation/testing/responsiveness/tablet/tablet-profile.png) | ![screenshot](documentation/testing/responsiveness/tablet/tablet-edit-profile.png) | ![screenshot](documentation/testing/responsiveness/tablet/tablet-logout.png) | ![screenshot](documentation/testing/responsiveness/tablet/tablet-login.png) | ![screenshot](documentation/testing/responsiveness/tablet/tablet-signup.png) | ![screenshot](documentation/testing/responsiveness/tablet/tablet-checkout.png) | ![screenshot](documentation/testing/responsiveness/tablet/tablet-checkout-successful.png) | Works as expected |
| Desktop | ![screenshot](documentation/testing/responsiveness/desktop/desktop-home.png) | ![screenshot](documentation/testing/responsiveness/desktop/desktop-about.png) | ![screenshot](documentation/testing/responsiveness/desktop/desktop-plans.png) | ![screenshot](documentation/testing/responsiveness/desktop/desktop-faq.png) | ![screenshot](documentation/testing/responsiveness/desktop/desktop-profile.png) | ![screenshot](documentation/testing/responsiveness/desktop/desktop-edit-profile.png) | ![screenshot](documentation/testing/responsiveness/desktop/desktop-logout.png) | ![screenshot](documentation/testing/responsiveness/desktop/desktop-login.png) | ![screenshot](documentation/testing/responsiveness/desktop/desktop-signup.png) | ![screenshot](documentation/testing/responsiveness/desktop/desktop-checkout.png) | ![screenshot](documentation/testing/responsiveness/desktop/desktop-checkout-successful.png) | Works as expected |
| iPhone 11 | ![screenshot](documentation/testing/responsiveness/iphone/iphone-home.png) | ![screenshot](documentation/testing/responsiveness/iphone/iphone-about.png) | ![screenshot](documentation/testing/responsiveness/iphone/iphone-plans.png) | ![screenshot](documentation/testing/responsiveness/iphone/iphone-faq.png) | ![screenshot](documentation/testing/responsiveness/iphone/iphone-profile.png) | ![screenshot](documentation/testing/responsiveness/iphone/iphone-edit-profile.png) | ![screenshot](documentation/testing/responsiveness/iphone/iphone-logout.png) | ![screenshot](documentation/testing/responsiveness/iphone/iphone-login.png) | ![screenshot](documentation/testing/responsiveness/iphone/iphone-signup.png) | ![screenshot](documentation/testing/responsiveness/iphone/iphone-checkout.png) | ![screenshot](documentation/testing/responsiveness/iphone/iphone-checkout-successful.png) | Works as expected |
| Safari | ![screenshot](documentation/testing/browser-compatibility/safari/safari-home.png) | ![screenshot](documentation/testing/browser-compatibility/safari/safari-about.png) | ![screenshot](documentation/testing/browser-compatibility/safari/safari-plans.png) | ![screenshot](documentation/testing/browser-compatibility/safari/safari-faq.png) | ![screenshot](documentation/testing/browser-compatibility/safari/safari-profile.png) | ![screenshot](documentation/testing/browser-compatibility/safari/safari-edit-profile.png) | ![screenshot](documentation/testing/browser-compatibility/safari/safari-logout.png) | ![screenshot](documentation/testing/browser-compatibility/safari/safari-login.png) | ![screenshot](documentation/testing/browser-compatibility/safari/safari-signup.png) | ![screenshot](documentation/testing/browser-compatibility/safari/safari-checkout.png) | ![screenshot](documentation/testing/browser-compatibility/safari/safari-checkout-successful.png) | Minor Text Issues |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/testing/lighthouse/mobile/home.png) | ![screenshot](documentation/testing/lighthouse/desktop/home.png) | Slow response time due to large images and some minor warnings |
| About | ![screenshot](documentation/testing/lighthouse/mobile/about.png) | ![screenshot](documentation/testing/lighthouse/desktop/about.png) | slow response time due to large images and some minor warnings |
| Plans | ![screenshot](documentation/testing/lighthouse/mobile/plans.png) | ![screenshot](documentation/testing/lighthouse/desktop/plans.png) | Some minor warnings |
| FAQ | ![screenshot](documentation/testing/lighthouse/mobile/faq.png) | ![screenshot](documentation/testing/lighthouse/desktop/faq.png) | Some minor warnings |
| Profile | ![screenshot](documentation/testing/lighthouse/mobile/profile.png) | ![screenshot](documentation/testing/lighthouse/desktop/profile.png) | Some minor warnings |
| Edit Profile | ![screenshot](documentation/testing/lighthouse/mobile/edit-profile.png) | ![screenshot](documentation/testing/lighthouse/desktop/edit-profile.png) | Some minor warnings |
| Logout | ![screenshot](documentation/testing/lighthouse/mobile/logout.png) | ![screenshot](documentation/testing/lighthouse/desktop/logout.png) | Some minor warnings |
| Login | ![screenshot](documentation/testing/lighthouse/mobile/login.png) | ![screenshot](documentation/testing/lighthouse/desktop/login.png) | Some minor warnings |
| Register | ![screenshot](documentation/testing/lighthouse/mobile/signup.png) | ![screenshot](documentation/testing/lighthouse/desktop/signup.png) | Some minor warnings |
| Checkout | ![screenshot](documentation/testing/lighthouse/mobile/checkout.png) | ![screenshot](documentation/testing/lighthouse/desktop/checkout.png) | Some minor warnings |
| Checkout Success | ![screenshot](documentation/testing/lighthouse/mobile/checkout-successful.png) | ![screenshot](documentation/testing/lighthouse/desktop/checkout-successful.png) | Some minor warnings |

## Automated Testing

I have conducted a series of automated tests on my application.

I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

### Python (Unit Testing)
I have used Django's built-in unit testing framework to test the application functionality.

In order to run the tests, I ran the following command in the terminal each time:

`python manage.py test`

To create the coverage report, I would then run the following commands:

`coverage run manage.py test`

`coverage report`

To see the HTML version of the reports, and find out whether some pieces of code were missing, I ran the following commands:

`coverage html`

`python -m http.server`

Below are the results from the various apps on my application that I've tested:
| App | File | Coverage | Screenshot                                                                                   | 
| --- | --- | --- |----------------------------------------------------------------------------------------------| 
  | about | test_urls.py | 100% | ![screenshot](documentation/testing/automated-testing/python/py-test-about-urls.png) | 
  | about  | test_views.py | 100% | ![screenshot](documentation/testing/automated-testing/python/py-test-about-views.png)  |
| accounts | test_models.py | 100% | ![screenshot](documentation/testing/automated-testing/python/py-test-accounts-models.png) | 
  | accounts  | test_forms.py | 98% | ![screenshot](documentation/testing/automated-testing/python/py-test-accounts-forms.png)  |
| accounts | test_views.py | 71% | ![screenshot](documentation/testing/automated-testing/python/py-test-accounts-views.png)  |
| accounts | test_urls.py | 100% | ![screenshot](documentation/testing/automated-testing/python/py-test-accounts-urls.png)  |
| checkout| test_models.py | 100% | ![screenshot](documentation/testing/automated-testing/python/py-test-checkout-models.png)  |
| checkout| test_forms.py | 100% | ![screenshot](documentation/testing/automated-testing/python/py-test-checkout-forms.png)  |
| checkout| test_views.py | 90% | ![screenshot](documentation/testing/automated-testing/python/py-test-checkout-views.png)  |
| checkout| test_urls.py | 100% | ![screenshot](documentation/testing/automated-testing/python/py-test-checkout-urls.png)  |
| contact| test_models.py | 100% | ![screenshot](documentation/testing/automated-testing/python/py-test-contact-models.png)  |
| contact| test_forms.py | 100% | ![screenshot](documentation/testing/automated-testing/python/py-test-contact-forms.png)  |
| contact| test_views.py | 100% | ![screenshot](documentation/testing/automated-testing/python/py-test-contact-views.png)  |
| contact| test_urls.py | 100% | ![screenshot](documentation/testing/automated-testing/python/py-test-contact-urls.png)  |
| faq| test_views.py | 100% | ![screenshot](documentation/testing/automated-testing/python/py-test-faq-views.png)  |
| faq| test_urls.py | 100% | ![screenshot](documentation/testing/automated-testing/python/py-test-faq-urls.png)  |
| home| test_models.py | 100% | ![screenshot](documentation/testing/automated-testing/python/py-test-home-models.png)  |
| home| test_forms.py | 100% | ![screenshot](documentation/testing/automated-testing/python/py-test-home-forms.png)  |
| home| test_views.py | 100% | ![screenshot](documentation/testing/automated-testing/python/py-test-home-views.png)  |
| home| test_urls.py | 100% | ![screenshot](documentation/testing/automated-testing/python/py-test-home-urls.png)  |
| plans| test_models.py | 88% | ![screenshot](documentation/testing/automated-testing/python/py-test-plans-models.png)  |
| plans| test_views.py | 44% | ![screenshot](documentation/testing/automated-testing/python/py-test-plans-views.png)  |
| plans| test_urls.py | 100% | ![screenshot](documentation/testing/automated-testing/python/py-test-plans-urls.png)  |
