

	*Automated simultaneous generation of statistics for multiple record IDs running on an instance
	of an Access point, thus the automatic generation of multiple CSV, JSON and PDML files for numerous record IDs. 
    
	Analyzed statistics which contained PDUs, SDUs and other fields for the goal of improvising and predicting throughput for access points

	*Input should be in the text file format of the captured file from Wireshark (Can be downloaded as .txt from Wireshark).
            
	*This code was specifically written to parse RNTI (Radio Network Temporary Identifier.) and
	PDU( Protocol Data Unit ) from 'Femto application platform interface' (FAPI). 
	
    	(( The specifications were extended to nFAPI (network functional application platform interface) 
	following a virtualization study undertaken by Small Cell Forum, 
    	which examined different functional splits between virtual and physical network functions. ))

    	*filter.txt contains a filter for FAPI packets. 
	After implimentation of this filter, Wireshark would parse FAPI packets at Wireshark level.
	It should then be converted to a text file to put in as input for parse.py

	For more details, check Explanation.pdf

