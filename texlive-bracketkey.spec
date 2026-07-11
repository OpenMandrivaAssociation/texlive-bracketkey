%global tl_name bracketkey
%global tl_revision 17129

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Produce bracketed identification keys
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bracketkey
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bracketkey.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bracketkey.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides an environment bracketkey for use when producing
lists of species.

