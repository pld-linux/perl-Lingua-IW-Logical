%include	/usr/lib/rpm/macros.perl
Summary:	Lingua-IW-Logical perl module
Summary(pl):	Modu� perla Lingua-IW-Logical
Name:		perl-Lingua-IW-Logical
Version:	0.4
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Lingua/Lingua-IW-Logical-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Lingua-IW-Logical module is intended to automate task of converting logical
Hebrew to visual Hebrew. 

%description -l pl
Modu� Lingua-IW-Logical jest przeznaczony do automatyzacji zada� konwersji
pomi�dzy logicznym i wizualnym hebrajskim.

%prep
%setup -q -n Lingua-IW-Logical-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Lingua/IW/Logical
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README}.gz

%{perl_sitelib}/Lingua/IW/Logical.pm
%{perl_sitearch}/auto/Lingua/IW/Logical

%{_mandir}/man3/*
