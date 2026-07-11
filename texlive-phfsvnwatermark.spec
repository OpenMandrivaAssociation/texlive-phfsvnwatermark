%global tl_name phfsvnwatermark
%global tl_revision 41870

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Watermarks with version control information from SVN
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/phfsvnwatermark
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/phfsvnwatermark.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/phfsvnwatermark.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/phfsvnwatermark.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package allows you to add version control information as a gray
watermark on each page of your document. The SVN info is read from
keyword tags such as $Id$, $Date$, and $Author$ via the svn or svn-multi
packages.

