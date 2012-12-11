%define upstream_name    Devel-Trace
%define upstream_version 0.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	A debugging module that prints out each line before it is executed
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Devel/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
A debugging module that prints out each line before it is executed
(like sh -x).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
echo "" | make test

%install
%makeinstall_std

%files
%{perl_vendorlib}/Devel
%{_mandir}/*/*


%changelog
* Sun Apr 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.110.0-1mdv2011.0
+ Revision: 654064
- update to new version 0.11

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.100.0-1mdv2011.0
+ Revision: 406983
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.10-5mdv2009.0
+ Revision: 256672
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.10-3mdv2008.1
+ Revision: 135833
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Jan 14 2007 Olivier Thauvin <nanardon@mandriva.org> 0.10-3mdv2007.0
+ Revision: 108542
- enable test, rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-Devel-Trace

* Sat Jun 18 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.10-2mdk
- Rebuild

* Fri May 14 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.10-1mdk
- Initial mdk release

