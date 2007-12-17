%define rname lzf
%define name lib%{rname}
%define version 2.0
%define release %mkrel 2

%define common_description LZF is an extremely fast (not that much slower than a pure memcpy) \
compression algorithm. It is ideal for applications where you want to \
save *some* space but not at the cost of speed. It is ideal for \
repetitive data as well. The module is self-contained and very small.

Summary: Very small data compression library
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: BSD
Group: System/Libraries
Url: http://liblzf.plan9.de/

%description
%{common_description}

%package -n %{rname}
Summary: Tools for the %{rname} compression library
Group: Archiving/Compression

%description -n	%{rname}
%{common_description}

This package contains tools for the %{rname} library.

%package -n %{name}-devel
Summary: Development tools for the %{rname} compression library
Group: Development/C
Provides: %{rname}-devel

%description -n	%{name}-devel
%{common_description}

This package contains the header files and libraries needed for
developing programs using the %{rname} library.

%prep
%setup -q
%configure2_5x

%build
%make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files -n %{rname}
%defattr(-,root,root)
%{_bindir}/%{rname}

%files -n %{name}-devel
%defattr(-,root,root)
%{_includedir}/%{rname}.h
%{_libdir}/%{name}.a
