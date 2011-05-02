%define rname lzf

%define common_description LZF is an extremely fast (not that much slower than a pure memcpy) \
compression algorithm. It is ideal for applications where you want to \
save *some* space but not at the cost of speed. It is ideal for \
repetitive data as well. The module is self-contained and very small.

Summary:	Very small data compression library
Name:		lib%{rname}
Version:	3.4
Release:	%mkrel 5
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
