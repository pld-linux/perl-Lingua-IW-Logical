%include	/usr/lib/rpm/macros.perl
%define	pdir	Lingua
%define	pnam	IW-Logical
Summary:	Lingua::IW::Logical perl module
Summary(pl):	Modu³ perla Lingua::IW::Logical
Name:		perl-Lingua-IW-Logical
Version:	0.5
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lingua::IW::Logical module is intended to automate task of converting
logical Hebrew to visual Hebrew.

%description -l pl
Modu³ Lingua::IW::Logical jest przeznaczony do automatyzacji zadañ
konwersji pomiêdzy logicznym i wizualnym hebrajskim.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%dir %{perl_sitelib}/Lingua/IW
%{perl_sitelib}/Lingua/IW/Logical.pm
%{_mandir}/man3/*
