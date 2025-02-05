# FLIK Checker

A simple web application to check FLIK (Feldblock-Identifikator) availability using the WFS service from NRW.

## Usage

1. Visit the GitHub Pages site at: https://kratum.github.io/flik-checker
2. Enter a FLIK number in the input field
3. Click "Check FLIK" to see the result

## Development

This application is a single HTML file that runs entirely in the browser. It uses:
- Vanilla JavaScript for functionality
- Built-in fetch API for making requests
- CORS proxy to handle cross-origin requests

## Note

The application uses a CORS proxy to handle cross-origin requests. For production use, you may want to set up your own proxy server or obtain proper CORS permissions from the WFS service provider.
