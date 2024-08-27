// Check if the browser supports the replaceState method
if (window.history.replaceState) {
    // Replace the current history state with a new one to prevent form resubmission
    window.history.replaceState(null, null, window.location.href);
}


document.addEventListener('DOMContentLoaded', function () {
    var stripePublicKey = document.getElementById('id_stripe_public_key').textContent.slice(1, -1);
    var clientSecret = document.getElementById('id_client_secret').textContent.slice(1, -1);
    var stripe = Stripe(stripePublicKey);
    var elements = stripe.elements();
    var card = elements.create('card', {
    iconStyle: 'solid',
    style: {
        base: {
            iconColor: '#ff5100',
            color: '#fff',
            fontWeight: 500,
            fontFamily: 'Roboto, Open Sans, Segoe UI, sans-serif',
            fontSize: '16px',
            fontSmoothing: 'antialiased',

            ':-webkit-autofill': {
                color: '#fce883',
            },
            '::placeholder': {
                color: '#ffff',
            },
        },
        
        },
    });

    card.mount('#card-element');
    var form = document.getElementById('payment-form');

    // Handle real-time validation errors on the card element
    card.addEventListener('change', function (event) {
        var errorDiv = document.getElementById('card-errors');
        if (event.error) {
            var html = `
                <div class="alert-danger>
                    <span class="icon" role="alert">
                        <i class="fas fa-times"></i>
                    </span>
                    <span>${event.error.message}</span>
                </div>
            `;
            errorDiv.innerHTML = html;
        } else {
            errorDiv.textContent = '';
        }
    });

    form.addEventListener('submit', function (ev) {
        ev.preventDefault();
        console.log('Form submission prevented. Processing payment...');

        var email = $.trim(form.querySelector('[name="email"]').value);
        var first_name = $.trim(form.querySelector('[name="first_name"]').value);
        var last_name = $.trim(form.querySelector('[name="last_name"]').value);

        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: first_name,
                    email: email
                },
            }
        }).then(function(result) {
            if (result.error) {
                // Show error to your customer (e.g., insufficient funds)
                console.error('Payment failed:', result.error.message);
                var errorDiv = document.getElementById('card-errors');
                var html = `
                    <span class="icon" role="alert">
                        <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>
                `;
                errorDiv.innerHTML = html;
            } else {
                // The payment has been processed!
                if (result.paymentIntent.status === 'succeeded') {
                    console.log('Payment successful! Submitting form...');
                    form.submit(); // Submit the form to complete the process
                }
            }
        }).catch(function(error) {
            console.error('Error during payment processing:', error);
        });
    });
});
