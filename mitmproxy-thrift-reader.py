#!/usr/bin/env python
import io
import sys

def convert_mitmproxy_flow_to_object(raw_data):
	start = 0
	clean_list = []
	modified = False

	while True:
		# print raw_data
		idx = raw_data.find(':', start+1)
		# print
		# print 'idx = ', idx
		if (idx > 0):
			length = raw_data[start:idx]
			if length == '':
				# print 'wrong length - start, idx = ', start, ',' , idx #,raw_data
				break
			try:
				length = int(length)
				pass
			except Exception, e:
				# it is clean data
				return (raw_data, False) 
				raise e
			# print "length - (", length , ')'
			if length > 0:
				clean_data = raw_data[idx + 1:length + idx + 1]
				# print clean_data
				test_list, test_modified = convert_mitmproxy_flow_to_object(clean_data)
				if test_modified:
					# print "test return modified"
					clean_list.append(test_list)
				else: 
					# print "test return not modified"
					clean_list.append(clean_data)
					# print clean_data
				start = length + idx + 2
			elif length == 0:
				# print "0 length"
				clean_list.append('')
				start = start + 3
			else:
				print "weird!"
				modified = False
				break
			if (start >= len(raw_data)):
				# print "debug: start(", start, ") overflow data length(", len(raw_data), ")"
				break
			modified = True

		else:
			# print "debug: just clean!"
			modified = False
			break

	return (clean_list, modified)

def convert_cleanlist_to_dict(clean_list):
	key_flag = True
	key_name = ''

	clean_dict = {}
	for item in clean_list:
		if key_flag:
			if isinstance(item, str):
				key_name = item
				# print "key_name - ", key_name
			else:
				return convert_cleanlist_to_dict(item)
		else:
			if isinstance(item, str):
				clean_dict[key_name] = item
				# print "val(str) - ", item
			else:
				converted = convert_cleanlist_to_dict(item)
				clean_dict[key_name] = converted
				# print "val(dict) - ", converted
		key_flag = not key_flag
	return clean_dict


if len(sys.argv) == 1:
	print 'no filename'
else:
	filename = sys.argv[1]
	f = io.open(filename, 'rb')
	data = f.read()
	clean_list, modified = convert_mitmproxy_flow_to_object(data)
	# print clean_list
	clean_dict = convert_cleanlist_to_dict(clean_list[0])
	# print
	# print clean_dict
	print clean_dict['request']['content']


