Name: hunspell-sk
Summary: Slovak hunspell dictionaries
Epoch: 1
%define upstreamid 20110228
Version: 0.%{upstreamid}
Release: 5%{?dist}
Source: http://www.sk-spell.sk.cx/files/hunspell-sk-%{upstreamid}.zip
Group: Applications/Text
URL: http://www.sk-spell.sk.cx/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LGPLv2 or GPLv2 or MPLv1.1
BuildArch: noarch

Requires: hunspell

%description
Slovak hunspell dictionaries.

%prep
%setup -q -n %{name}-%{upstreamid}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc doc/*
%{_datadir}/myspell/*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1:0.20110228-5
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.20110228-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.20110228-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.20110228-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Mar 18 2011 Caolán McNamara <caolanm@redhat.com> - 1:0.20110228-1
- latest version

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.20091213-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 14 2009 Caolán McNamara <caolanm@redhat.com> - 1:0.20091213-1
- latest version

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.20090330-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 01 2009 Caolán McNamara <caolanm@redhat.com> - 1:0.20090330-1
- latest version

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.20090106-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 11 2009 Caolán McNamara <caolanm@redhat.com> - 1:0.20090106-1
- latest version

* Thu Dec 03 2008 Caolán McNamara <caolanm@redhat.com> - 1:0.20080525-1
- latest version

* Fri Aug 03 2007 Caolán McNamara <caolanm@redhat.com> - 1:0.5.6-2
- clarify that tri-licensed

* Wed Jul 11 2007 Caolán McNamara <caolanm@redhat.com> - 1:0.5.6-1
- canonical upstream version

* Wed Feb 14 2007 Caolán McNamara <caolanm@redhat.com> - 0.20050911-1
- upstream id

* Thu Dec 07 2006 Caolán McNamara <caolanm@redhat.com> - 0.20050228-1
- initial version
