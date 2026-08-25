// JavaScript Calculator - Core logic
// This module contains the pure calculation functions used by the
// HTML calculator (index.html). It is kept separate so the logic
// can be reused and tested independently of the UI.

const Calculator = {
    add(a, b) {
        return a + b;
    },

    subtract(a, b) {
        return a - b;
    },

    multiply(a, b) {
        return a * b;
    },

    divide(a, b) {
        if (b === 0) {
            throw new Error("Cannot divide by zero.");
        }
        return a / b;
    },

    /**
     * Evaluate a simple arithmetic expression string.
     * Supports +, -, *, / and parentheses.
     * @param {string} expression
     * @returns {number}
     */
    evaluate(expression) {
        if (!expression || typeof expression !== "string") {
            throw new Error("Empty expression.");
        }

        // Only allow digits, operators, decimals, parentheses and spaces
        const safe = expression.replace(/\s+/g, "");
        if (!/^[0-9+\-*/.()]+$/.test(safe)) {
            throw new Error("Invalid characters in expression.");
        }

        const result = Function('"use strict"; return (' + safe + ")")();

        if (typeof result !== "number" || isNaN(result)) {
            throw new Error("Invalid expression.");
        }

        // Round to avoid floating point noise
        return Math.round(result * 1e10) / 1e10;
    }
};

// Export for use in Node.js / testing if running outside the browser
if (typeof module !== "undefined" && module.exports) {
    module.exports = Calculator;
}
