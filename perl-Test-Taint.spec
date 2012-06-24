#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Test
%define	pnam	Taint
Summary:	Test::Taint - tools to test taintedness
Summary(pl):	Test::Taint - narz�dzia do sprawdzania napi�tnowania
Name:		perl-Test-Taint
Version:	1.00
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fef3d4268fcefe471b2b46baeb8e36a6
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
#BuildRequires:	perl-Test-Pod-Coverage >= 0.08
BuildRequires:	perl-Test-Pod >= 1.00
%endif
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

%description -l pl
Dane napi�tnowane to dane pochodz�ce z niebezpiecznego �r�d�a, takiego
jak linia polece�, lub, w przypadku aplikacji WWW, wszelkie transakcje
GET i POST (na stronie podr�cznika perlsec(1) mo�na znale��
dok�adniejsze informacje dlaczego dane napi�tnowane s� z�e i jak
pozby� si� z nich pi�tna).

Przy pisaniu test�w jednostkowych dla kodu przetwarzaj�cego dane
napi�tnowane zwykle chcemy m�c dostarczy� napi�tnowane dane do
w�asnych funkcji i w �atwy spos�b sprawdzi� napi�tnowanie naszych
danych w standardowym stylu Test::More.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
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
%{perl_vendorarch}/auto/Test/Taint/Taint.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Test/Taint/Taint.so
%{_mandir}/man3/*
