%define rname	lzf
%define major	1
%define libname	%mklibname %{rname} %{major}
%define devname	%mklibname %{rname} -d

Summary:	Very small data compression library
Name:		liblzf
Version:	3.6
Release:	7
License:	BSD
Group:		System/Libraries
Url:		http://liblzf.plan9.de/
Source0:	http://dist.schmorp.de/liblzf/%{name}-%{version}.tar.gz
Patch0:		liblzf-3.1-makefile.patch
Patch1:		liblzf-3.4-LDFLAGS.diff
# MD from fedora makes a proper shared lib
Patch2:		liblzf-3.6-autoconf.patch

%description
LZF is an extremely fast (not that much slower than a pure memcpy)
compression algorithm. It is ideal for applications where you want to
save *some* space but not at the cost of speed. It is ideal for
repetitive data as well. The module is self-contained and very small.

%package -n %{rname}
Summary:	Tools for the %{rname} compression library
Group:		Archiving/Compression

%description -n	%{rname}
This package contains tools for the %{rname} library.

%package -n %{libname}
Summary:	Shared library for %{name}
Group:		System/Libraries

%description -n	%{libname}
This package contains the shared library for %{name}.

%package -n %{devname}
Summary:	Development tools for the %{rname} compression library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	liblzf-devel < 3.6-2

%description -n	%{devname}
This package contains the header files and libraries needed for
developing programs using the %{rname} library.

%prep
%setup -q
%apply_patches
sh ./bootstrap.sh

%build
%configure2_5x \
	--disable-static
%make

%install
%makeinstall_std

%files -n %{rname}
%doc README
%{_bindir}/%{rname}

%files -n %{libname}
%{_libdir}/%{name}.so.%{major}*

%files -n %{devname}
%{_includedir}/%{rname}.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/liblzf.pc

