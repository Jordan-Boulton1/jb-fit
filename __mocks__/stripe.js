const stripeMock = {
    elements: jest.fn().mockReturnThis(),
    create: jest.fn().mockReturnThis(),
    mount: jest.fn(),
    confirmCardPayment: jest.fn().mockResolvedValue({
        paymentIntent: {
            status: 'succeeded',
        },
    }),
};

const Stripe = jest.fn(() => stripeMock);

export default Stripe;