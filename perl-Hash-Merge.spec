#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Hash-Merge
Version  : 0.302
Release  : 19
URL      : https://cpan.metacpan.org/authors/id/H/HE/HERMES/Hash-Merge-0.302.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/H/HE/HERMES/Hash-Merge-0.302.tar.gz
Summary  : 'Merges arbitrarily deep hashes into a single hash'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Hash-Merge-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Clone::Choose)

%description
# NAME
Hash::Merge - Merges arbitrarily deep hashes into a single hash
# SYNOPSIS

%package dev
Summary: dev components for the perl-Hash-Merge package.
Group: Development
Provides: perl-Hash-Merge-devel = %{version}-%{release}
Requires: perl-Hash-Merge = %{version}-%{release}

%description dev
dev components for the perl-Hash-Merge package.


%package perl
Summary: perl components for the perl-Hash-Merge package.
Group: Default
Requires: perl-Hash-Merge = %{version}-%{release}

%description perl
perl components for the perl-Hash-Merge package.


%prep
%setup -q -n Hash-Merge-0.302
cd %{_builddir}/Hash-Merge-0.302

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Hash::Merge.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Hash/Merge.pm
