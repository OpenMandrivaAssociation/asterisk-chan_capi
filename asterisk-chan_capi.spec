%define rname	chan_capi

Summary:	Asterisk ISDN CAPI channel driver
Name:		asterisk-%{rname}
Version:	1.1.5
Release:	%mkrel 2
License:	GPLv2
Group:		System/Servers
URL:		http://www.melware.org/ChanCapi
Source0:	ftp://ftp.chan-capi.org/chan-capi/%{rname}-%{version}.tar.gz
BuildRequires:	isdn4k-utils-devel
BuildRequires:	asterisk-devel
Requires:	asterisk
Provides:	asterisk-chan_capi-cm = %{version}-%{release}
Obsoletes:	asterisk-chan_capi-cm
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
ISDN CAPI Channel driver (chan_capi) for the Asterisk Open Source VOIP
Platform. Reworked, but based on the work of Copyright (C) 2002-2005
Junghanns.NET GmbH Klaus-Peter Junghanns.

%prep

%setup -q -n %{rname}-%{version}

# clean up CVS stuff
for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -r $i; fi >&/dev/null
done

# fix file perms
chmod 644 CHANGES INSTALL README

%build

#make CFLAGS="%{optflags} -pipe -Wall -fPIC -DPIC -D_REENTRANT -D_GNU_SOURCE -DASTERISKVERSION=\\\"1.6\\\" -I. -I%{_includedir}" USE_OWN_LIBCAPI=no
%make

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_sysconfdir}/asterisk/modules
install -d %{buildroot}%{_libdir}/asterisk/modules

install -m0644 capi.conf %{buildroot}%{_sysconfdir}/asterisk/
install -m0755 chan_capi.so %{buildroot}%{_libdir}/asterisk/modules/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES INSTALL README
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/asterisk/capi.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/chan_capi.so

