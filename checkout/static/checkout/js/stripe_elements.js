/* jshint esversion: 11, jquery: true */
/* global Stripe */

// Check if the browser supports the replaceState method
if (window.history.replaceState) {
    // Replace the current history state with a new one to prevent form resubmission
    window.history.replaceState(null, null, window.location.href);
}

// Wait for the DOM to fully load before running the script
document.addEventListener('DOMContentLoaded', function () {
    // Get the Stripe public key and client secret from the HTML elements
    var stripePublicKey = document.getElementById('id_stripe_public_key').textContent.slice(1, -1);
    var clientSecret = document.getElementById('id_client_secret').textContent.slice(1, -1);

    // Initialize Stripe with the public key
    var stripe = Stripe(stripePublicKey);

    // Create an instance of Stripe elements
    var elements = stripe.elements();

    // Create a card element with custom styling
    var card = elements.create('card', {
        iconStyle: 'solid',  // Use a solid icon style
        style: {
            base: {
                iconColor: '#ff5100',  // Set icon color
                color: '#fff',  // Set text color
                fontWeight: 500,  // Set font weight
                fontFamily: 'Roboto, Open Sans, Segoe UI, sans-serif',  // Set font family
                fontSize: '16px',  // Set font size
                fontSmoothing: 'antialiased',  // Smoothing for better font rendering

                // Styling for autofill text
                ':-webkit-autofill': {
                    color: '#fce883',  // Set color for autofilled text
                },
                // Styling for placeholder text
                '::placeholder': {
                    color: '#ffff',  // Set placeholder color
                },
            },
        },
    });

    // Mount the card element into the DOM element with the ID 'card-element'
    card.mount('#card-element');

    // Get the payment form element
    var form = document.getElementById('payment-form');

    // Handle real-time validation errors on the card element
    card.addEventListener('change', function (event) {
        // Get the error div element to display errors
        var errorDiv = document.getElementById('card-errors');
        if (event.error) {
            // If there's an error, display it in the error div
            var html = `
                <div class="alert-danger>
                    <span class="icon" role="alert">
                        <i class="fas fa-times"></i>
                    </span>
                    <span>${event.error.message}</span>
                </div>
            `;
            errorDiv.innerHTML = html;  // Update the error div with the error message
        } else {
            errorDiv.textContent = '';  // Clear the error message if no errors
        }
    });

    // Handle form submission
    form.addEventListener('submit', function (ev) {
        ev.preventDefault();  // Prevent the default form submission

        // Get trimmed values from the form inputs
        var email = $.trim(form.querySelector('[name="email"]').value);
        var first_name = $.trim(form.querySelector('[name="first_name"]').value);
        var last_name = $.trim(form.querySelector('[name="last_name"]').value);

        // Confirm the card payment using Stripe's confirmCardPayment method
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,  // The card element created earlier
                billing_details: {
                    name: `${first_name} ${last_name}`,  // Concatenate first and last name for billing
                    email: email  // Email address for billing
                },
            }
        }).then(function(result) {
            if (result.error) {
                // If there's an error during payment confirmation, display it
                var errorDiv = document.getElementById('card-errors');
                var html = `
                    <span class="icon" role="alert">
                        <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>
                `;
                errorDiv.innerHTML = html;  // Update the error div with the error message
            } else {
                // The payment has been processed successfully
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();  // Submit the form to complete the process if payment succeeded
                }
            }
        }).catch(function(error) {
            // Log any errors during payment processing
            console.error('Error during payment processing:', error);
        });
    });
});
