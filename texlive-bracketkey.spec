Name:		texlive-bracketkey
Version:	1.0
Release:	1
Summary:	Produce bracketed identification keys
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bracketkey
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bracketkey.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bracketkey.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides an environment bracketkey for use when
producing lists of species.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bracketkey/bracketkey.sty
%doc %{_texmfdistdir}/doc/latex/bracketkey/Malva.pdf
%doc %{_texmfdistdir}/doc/latex/bracketkey/Malva.tex
%doc %{_texmfdistdir}/doc/latex/bracketkey/README
%doc %{_texmfdistdir}/doc/latex/bracketkey/bracketkey.pdf
%doc %{_texmfdistdir}/doc/latex/bracketkey/bracketkey.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
