/* jshint esversion: 11, jquery: true */
/* global beforeEach, describe, expect, jest, test */

import '@testing-library/jest-dom';
import { fireEvent } from '@testing-library/dom';
import {setupCloseButtons, loadTooltips} from '../base';

beforeEach(() => {
    // Set up the HTML structure required for the script
    document.body.innerHTML = `
        <div class="alert" style="display: block;">
            <button class="closebtn-variant">Close Variant</button>
        </div>
        <div class="alert" style="display: block;">
            <button class="closebtn">Close</button>
        </div>
        <div class="alert" style="display: block;">
            <button class="closeerrorbtn">Close Error</button>
        </div>
        <div data-bs-toggle="tooltip" title="Tooltip text"></div>
    `;

    jest.clearAllMocks(); // Clear mocks before each test
});


describe('Page functionality', () => {
    test('Sets up click event listeners on close buttons', () => {
        require('../base.js'); // Load the script

         // Query the close buttons
        const closeBtnVariant = document.querySelector('.closebtn-variant');
        const closeBtn = document.querySelector('.closebtn');
        const closeErrorBtn = document.querySelector('.closeerrorbtn');

        // Add spies to check if event listeners are attached
        setupCloseButtons('.closebtn-variant');
        setupCloseButtons('.closebtn');
        setupCloseButtons('.closeerrorbtn');

        fireEvent.click(closeBtnVariant);
        fireEvent.click(closeBtn);
        fireEvent.click(closeErrorBtn);

        // Check if the parent alerts are hidden
        expect(closeBtnVariant.closest('.alert')).toHaveStyle('display: none');
        expect(closeBtn.closest('.alert')).toHaveStyle('display: none');
        expect(closeErrorBtn.closest('.alert')).toHaveStyle('display: none');
    });

    test('Initializes Bootstrap tooltips', () => {
       loadTooltips();

        // Check if Bootstrap Tooltip was called correctly
        expect(global.bootstrap.Tooltip).toHaveBeenCalledTimes(1);

        // Check if the tooltip was initialized on the correct element
        const tooltipElement = document.querySelector('[data-bs-toggle="tooltip"]');
        expect(global.bootstrap.Tooltip).toHaveBeenCalledWith(tooltipElement);
    });
});