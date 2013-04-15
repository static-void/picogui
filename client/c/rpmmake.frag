# how to create the rpm

rpm: dist
	sudo rpm -tb picogui-client-0.0.tar.gz
