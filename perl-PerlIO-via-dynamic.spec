%define realname	PerlIO-via-dynamic

Name:		perl-%{realname}
Version:        0.12
Release: %mkrel 3
License:	GPL or Artistic
Group:		Development/Perl
Summary:        Perl module that helps creating dynamic PerlIO layers
Source0:        http://search.cpan.org/CPAN/authors/id/C/CL/CLKAO/%{realname}-%{version}.tar.gz
Url:		http://www.cpan.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel
BuildArch:      noarch

%description
PerlIO::via::dynamic is used for creating dynamic PerlIO layers.
It is useful when the behavior or the layer depends on variables.

%prep
%setup -q -n %{realname}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README CHANGES
%{perl_vendorlib}/*
%{_mandir}/man3/* 

