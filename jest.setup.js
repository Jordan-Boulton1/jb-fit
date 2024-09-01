// jest.setup.js
import '@testing-library/jest-dom';  // Provides custom DOM matchers
import 'whatwg-fetch';              // Provides fetch API for testing

// Mock for Bootstrap modal, as it's used directly in the code.
global.bootstrap = {
    Modal: jest.fn().mockImplementation(() => ({
        show: jest.fn(),
        hide: jest.fn(),
    })),
    Tooltip: jest.fn(),
};

// Mock the getCookie function if it needs to be used globally
global.getCookie = jest.fn(() => 'mockCsrfToken');

// Mock window.location.reload and window.history.replaceState
Object.defineProperty(window, 'location', {
    writable: true,
    value: {
        ...window.location,
        reload: jest.fn(),
    },
});

Object.defineProperty(window.history, 'replaceState', {
    writable: true,
    value: jest.fn(),
});

// Mock jQuery
global.$ = jest.fn().mockImplementation((selector) => {
    if (selector === '[name="email"]' || selector === '[name="first_name"]' || selector === '[name="last_name"]') {
        return { value: 'test' };
    }
    return {
        trim: () => '',
        on: jest.fn(),  // Mock jQuery event listener
        modal: jest.fn(),  // Mock Bootstrap's modal method
    };
});

// Mock fetch
global.fetch = jest.fn(); // Mock fetch for API calls