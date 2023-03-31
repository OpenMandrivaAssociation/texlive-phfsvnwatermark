Name:		texlive-phfsvnwatermark
Version:	41870
Release:	2
Summary:	Watermarks with version control information from SVN
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/phfsvnwatermark
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/phfsvnwatermark.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/phfsvnwatermark.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/phfsvnwatermark.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package allows you to add version control information as a
gray watermark on each page of your document. The SVN info is
read from keyword tags such as $Id$, $Date$, and $Author$ via
the svn or svn-multi packages.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/phfsvnwatermark
%{_texmfdistdir}/tex/latex/phfsvnwatermark
%doc %{_texmfdistdir}/doc/latex/phfsvnwatermark

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
