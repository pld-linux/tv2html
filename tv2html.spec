%include	/usr/lib/rpm/macros.perl
Summary:	XMLTV to HTML converter
Name:		tv2html
Version:	0.0.4
Release:	0.2
License:	GPL v2+
Group:		Applications
Source0:	http://tobyinkster.co.uk/Software/linux/tv2html/tv2html-0.0.4.txt
# Source0-md5:	d233b50c1e78746a61bef7cd7677c4a7
Source1:	http://tobyinkster.co.uk/Software/linux/tv2html/xmltv.css
# Source1-md5:	7f1da9cea1220ee871f0073c3710f59f
URL:		http://tobyinkster.co.uk/tv2html
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Perl script that converts a sorted XML file made by XMLTV
into a nicely formatted HTML TV guide.

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
