%include	/usr/lib/rpm/macros.perl
%define	pdir	Lingua
%define	pnam	IW-Logical
Summary:	Lingua::IW::Logical perl module
Summary(pl):	Modu� perla Lingua::IW::Logical
Name:		perl-Lingua-IW-Logical
Version:	0.5
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lingua::IW::Logical module is intended to automate task of converting
logical Hebrew to visual Hebrew.

%description -l pl
Modu� Lingua::IW::Logical jest przeznaczony do automatyzacji zada�
konwersji pomi�dzy logicznym i wizualnym hebrajskim.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%dir %{perl_vendorlib}/Lingua/IW
%{perl_vendorlib}/Lingua/IW/Logical.pm
%{_mandir}/man3/*