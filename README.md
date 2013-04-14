pyMITMProxyParser
=================

python code that parse MITMProxy flow data


**status**

* It works now

**usage**

* you can see [https://github.com/bandoche/pyThriftParser](https://github.com/bandoche/pyThriftParser)

		from MITMProxyReader import MITMProxyReader
		mpr = MITMProxyReader()
		clean_dict = mpr.read_file(filename)
		for clean_dict_item in clean_dict:
			print clean_dict_item['request']['host'] , clean_dict_item['request']['path']
		
		