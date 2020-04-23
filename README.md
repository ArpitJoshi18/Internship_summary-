# Internship_summary-
Automated simultaneous generation of statistics for multiple record Id’s running on an instance of an Access point, thus the automatic generation of multiple CSV, JSON and PDML files for numerous record Id’s. Analyzed statistics which contained PDU’s, SDU’s and other fields for the goal of improvising and predicting throughput for access points



**Input should be in the text file format of captured file from Wireshark (Can be downloaded as .txt from wireshark)
**This code was specifically written to parse RNTI (Radio Network Temporary Identifier.), PDU( Protocol Data Unit ) from 'Femto application platform interface' (FAPI).
(( The specifications were extended to nFAPI (network functional application platform interface) following a virtualization study undertaken by Small Cell Forum, which examined different functional splits between virtual and physical network functions. ))

**filter.txt contains filter for FAPI packets. This would parse FAPI packets at wireshark level. It should then be converted to text file to put in as input for parse.py

for more details, check Explanation.pdf
