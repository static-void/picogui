# how to create the rpm

rpm: dist
	sudo rpm -tb picogui-apps-0.5.tar.gz
