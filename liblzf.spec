%define rname lzf

%define common_description LZF is an extremely fast (not that much slower than a pure memcpy) \
compression algorithm. It is ideal for applications where you want to \
save *some* space but not at the cost of speed. It is ideal for \
repetitive data as well. The module is self-contained and very small.

Summary:	Very small data compression library
Name:		lib%{rname}
Version:	3.6
Release:	%mkrel 1
License:	BSD
Group:		System/Libraries
URL:		http://liblzf.plan9.de/
Source0:	http://dist.schmorp.de/liblzf/%{name}-%{version}.tar.gz
Patch0:		liblzf-3.1-makefile.patch
Patch1:		liblzf-3.4-LDFLAGS.diff
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
%{common_description}

%package -n %{rname}
Summary:	Tools for the %{rname} compression library
Group:		Archiving/Compression

%description -n	%{rname}
%{common_description}

This package contains tools for the %{rname} library.

%package -n %{name}-devel
Summary:	Development tools for the %{rname} compression library
Group:		Development/C
Provides:	%{rname}-devel

%description -n	%{name}-devel
%{common_description}

This package contains the header files and libraries needed for
developing programs using the %{rname} library.

%prep
%setup -q
%patch0 -p1
%patch1 -p0 -b .LDFLAGS

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files -n %{rname}
%defattr(-,root,root)
%doc README
%{_bindir}/%{rname}

%files -n %{name}-devel
%defattr(-,root,root)
%{_includedir}/%{rname}.h
%{_libdir}/%{name}.a


%changelog
* Tue Oct 11 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 3.6-1mdv2012.0
+ Revision: 704261
- update to new version 3.6

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 3.4-5
+ Revision: 661494
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 3.4-4mdv2011.0
+ Revision: 602572
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 3.4-3mdv2010.1
+ Revision: 520882
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 3.4-2mdv2010.0
+ Revision: 425594
- rebuild

* Sun Dec 21 2008 Oden Eriksson <oeriksson@mandriva.com> 3.4-1mdv2009.1
+ Revision: 317018
- 3.4
- use %%ldflags

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 3.1-2mdv2009.0
+ Revision: 222924
- rebuild
- fix no-buildroot-tag

* Mon Dec 31 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 3.1-1mdv2008.1
+ Revision: 139735
- new version
- fix makefile with patch 0
- spec file clean

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 31 2007 Oden Eriksson <oeriksson@mandriva.com> 2.0-2mdv2008.0
+ Revision: 76772
- rebuild


* Sat Mar 10 2007 Olivier Blin <oblin@mandriva.com> 2.0-1mdv2007.1
+ Revision: 140476
- initial release
- Create liblzf

