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
| Firefox | ![screenshot](documentation/testing/browser-compatibility/firefox/firefox-home.png) | ![screenshot](documentation/testing/browser-compatibility/firefox/firefox-about.png) | ![screenshot](documentation/testing/browser-compatibility/firefox/firefox-plans.png) | ![screenshot](documentation/testing/browser-compatibility/firefox/firefox-faq.png) | ![screenshot](documentation/testing/browser-compatibility/firefox/firefox-profile.png) | ![screenshot](documentation/testing/browser-compatibility/firefox/firefox-edit-profile.png) | ![screenshot](documentation/testing/browser-compatibility/firefox/firefox-logout.png) | ![screenshot](documentation/testing/browser-compatibility/firefox/firefox-login.png) | ![screenshot](documentation/testing/browser-compatibility/firefox/firefox-signup.png) | ![screenshot](documentation/testing/browser-compatibility/firefox/firefox-checkout.png) | ![screenshot](documentation/testing/browser-compatibility/firefox/firefox-checkout-successful.png) | Works as expected 