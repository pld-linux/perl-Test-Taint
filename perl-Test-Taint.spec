#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Test
%define		pnam	Taint
Summary:	Test::Taint - tools to test taintedness
Summary(pl.UTF-8):	Test::Taint - narzędzia do sprawdzania napiętnowania
Name:		perl-Test-Taint
Version:	1.08
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d59152acb169a34640bec861fca170de
URL:		http://search.cpan.org/dist/Test-Taint/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tainted data is data that comes from an unsafe source, such as the
command line, or, in the case of web apps, any GET or POST
transactions (see perlsec(1) man page for details on why tainted data
is bad, and how to untaint the data).

When you're writing unit tests for code that deals with tainted data,
you'll want to have a way to provide tainted data for your routines to
handle, and easy ways to check and report on the taintedness of your
data, in standard Test::More style.

%description -l pl.UTF-8
Dane napiętnowane to dane pochodzące z niebezpiecznego źródła, takiego
jak linia poleceń, lub, w przypadku aplikacji WWW, wszelkie transakcje
GET i POST (na stronie podręcznika perlsec(1) można znaleźć
dokładniejsze informacje dlaczego dane napiętnowane są złe i jak
pozbyć się z nich piętna).

Przy pisaniu testów jednostkowych dla kodu przetwarzającego dane
napiętnowane zwykle chcemy móc dostarczyć napiętnowane dane do
własnych funkcji i w łatwy sposób sprawdzić napiętnowanie naszych
danych w standardowym stylu Test::More.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorarch}/Test/Taint.pm
%dir %{perl_vendorarch}/auto/Test/Taint
%attr(755,root,root) %{perl_vendorarch}/auto/Test/Taint/Taint.so
%{_mandir}/man3/Test::Taint.3pm*
