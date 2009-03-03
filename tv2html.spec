%include	/usr/lib/rpm/macros.perl
Summary:	XMLTV to HTML converter
Summary(pl.UTF-8):	Konwerter XMLTV do HTML-a
Name:		tv2html
Version:	0.1.1
Release:	0.1
License:	GPL v2+
Group:		Applications
Source0:	http://tobyinkster.co.uk/Software/linux/tv2html/%{name}-%{version}.txt
# Source0-md5:	f5c29413634a3d73aa68f1f34f3943e5
Source1:	http://tobyinkster.co.uk/Software/linux/tv2html/xmltv.css
# Source1-md5:	7f1da9cea1220ee871f0073c3710f59f
URL:		http://tobyinkster.co.uk/tv2html
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Perl script that converts a sorted XML file made by XMLTV into a
nicely formatted HTML TV guide.

%description -l pl.UTF-8
Skrypt Perla przekształcający posortowany plik XML stworzony przez
XMLTV na ładnie sformatowany przewodnik telewizyjny w HTML-u.

%prep
%setup -q -c -T
cp %{SOURCE0} %{name}
cp %{SOURCE1} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.css
%attr(755,root,root) %{_bindir}/*
