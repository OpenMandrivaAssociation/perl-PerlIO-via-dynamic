%define upstream_name	 PerlIO-via-dynamic
%define upstream_version 0.13

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Perl module that helps creating dynamic PerlIO layers
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/C/CL/CLKAO/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Internals)
BuildArch:	noarch

%description
PerlIO::via::dynamic is used for creating dynamic PerlIO layers.
It is useful when the behavior or the layer depends on variables.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README CHANGES
%{perl_vendorlib}/*
%{_mandir}/man3/* 

%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.130.0-2mdv2011.0
+ Revision: 658875
- rebuild for updated spec-helper

* Mon Aug 03 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.130.0-1mdv2010.0
+ Revision: 407961
- rebuild using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.13-4mdv2009.0
+ Revision: 268710
- rebuild early 2009.0 package (before pixel changes)

* Mon Jun 02 2008 Olivier Thauvin <nanardon@mandriva.org> 0.13-3mdv2009.0
+ Revision: 214244
- 0.13
- update buildrequires

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 16 2007 Thierry Vignaud <tv@mandriva.org> 0.12-3mdv2008.0
+ Revision: 64194
- rebuild

* Tue May 08 2007 Olivier Thauvin <nanardon@mandriva.org> 0.12-2mdv2008.0
+ Revision: 25178
- rebuild


* Wed Apr 05 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.12-1mdk
- New release 0.12
- use mkrel

* Sun Feb 06 2005 Sylvie Terjan <erinmargault@mandrake.org> 0.11-2mdk
- rebuild for new perl

* Tue Sep 21 2004 Michael Scherer <misc@mandrake.org> 0.11-1mdk
- New release 0.11

* Tue Aug 31 2004 Michael Scherer <misc@mandrake.org> 0.02-2mdk 
- rebuild for new perl ( [DIRM] )

* Fri Apr 02 2004 Michael Scherer <misc@mandrake.org> 0.02-1mdk 
- First MandrakeSoft Package

