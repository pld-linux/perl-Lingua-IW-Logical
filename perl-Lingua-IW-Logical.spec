%include	/usr/lib/rpm/macros.perl
Summary:	Lingua-IW-Logical perl module
Summary(pl):	Modu� perla Lingua-IW-Logical
Name:		perl-Lingua-IW-Logical
Version:	0.5
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Lingua/Lingua-IW-Logical-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lingua-IW-Logical module is intended to automate task of converting
logical Hebrew to visual Hebrew.

%description -l pl
Modu� Lingua-IW-Logical jest przeznaczony do automatyzacji zada�
konwersji pomi�dzy logicznym i wizualnym hebrajskim.

%prep
%setup -q -n Lingua-IW-Logical-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Lingua/IW/Logical.pm
%{_mandir}/man3/*
