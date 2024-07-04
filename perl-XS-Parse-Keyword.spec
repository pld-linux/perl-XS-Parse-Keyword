#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	XS
%define		pnam	Parse-Keyword
Summary:	XS::Parse::Keyword - XS functions to assist in parsing keyword syntax
Summary(pl.UTF-8):	XS::Parse::Keyword - funkcje XS pomagające w analizie składni słów kluczowych
Name:		perl-XS-Parse-Keyword
Version:	0.43
Release:	1
# same as perl 5
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-authors/id/P/PE/PEVANS/XS-Parse-Keyword-%{version}.tar.gz
# Source0-md5:	e7ba804b20349dfec79cf4de93e81fa3
URL:		https://metacpan.org/dist/XS-Parse-Keyword
BuildRequires:	perl-ExtUtils-CChecker >= 0.11
BuildRequires:	perl-ExtUtils-ParseXS >= 3.16
BuildRequires:	perl-Module-Build >= 0.4004
BuildRequires:	perl-devel >= 1:5.14.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-File-ShareDir >= 1.0
BuildRequires:	perl-Test2-Suite
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides some XS functions to assist in writing syntax
modules that provide new perl-visible syntax, primarily for authors of
keyword plugins using the PL_keyword_plugin hook mechanism.

%description -l pl.UTF-8
Ten moduł udostępnia funkcje XS pomagające w pisaniu modułów
składniowych, dostarczających składnię widoczną dla Perla, głównie dla
autorów wtyczek składniowych wykorzystujący mechanizm uchwytów
PL_keyword_plugin.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	config=optimize="%{rpmcflags}" \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build 

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/auto/XS/Parse/Keyword/Keyword.bs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorarch}/XS
%dir %{perl_vendorarch}/XS/Parse
%{perl_vendorarch}/XS/Parse/Infix
%{perl_vendorarch}/XS/Parse/Keyword
%{perl_vendorarch}/XS/Parse/Infix.pm
%{perl_vendorarch}/XS/Parse/Keyword.pm
%dir %{perl_vendorarch}/auto/XS
%dir %{perl_vendorarch}/auto/XS/Parse
%dir %{perl_vendorarch}/auto/XS/Parse/Keyword
%attr(755,root,root) %{perl_vendorarch}/auto/XS/Parse/Keyword/Keyword.so
%{perl_vendorarch}/auto/share/dist/XS-Parse-Keyword
%{_mandir}/man3/XS::Parse::Infix*.3pm*
%{_mandir}/man3/XS::Parse::Keyword*.3pm*
