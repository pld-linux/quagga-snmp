Summary:	Net-SNMP extension for monitoring Quagga bgpd
Name:		quagga-snmp
Version:	0.3
Release:	0.1
License:	GPLv2
Group:		Applications
Source0:	http://www.net-track.ch/opensource/quagga-snmp/%{name}-%{version}.tar.gz
# Source0-md5:	a5c06a2ef8d164a0a4f04c1e3c7a2516
URL:		http://www.net-track.ch/opensource/quagga-snmp/
BuildRequires:	rpmbuild(macros) >= 1.228       
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
quagga-snmp-bgpd is an extension for the Net-SNMP agent. It probes a
running Quagga bgpd instance and makes show ip bgp summary statistics
available through SNMP. Unlike the standard RFC 1657 BGP4 MIB, this
includes the number of prefixes received from every peer. This makes
it possible to see disappearing peers using a tool such as MRTG.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
