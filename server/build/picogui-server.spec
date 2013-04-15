%define prefix @RPM_PREFIX@
%define module %{prefix}/../bee

Summary: PicoGUI server
Name: picogui-server
Version: 0.45
Release: sd.8
Copyright: GPL
Group: PicoGUI/Server
Packager: Olivier Bornet <Olivier.Bornet@smartdata.ch>
Source: picogui-server-0.45.tar.gz
Vendor: SMARTDATA

Buildroot: %{_tmppath}/picogui-server

%description
The PicoGUI server application, which provides the display engine for PicoGUI clients.

%package @RPM_PLATFORM@
Summary: executable and headers
Group: PicoGUI/Server
Requires: picogui-server-mdl = 0.45

%package mdl
Summary: bee module
Group: PicoGUI/Server
Requires: bee >= 1.0.4

%description @RPM_PLATFORM@
The PicoGUI server application, which provides the display engine for PicoGUI clients.

%description mdl
The PicoGUI server application, which provides the display engine for PicoGUI clients.


%prep
%setup -n picogui-server-0.45

%build
mkdir build && cd build
.@RPM_CONFIGURE@
make

%install
cd build
make install prefix=$RPM_BUILD_ROOT%{prefix}

install -D -m 0644 ../PicoGUIServer.mdl $RPM_BUILD_ROOT%{module}/PicoGUIServer.mdl

%files @RPM_PLATFORM@
%{prefix}/bin/*
%{prefix}/etc/*

%files mdl
%{module}/*

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf ${RPM_BUILD_ROOT}

