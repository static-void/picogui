# handle PicoGUI responses

import struct

# errors (pgresponse_err)

class Error(Exception): pass
class ProtocolError(Error):
	def __init__(self, id, data_len):
		self.id = id
		self.additional_data_wanted = data_len

	def setData(self, data):
		# data is a C string
		self.args = data.replace('\0','')

class MemoryError(ProtocolError): pass
class IOError(ProtocolError): pass
class NetworkError(ProtocolError): pass
class ParameterError(ProtocolError): pass
class HandleError(ProtocolError): pass
class InternalError(ProtocolError): pass
class BusyError(ProtocolError): pass
class FileFormatError(ProtocolError): pass

class Dead(Error): pass

def NoError(id, data_len):
	return None

_error_types = {
	0x0000: NoError,
	0x0101: MemoryError,
	0x0200: IOError,
	0x0300: NetworkError,
	0x0400: ParameterError,
	0x0500: HandleError,
	0x0600: InternalError,	# shouldn't happen
	0x0700: BusyError,
	0x0800: FileFormatError,
	# 0x8000: ClientError,	# shouldn't happen - generated by us only
	}
	
def _error(args):
	id = args[2]
	errt = args[0]
	return id, _error_types[errt](id, args[1])

# returns (pgresponse_ret)

def _return(args):
	return args # d'oh

# events (pgresponse_event)

import events

def _event(args):
	return None, events.Event(*args)

# big data (pgresponse_data)

class Data(object):
	"""Encapsulates returned data, which will be in a string format but usually isn't
	really a string. To retrieve the data, call the instance passing a struct format.
	"""
	def __init__(self, id, data_len):
		self.id = id
		self.additional_data_wanted = data_len
		self.data = ''

	def setData(self, data):
		self.additional_data_wanted = 0
		self.data = data
	
	def __call__(self, format):
		return struct.unpack(format, self.data)

	def fstyle(self):
		"""pgdata_getfstyle
		"""
		return self('!40sHH')

	def modeinfo(self):
		"""pgmodeinfo
		"""
		return self('!LHHHHHxx')

	def __getslice__(self, left, right):
		return self.data[left:right]

def _data(args):
	return args[0], Data(*args)

_formats = (
	#handler,	format
	None,				# types start at one
	(_error,	'HHxxL'),	# errt, msglen, id
	(_return,	'xxLL'),	# id, data
	(_event,	'HLL'),		# event type, from, param
	(_data,		'xxLL'),	# id, size
)

def get(connection):
	"""Get (and return) the next response in connection
	"""
	if hasattr(connection, 'read'):
		read = connection.read
	elif hasattr(connection, 'recv'):
		read = connection.recv
	else:
		raise TypeError('Connection object supports neither read() nor recv()')
	def safe_read(l, read=read):
		try:
			r = read(l)
		except:
			import sys
			# fetch the exception object, so that we may know what went wrong
			corpse = 'Exception during read from pgserver', sys.exc_info()[1]
			raise Dead(*corpse)
		if len(r) == l:
			return r
		raise Dead, 'We seem to have lost our server - tried to read %s bytes and got %s (%r)' % (
			l, len(r), r)
	type_num, = struct.unpack('!H', safe_read(2))
	try:
		handler, format = _formats[type_num]
	except:
		raise Dead('Invalid return packet type', type_num)
	# this is in code to make sure it's enforced
	format = '!' + format
	resp_size = struct.calcsize(format)
	response = struct.unpack(format, safe_read(resp_size))
	id, obj = handler(response)
	if hasattr(obj, 'additional_data_wanted'):
		if obj.additional_data_wanted:
			obj.setData(safe_read(obj.additional_data_wanted))
		else:
			obj.setData('')
	try:
		connection.last_id = id
	except:
		pass
	return id, obj

def next(connection):
	# call get() and process when necessary
	resp = get(connection)[1]
	if isinstance(resp, Exception):
		raise resp
	else:
		return resp
