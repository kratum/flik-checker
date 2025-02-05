# FLIK Checker

A simple web application to check if a FLIK (Feldblock-Identifikator) is "innerhalb der mit Nitrat belasteten Gebiete nach § 13a DüV (01/2025)". For this task the following WFS-Service of LANUV is used: 

url='https://www.wfs.nrw.de/umwelt/elwas-duengeverordnung_wfs'
typename='elwas_duengeverordnung_wfs:nitratbelastete_gebiete_feldbloecke'


## Usage

1. Visit the GitHub Pages site at: https://kratum.github.io/flik-checker
2. Enter a FLIK number in the input field
3. Click "Check FLIK" to see the result

## Development

This application is a single HTML file that runs entirely in the browser. It uses:
- Vanilla JavaScript for functionality
- Built-in fetch API for making requests
