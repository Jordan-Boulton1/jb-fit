/* jshint esversion: 11, jquery: true */
/* global beforeEach, describe, expect, jest, test */

import '@testing-library/jest-dom';  // Import Jest DOM utilities for testing
import { fireEvent } from '@testing-library/dom';  // Import fireEvent from testing-library for simulating events
import { setupCloseButtons, loadTooltips } from '../base';  // Import the functions to be tested

// Setup function that runs before each test case
beforeEach(() => {
    // Set up the HTML structure required for the script, including alert elements with close buttons and a tooltip
    document.body.innerHTML = `
        <div class="alert" style="display: block;">
            <button class="closebtn-variant">Close Variant</button>  <!-- Button to close variant alert -->
        </div>
        <div class="alert" style="display: block;">
            <button class="closebtn">Close</button>  <!-- Button to close normal alert -->
        </div>
        <div class="alert" style="display: block;">
            <button class="closeerrorbtn">Close Error</button>  <!-- Button to close error alert -->
        </div>
        <div data-bs-toggle="tooltip" title="Tooltip text"></div>  <!-- Element with tooltip -->
    `;

    // Clear all mocks before each test to reset the state
    jest.clearAllMocks();
});

// Describe block for grouping tests related to page functionality
describe('Page functionality', () => {

    // Test case for setting up click event listeners on close buttons
    test('Sets up click event listeners on close buttons', () => {
        require('../base.js');  // Load the script to initialize functions

        // Query the close buttons from the DOM
        const closeBtnVariant = document.querySelector('.closebtn-variant');
        const closeBtn = document.querySelector('.closebtn');
        const closeErrorBtn = document.querySelector('.closeerrorbtn');

        // Call setupCloseButtons for each type of close button
        setupCloseButtons('.closebtn-variant');
        setupCloseButtons('.closebtn');
        setupCloseButtons('.closeerrorbtn');

        // Simulate click events on each close button
        fireEvent.click(closeBtnVariant);
        fireEvent.click(closeBtn);
        fireEvent.click(closeErrorBtn);

        // Check if the parent alert elements are hidden after clicking the buttons
        expect(closeBtnVariant.closest('.alert')).toHaveStyle('display: none');  // Verify that the alert is hidden
        expect(closeBtn.closest('.alert')).toHaveStyle('display: none');  // Verify that the alert is hidden
        expect(closeErrorBtn.closest('.alert')).toHaveStyle('display: none');  // Verify that the alert is hidden
    });

    // Test case for initializing Bootstrap tooltips
    test('Initializes Bootstrap tooltips', () => {
        loadTooltips();  // Call the function to initialize tooltips

        // Check if Bootstrap Tooltip was called correctly
        expect(global.bootstrap.Tooltip).toHaveBeenCalledTimes(1);  // Verify that the Tooltip constructor was called once

        // Check if the tooltip was initialized on the correct element
        const tooltipElement = document.querySelector('[data-bs-toggle="tooltip"]');  // Select the element with the tooltip
        expect(global.bootstrap.Tooltip).toHaveBeenCalledWith(tooltipElement);  // Verify that the tooltip was initialized on the correct element
    });
});
